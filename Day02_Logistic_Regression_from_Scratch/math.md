# Mathematical Foundation — Logistic Regression

Logistic Regression is used for **binary classification problems**, where the target variable has two possible outcomes:

```
0 → Negative class
1 → Positive class
```

Unlike Linear Regression, which predicts continuous values, Logistic Regression predicts the **probability of belonging to a class**.

---

# 1. Linear Model

The model first computes a linear combination of the input features:

[
z = wX + b
]

Where:

* **X** → feature vector
* **w** → weight vector
* **b** → bias (intercept)

In vectorized form:

[
z = Xw + b
]

This value **z** can be any real number between:

```
−∞  to  +∞
```

Since probabilities must lie between **0 and 1**, we apply a transformation.

---

# 2. Sigmoid Function

Logistic Regression uses the **sigmoid function** to convert the linear output into a probability.

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

Properties of the sigmoid function:

* Output range: **0 to 1**
* Smooth and differentiable
* Suitable for probability modeling

Examples:

```
z = -5 → probability ≈ 0.006
z = 0  → probability = 0.5
z = 5  → probability ≈ 0.993
```

So the predicted probability becomes:

[
p = \sigma(Xw + b)
]

---

# 3. Classification Rule

The predicted probability is converted into a class label using a threshold:

```
if p ≥ 0.5 → class 1
if p < 0.5 → class 0
```

This creates a **decision boundary** separating the two classes.

---

# 4. Loss Function (Binary Cross-Entropy)

To train the model, we must measure how incorrect the predictions are.

Logistic Regression uses **Binary Cross-Entropy Loss**:

[
L = -\frac{1}{n} \sum_{i=1}^{n}
[y_i \log(p_i) + (1-y_i)\log(1-p_i)]
]

Where:

* **y** → true label
* **p** → predicted probability

Why this loss function?

Because it heavily penalizes **confident wrong predictions**.

Example:

| True Label | Prediction | Loss       |
| ---------- | ---------- | ---------- |
| 1          | 0.9        | small      |
| 1          | 0.1        | very large |

This encourages the model to produce **accurate probability estimates**.

---

# 5. Gradient Descent Optimization

The objective is to **minimize the cross-entropy loss**.

Parameters **w** and **b** are updated using gradient descent.

Weight gradient:

[
\frac{dL}{dw} = \frac{1}{n} X^T (p - y)
]

Bias gradient:

[
\frac{dL}{db} = \frac{1}{n} \sum (p - y)
]

Where:

```
p = predicted probability
y = true label
```

---

# 6. Parameter Update Rule

Weights are updated iteratively:

[
w = w - \alpha \frac{dL}{dw}
]

[
b = b - \alpha \frac{dL}{db}
]

Where:

```
α = learning rate
```

The learning rate controls how large the update step is.

* Too large → unstable training
* Too small → very slow convergence

---

# 7. Training Process

Each iteration of gradient descent performs:

1. Compute linear score

[
z = Xw + b
]

2. Apply sigmoid

[
p = \sigma(z)
]

3. Compute loss

[
L = -[y\log(p) + (1-y)\log(1-p)]
]

4. Compute gradients

```
dw = (1/n) Xᵀ(p − y)
db = (1/n) Σ(p − y)
```

5. Update parameters

```
w = w − αdw
b = b − αdb
```

This process repeats for many iterations until the model converges.

---

# 8. Connection to Linear Regression

Linear Regression:

```
Output → continuous value
Loss   → Mean Squared Error
```

Logistic Regression:

```
Output → probability
Loss   → Cross-Entropy
Activation → Sigmoid
```

Thus, Logistic Regression can be seen as a **probabilistic extension of linear models**.

---

# Conclusion

Logistic Regression combines:

* a linear decision function
* sigmoid probability transformation
* cross-entropy loss optimization

These ideas form the foundation of many modern machine learning and deep learning algorithms.
