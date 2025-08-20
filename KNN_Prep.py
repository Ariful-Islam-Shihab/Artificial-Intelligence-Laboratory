import numpy as np # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from collections import Counter
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Making dataset
X,y=make_classification(
    n_samples=200,
    n_features=5,
    n_informative=2,
    n_redundant=0,
    random_state=69,
    n_clusters_per_class=1,
)
print(X,y) 
# if already given

# hours_studied=[2,3.5,6,1,4,6,1.5,3,2.5,4.5]
# hours_slept=[7,6,8,5,6.5, 8.5,6,7,5,7.5]
# prior_grade=[70, 65, 80, 50, 78, 85, 73, 75, 55, 82,]
# results=[0 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,0, 1]
# print(len(hours_studied)==len(hours_slept)==len(prior_grade)==len(results))
# X=np.array([
#     hours_studied,hours_slept,prior_grade
# ]
# ).T
print(X.shape)
# print(y.shape)
# if y is given in another format
# label={0:'fail',1:'pass'}
# results_mod=[ label[i] for i in results]
# y=np.array(
#     results_mod,
# )
# for 
# y=np.array(
# )
#     results,
print(y.shape)
class KNN:
    def __init__(self,X,y,k):
        self.X=X
        self.y=y
        self.k=k
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X,y,random_state=42,test_size=0.2)
        self.predict_all_KNN()
        


    def euclidean_distance(self,a,b):
        return np.sqrt(np.sum((a-b)**2))

    def KNN(self,x_query):
        distances=[self.euclidean_distance(x_query,x_train) for x_train in self.X_train]
        k_neigbour_indices=np.argsort(distances)[:self.k]
        k_neigbour_labels=[self.y_train[i] for i in k_neigbour_indices ]
        label_counter=Counter(k_neigbour_labels)
        predicted=label_counter.most_common(1)[0][0]
        return predicted
    
    def predict_all_KNN(self):
        self.predictions=[]
        for x_query in self.X_test:
            predicted=self.KNN(x_query)
            self.predictions.append(predicted)

    def scores(self):
        predictions = np.array(self.predictions)
        self.accuracy = accuracy_score(self.y_test, predictions)
        self.precision = precision_score(self.y_test, predictions, average='binary')
        self.f1 = f1_score(self.y_test, predictions, average='binary')
        self.recall = recall_score(self.y_test, predictions, average='binary')
        self.all_scores = np.array([self.accuracy, self.precision, self.f1, self.recall])
        return self.all_scores

    

knn_model=KNN(X=X,y=y,k=3)
print(knn_model.scores())
print(i for i in knn_model.predictions)
