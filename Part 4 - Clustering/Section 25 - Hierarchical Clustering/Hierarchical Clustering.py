# Hierarchical Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'E:\\WORKSTATION\\Machine Learning Training\\Machine Learning A-Z™ Hands-On Python and R In Data Science\\Part 4 - Clustering\\Section 25 - Hierarchical Clustering\\Dataset\\Mall Customers.csv'
dataset = pd.read_csv(filepath)
X = dataset.iloc[:,[3, 4]].values

# Using the dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()