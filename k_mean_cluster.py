import numpy as np
from sklearn.metrics import accuracy_score

# print(X.shape)

class KMeansCluster:
    def __init__(self,n_clusters,max_iterations,tol):
        self.n_clusters=n_clusters
        self.max_iterations=max_iterations
        self.tol=tol
        self.centroids=None
        self.labels=None

    def euclidean_distance(self,a,b):
        return np.sqrt(np.sum((a-b)**2))
    
    def initialize_centroids(self,X):
        n_samples=X.shape[0]
        np.random.seed(69)
        random_indices=np.random.choice(n_samples,self.n_clusters,replace=False)
        return np.array(X[random_indices])
    
    def assign_centroids(self,X):
        labels=[]
        for x in X:
            distance=[self.euclidean_distance(x,i) for i in self.centroids]
            labels.append(np.argmin(distance))

        return np.array(labels)
    
    def update_centroids(self,X):
        updated_centroids=[]
        for i in range(self.n_clusters):
            points_that_belong=[]
            for j,point in enumerate(X):
                if self.labels[j]==i:
                    points_that_belong.append(point)

            updated_centroids.append(np.mean(points_that_belong,axis=0))

        return np.array(updated_centroids)
    
    def train(self,X):
        self.centroids=self.initialize_centroids(X)
        for i in range(self.max_iterations):
            old_centroids=self.centroids
            self.labels=self.assign_centroids(X)
            self.centroids=self.update_centroids(X)
            diff=self.euclidean_distance(old_centroids,self.centroids)
            if np.max(diff)<self.tol:
                return
            

    def predict(self,X):
        return self.assign_centroids(X)
    

monthly_spending=np.array(
    [100,250,700,50,1800,900,120,1600,60,1100]
)
number_of_visits=np.array(
    [2,5,10,1,3,12,7,2,15,8]
)
X=np.array(
    [
        monthly_spending,number_of_visits
    ]
).T
n_clusters=3
tol=1e-4
max_iterations=100
model=KMeansCluster(n_clusters=n_clusters,max_iterations=max_iterations,tol=tol)
model.train(X)
X_sample=np.array(
    [
        [300,4],
        [1500,1]
    ]
)
y=model.predict(X_sample)
for i in range(len(X_sample)):
    print(f'Customer {i} with features "{X_sample[i]}" is assigned to Cluster {y[i]}')