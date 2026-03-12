import numpy as np
def gradient_descent(X, y, lr=0.00000001, epochs=200):

    n_samples, n_features = X.shape
    
    w = np.zeros(n_features)
    b = 0
    
    losses = []
    
    for _ in range(epochs):
        
        y_pred = np.dot(X, w) + b
        
        error = y_pred - y
        
        loss = np.mean(error**2)
        losses.append(loss)
        
        dw = (2/n_samples) * np.dot(X.T, error)
        db = (2/n_samples) * np.sum(error)
        
        w -= lr * dw
        b -= lr * db
        
    return losses