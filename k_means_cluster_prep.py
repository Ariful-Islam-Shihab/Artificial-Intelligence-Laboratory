import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from matplotlib.animation import FuncAnimation

class kMeansCluster:
    def __init__(self,n_cluster,max_iter=300,tol=1e-4):
        self.n_cluster=n_cluster
        self.max_iter=max_iter
        self.tol=tol
        self.centroid=None
        self.labels=None
        self.history=[]

    def euclidean_distance(self,a,b):
        return np.sqrt(np.sum((a-b)**2))

    # Randomly select centroid
    def assign_centroids(self,X):
        np.random.seed(43)
        n_samples=X.shape[0]
        random_indices=np.random.choice(n_samples,self.n_cluster,replace=False)
        return X[random_indices]
    
    # find labels for each points
    def assign_cluster(self,X):
        labels=[]
        for points in X:
            distances=[]
            for center in self.centroid:
                distances.append(self.euclidean_distance(points,center))
            labels.append(np.argmin(distances))
        return np.array(labels)
    
    def update_centroids(self,X):
        new_centroid=[]
        for centers in range(self.n_cluster):
            cluster_points=[]
            for idx,point in enumerate(X):
                if self.labels[idx]==centers:
                    cluster_points.append(point)
            new_centroid.append(np.mean(cluster_points,axis=0))
        return np.array(new_centroid)

    def train(self,X):
        self.centroid=self.assign_centroids(X)
        for i in range(self.max_iter):
            old_centroids=self.centroid
            self.labels=self.assign_cluster(X)
            self.centroid=self.update_centroids(X)
            self.history.append(self.centroid.copy())
            ds=[]
            for i in range(self.n_cluster):
                ds.append(self.euclidean_distance(old_centroids[i],self.centroid[i]))
            if max(ds)<self.tol:
                break

    def predict(self,X):
        return self.assign_cluster(X)


def animate_kmeans(X, model):
    fig, ax = plt.subplots(figsize=(8, 6))

    scatter = ax.scatter(X[:, 0], X[:, 1], c=model.labels, cmap='viridis', s=10)
    centroid_scat = ax.scatter([], [], c='red', marker='X', s=200)

    def update(frame):
        centroids = model.history[frame]
        centroid_scat.set_offsets(centroids)
        ax.set_title(f'Iteration {frame + 1}/{len(model.history)}')
        return centroid_scat,

    anim = FuncAnimation(fig, update, frames=len(model.history), interval=500, repeat=False)
    plt.show()

n_samples=100000
n_features=2
n_clusters=5
X,_=make_blobs(n_samples=n_samples,n_features=n_features,random_state=69,centers=n_clusters)
model = kMeansCluster(n_cluster=n_clusters)
model.train(X)

# Animate
animate_kmeans(X, model)
# plt.scatter(X[:,0],X[:,1],c=model.labels,cmap='managua_r',s=10,alpha=0.6)
# plt.scatter(model.centroid[:,0],model.centroid[:,1],c='red',marker='X',s=200)
# plt.show()