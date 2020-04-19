# Data Preprocessing

# Step 1: Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Step 2: Importing the dataset
dataset = pd.read_csv('E:\WORKSTATION\Machine Learning Training\Machine Learning A-Z™ Hands-On Python and R In Data Science\Part 1 - Data Preprocessing\Dataset\Data.csv')
# Creating a matrix of independent variables
X = dataset.iloc[:, :-1].values
# Creating dependent variable vector
Y = dataset.iloc[:, 3].values

# Step 3: Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3]) 

# Step 4: Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Encode "Country" column
labelEncoder_X = LabelEncoder() 
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])

# Dummy Encoding "Country" column
oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()

labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

# Step 5: Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Step 6: Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
# For the test set we don’t need to fit the sc_X object because it's already fitted to the training set.
X_test = sc_X.transform(X_test)