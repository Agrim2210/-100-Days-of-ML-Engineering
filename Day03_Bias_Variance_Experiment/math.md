# Mathematical Foundation — Bias vs Variance

## 1. Polynomial Regression

Polynomial regression extends linear regression by including higher-order terms.

A polynomial model of degree **d** can be written as:

[
y = w_0 + w_1x + w_2x^2 + w_3x^3 + ... + w_dx^d
]

This allows the model to capture **non-linear relationships**.

---

## 2. Model Complexity

The **degree of the polynomial** controls model complexity.

Example:

Degree 1:

[
y = w_0 + w_1x
]

Degree 3:

[
y = w_0 + w_1x + w_2x^2 + w_3x^3
]

Higher degrees allow the model to fit more complex patterns.

---

## 3. Bias

Bias measures how far model predictions are from the true relationship.

High bias occurs when the model is **too simple**.

Example:

* Linear model trying to fit a quadratic relationship.

This leads to **underfitting**.

---

## 4. Variance

Variance measures how sensitive the model is to training data.

High variance occurs when the model is **too complex**.

Example:

* Very high-degree polynomial fitting noise in the data.

This leads to **overfitting**.

---

## 5. Bias–Variance Tradeoff

Model performance depends on balancing bias and variance.

```
Low Complexity  → High Bias, Low Variance
Optimal Model   → Balanced Bias and Variance
High Complexity → Low Bias, High Variance
```

The goal is to find a model complexity that minimizes prediction error on unseen data.
