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
      # max_iter - The maximum number of iterations there can be to find the final clusters when the K-Means algorithm is running. 
      # The default value for this parameter is 300.
      # n_init - The number of times the K-Mean algorithm will be run with different initial centroid. 
      # The default value for this parameter is 300.
      # random_state - This fixes all the random factors of the K-Means process. Setting it to zero will always give the same results
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
# fit_predict method returns for each observation which cluster it belongs to. It will return this cluster numbers into a single vector
y_kmeans = kmeans.fit_predict(X)

# Visualizing the clusters
# Cluster are numbered from 0 to 4
# X[y_kmeans == 0, 0] - Plotting the x coordinates of all the observation points that belong to cluster 1
# y_kmeans == 0 - Taking the cluster 1, 0 - Specifying the first column of dataset X
# X[y_kmeans == 0, 1] - Plotting the y coordinates of all the observation points that belong to cluster 1
# s - Size of a observation
# c - Set the cluster color   
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Careful')
# Follow same thing for other 4 clusters
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Standard')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Target')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Careless')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Sensible')

# Plot the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')

# Caveat - For clustering in more than two dimensions, the below code block will not work properly 
plt.title('Clusters of clients') 
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()
