# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'E:\\WORKSTATION\Machine Learning Training\\Machine Learning A-Z™ Hands-On Python and R In Data Science\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\Dataset\\50 Startups.csv'
dataset = pd.read_csv(filepath)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding the categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,3] = labelEncoder_X.fit_transform(X[:, 3])
oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
# Note: Usually the library takes care of this phenomenon
X = X[:, 1:]
      
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_prediction = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.api as sm
# Step 1
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)

# Step 2
X_optimal = X[:, [0, 1, 2, 3, 4, 5]]
regressorOLS = sm.OLS(endog = y, exog = X_optimal).fit()

# Step 3
regressorOLS.summary()

# Step 4: Fitting model without x2 independent variable (2nd dummy variable)
X_optimal = X[:, [0, 1, 3, 4, 5]]
regressorOLS = sm.OLS(endog = y, exog = X_optimal).fit()

# Step 3
regressorOLS.summary()

# Step 4: Fitting model without x1 independent variable (1st dummy variable)
X_optimal = X[:, [0, 3, 4, 5]]
regressorOLS = sm.OLS(endog = y, exog = X_optimal).fit()

# Step 3
regressorOLS.summary()


# Step 4: Fitting model without Administration independent variable (1st dummy variable)
X_optimal = X[:, [0, 3, 5]]
regressorOLS = sm.OLS(endog = y, exog = X_optimal).fit()

# Step 3
regressorOLS.summary()

# Step 4: Fitting model without Marketing Spend independent variable (1st dummy variable)
X_optimal = X[:, [0, 3]]
regressorOLS = sm.OLS(endog = y, exog = X_optimal).fit()

# Step 3
regressorOLS.summary()
