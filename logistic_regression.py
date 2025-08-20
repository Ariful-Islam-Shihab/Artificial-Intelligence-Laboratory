import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
X=np.array([
    [20,3],
    [22,4],
    [25,5],
    [40,15],
    [45,18],
    [50,20]
])
y=np.array([0,0,0,1,1,1])
X_train,X_test,y_train,y_test=train_test_split(
    X,y,train_size=0.8,random_state=69
)
class Linear_regression:
    def __init__(self,learning_rate,epochs):
        self.learning_rate=learning_rate
        self.epochs=epochs
        self.weights=None
        self.bias=None       
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))


    def train(self,X,y):
        n_samples,n_features=X.shape
        self.weights=np.zeros(n_features)
        self.bias=0

        for i in range(self.epochs):
            linear_model=np.dot(X,self.weights)+self.bias
            y_predict=self.sigmoid(linear_model)

            dw=(1/n_samples)*np.dot(X.T,(y_predict-y))
            db=(1/n_samples)*np.sum(y_predict-y)

            self.weights-=self.learning_rate*dw
            self.bias-=self.bias

    def predict(self,X):
        linear_model=np.dot(X,self.weights)+self.bias
        y_predict=self.sigmoid(linear_model)

        results=[1 if i>0.5 else 0 for i in y_predict]

        return results
    

model=Linear_regression(learning_rate=0.05,epochs=10000)
model.train(X_train,y_train)
print(X_train)
print(y_train)
y_pred=model.predict(X_test)
print(accuracy_score(y_pred=y_pred,y_true=y_test))