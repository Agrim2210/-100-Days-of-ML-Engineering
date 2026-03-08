import numpy as np 
class LogisticRegression:
    def __init__(self,lr,epochs):
        self.lr=lr
        self.epochs=epochs 
    def sigmoid(self,z):
        z=np.clip(z,-500,500)
        return 1/(1+np.exp(-z) )   
    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.w=np.zeros(n_features)
        self.b=0
        self.loss_history=[]
        for _ in range(self.epochs):
            linear=np.dot(X,self.w)+self.b 
            y_pred=self.sigmoid(linear)
            y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)
            error=y-y_pred
            dw=(-1/n_samples)*np.dot(X.T,error)    
            db=(-1/n_samples)*np.sum(error)
            self.w-=self.lr*dw
            self.b-=self.lr*db 
            loss = -np.mean(
                y*np.log(y_pred ) +
                (1-y)*np.log(1-y_pred )
            )
            self.loss_history.append(loss)
            
    def predict(self,X):
        linear=np.dot(X,self.w)+self.b 
        probs=self.sigmoid(linear)
        return (probs>=0.5).astype(int)
