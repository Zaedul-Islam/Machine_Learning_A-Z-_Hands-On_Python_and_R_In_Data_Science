# Data Preprocessing

# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('E:\WORKSTATION\Machine Learning Training\Machine Learning A-Z™ Hands-On Python and R In Data Science\Part 1 - Data Preprocessing\Dataset\Data.csv')
# Creating a matrix of independent variables
X = dataset.iloc[:, :-1].values
# Creating dependent variable vector
Y = dataset.iloc[:, 3].values
