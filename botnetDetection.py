# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('/Users/Chandler/Documents/Machine_Learning/BotnetData/botnetData.csv', nrows=50)

X = dataset.iloc[:, 0:5].values
X

y = dataset.iloc[:, 5].values
y

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


#Creating my base rate model
def base_rate_model(X):
    y = np.zeros(X.shape[0])
    return y
    
#Define Accurate of the base rate model
y_base_rate = base_rate_model(X_test)
from sklearn.metrics import accuracy_score
print("Base rate accuracy is %2.2f" % accuracy_score(y_test, y_base_rate))

#Accuracy of logistic regression'
print("Accuracy of logistic model %2.2f" % accuracy_score(y_test, y_pred))


#AUC Scores
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

print("---Base Model---")
base_roc_auc = roc_auc_score(y_test, base_rate_model(X_test))
print("Base Rate AUC = %2.2f" % base_roc_auc)
print(classification_report(y_test, base_rate_model(X_test)))

print("---Logistic Model---")
logit_roc_auc = roc_auc_score(y_test, y_pred)
print("Logistic Rate AUC = %2.2f" % base_roc_auc)
print(classification_report(y_test, y_pred))


#Graphing 
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])

plt.figure()
plt.plot(fpr, tpr, label = 'ROC Curve (area = %0.2f)' % logit_roc_auc)
plt.plot([0,1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.xlim([0.0, 1.05])
plt.xlabel('Flase Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Ralationship Between Flase Positive & True Positives')
plt.legend(loc = 'lower right')
plt.show()
