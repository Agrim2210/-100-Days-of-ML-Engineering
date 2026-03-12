# Mathematical Foundation — Feature Scaling

## Why Scaling Matters

Consider a regression model:

y = w₁x₁ + w₂x₂ + b

If the features have very different magnitudes:

x₁ (size) → 500–5000
x₂ (rooms) → 1–6

The gradient of the loss function depends on the feature values.

∂L/∂w₁ ∝ x₁
∂L/∂w₂ ∝ x₂

As a result, gradients for large-scale features dominate the optimization process.

This leads to inefficient updates and slow convergence.

---

## Standardization

A common scaling technique is **standardization**.

Formula:

x' = (x − μ) / σ

Where:

μ = mean of the feature
σ = standard deviation

After transformation:

* mean becomes 0
* standard deviation becomes 1

---

## Effect on Optimization

Without scaling:

* loss surface becomes elongated
* gradient descent follows a zig-zag path

With scaling:

* loss surface becomes more symmetric
* gradient descent converges faster

Feature scaling therefore improves optimization efficiency without changing the underlying data relationships.
