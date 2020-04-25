# Logistic Regression

# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = './Dataset/Social Network Ads.csv'
dataset = pd.read_csv(filepath)
# Creating a matrix of independent variables
X = dataset.iloc[:,[2,3]].values
# Creating dependent variable vector
y = dataset.iloc[:,4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train = standardScaler.fit_transform(X_train)
X_test = standardScaler.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
logisticRegressionClassifier = LogisticRegression(random_state = 0)
logisticRegressionClassifier.fit(X_train, y_train)
