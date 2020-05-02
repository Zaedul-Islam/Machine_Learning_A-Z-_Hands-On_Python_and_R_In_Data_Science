# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'E:\\WORKSTATION\\Machine Learning Training\\Machine Learning A-Z™ Hands-On Python and R In Data Science\\Part 4 - Clustering\\Section 24 - K-Means Clustering\\Dataset\\Mall Customers.csv'
dataset = pd.read_csv(filepath)
X = dataset.iloc[:,[3,4]].values

# Using the Elbow Method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11): # In range, the upper bound is exclusive
      # init - 'k-means++' intialization method overcomes the random initialization method trap
      # max_iter - The maximum number of iterations there can be to find the final clusters when the K-Means
      # algorithm is running. The default value for this parameter is 300.
      # n_init - The number of times the K-Mean algorithm will be run with different initial centroid. 
      # The default value for this parameter is 300.
      # random_state - This fixes all the random factors of the K-Means process. Setting it to zero will always
      # give the same results
      kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
      kmeans.fit(X)
      # inertia_ is another name WCSS
      wcss.append(kmeans.inertia_)
      
# Plotting the Elbow Method graph
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Applying K-Means to the Mall Customers dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
# fit_predict method returns for each observation which cluster it belongs to. It will return
# this cluster numbers into a single vector
y_kmeans = kmeans.fit_predict(X)