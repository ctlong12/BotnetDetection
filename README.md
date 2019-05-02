# Botnet Detection with Machine Learning

Semester-long research into botnets and their detection methods using machine learning algorithms. The machine learning model was created in Python with NumPy and Panda libraries.

## Abstract

  Malware and other phishing attempts are becoming more widely spread than ever before in the world today. People today continue to move more and more of their daily routines, memories, and transactions over to digital devices. The issue here lies with the amount of sensitive data people move over to their digital devices. This sensitive data gives hackers incentive and leaves people prone to attacks from black hat hackers attempting to gain and wrongfully use that data. Recently, there has been an increase in the use of botnets to obtain this sensitive data. A Botnet by definition is a network of private computers infected with malicious software and controlled as a group without the owners' knowledge These attacks implemented using botnet makes botnets a very dangerous threat to anyone using a device today. Previously completed research shows much difficulty in predicting malicious botnets. This ever-growing need for a solution to the rapidly increasing number of botnets on the internet today still remains up in the air. What makes this problem even more difficult is that not all botnets are technically malicious. Botnets are used by corporations every day to help solve costumer service related issues, help users buy products, and much more. Using machine learning, the goal is to properly identify a botnet on a website using key features that all botnets abide by. Once able to properly detect a botnet, many doors will open up in the world of cybersecurity that allow internet websites to manage this ongoing problem.

## The Approach

### Logistic Regression

<a target="_blank"><img src="http://i67.tinypic.com/16blmaa.jpg" border="0" alt="Logistic Regression"></a>

  To start the Logistic Regression model for botnet detection, specifying the independent and dependent variables in the model represented as , then from there plugging the into a sigmoid function. The sigmoid function creates a non-linear S-shaped curve where the curve has a finite limit of as approaches and 1 as approaches . Since the base case of the Sigmoid Function of is exactly 0.5, it is possible to accurately predict whether a variable is a 0 if its probability is less than 0.50, or a 1 is it is greater than 0.50. Mathematically this can be represented by taking our original value and plugging it into the Sigmoid Function represented by . From there it is possible to solve for the in terms of the Sigmoid Function which results in the equation . This equation will determine the probability and accurately classify the results. Luckily there are many library’s that are able to handle the heavy mathematics involved with this classification method.
  
### Random Forest 
 
<img align="right" width="400" height="350" src="http://i67.tinypic.com/bfgq5h.jpg" alt="Random Forest"></a>

For the second classification model we will be assigning a Random Forest Algorithm. Random Forest algorithms are a supervised classification algorithm. This algorithm creates the forest with a number of decision trees. The more trees in the forest the more in depth the forest looks. Random Forest is build off of the idea of bagging which is a method of repeatedly selecting data at random and then performing a decision tree classification method to it. The genius behind the Random Forest Algorithm is that each new tree in the algorithm is grown from the knowledge gained from the previous one. This method is highly accurate when applied to classification problems.

## The Results

#### Logistic Regression Results

The results for the area under the cruve model (AUC), but the model still yielded some very interesting results. A few of the more notable relationships between the features happened to be between the number of failed validations and login attempts, and the current byte flow along with the packet flow. The Logistic Regression model did a good job accurately classifying the relationships between these features compared to others.

<a target="_blank"><img src="http://i66.tinypic.com/258tqww.png" border="0" alt="Logistic Regression"></a>

#### Random Forest Results

The results from the Random Forest model stood out more than the Logistic Regression model. Once again the more notable relationships between the number of failed validations and login attempts. Even more outstanding was that the Random Forest Algorithm had better accuracy than the Logistic Regression model and the current byte flow along with the packet flow.
Using the AUC scoring method we can see that the prediction results were better than that of the Logistic Regression. We went from the base rate model AUC of 50% and increased the odds of predicting the correct outcome to 92%.


<a target="_blank"><img src="http://i67.tinypic.com/wwhus0.jpg" border="0" alt="Random Forest"></a>
