# Simple Linear Regression
 
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'E:\WORKSTATION\Machine Learning Training\Machine Learning A-Z™ Hands-On Python and R In Data Science\Part 2 - Regression\Simple Linear Regression\Dataset\Salary Data.csv'
dataset = pd.read_csv(filepath)
# Creating a matrix of independent variables (YearsExperience)
X = dataset.iloc[:, :-1].values
# Creating dependent variable vector (Salary)
Y = dataset.iloc[:, 1].values
 
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
Y_prediction = regressor.predict(X_test)

# Visualizing the Training set results
plt.scatter(X_train, Y_train, color = 'red')

