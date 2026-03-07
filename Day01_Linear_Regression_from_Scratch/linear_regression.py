import numpy as np
class LinearRegression:
    def __init__(self,lr,epochs):
        self.lr=lr
        self.epochs=epochs
    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.w=np.zeros(n_features)
        self.b=0 
        self.loss_history=[] 
        for _ in range(self.epochs):
            y_pred=np.dot(X,self.w) +self.b 
            error=y-y_pred
            dw=(-2/n_samples)*np.dot(X.T,error)
            db=(-2/n_samples)*np.sum(error)
            self.w-=self.lr*dw 
            self.b-=self.lr*db 
            loss=np.mean(error**2)
            self.loss_history.append(loss)
    def predict(self,X):
        return np.dot(X,self.w)+self.b         



        
