# Mathematical Foundation

Linear regression assumes a linear relationship between features and target.

Model equation:

y = wX + b

Where:

w = weight  
b = bias  

---

## Loss Function

Mean Squared Error:

L = (1/n) Σ (y_true - y_pred)^2

Goal:

Minimize L by adjusting parameters w and b.

---

## Gradient Descent

Update rule:

w = w - α * dL/dw

b = b - α * dL/db

Where α is the learning rate.

---

## Gradients

dL/dw = (-2/n) Σ X (y_true - y_pred)

dL/db = (-2/n) Σ (y_true - y_pred)
