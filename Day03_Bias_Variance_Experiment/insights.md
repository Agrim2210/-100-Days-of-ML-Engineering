# Key Insights — Day 3 (Bias vs Variance)

## 1. Underfitting

When the polynomial degree is too low (e.g., degree = 1), the model cannot capture the true nonlinear relationship in the dataset.

This leads to:

* High training error
* Poor predictive performance

This phenomenon is known as **underfitting** and occurs due to **high bias**.

---

## 2. Appropriate Model Complexity

When using a moderate polynomial degree (e.g., degree = 3), the model is able to capture the underlying trend of the data.

Characteristics:

* Lower training error
* Good generalization

This represents a good balance between bias and variance.

---

## 3. Overfitting

When the polynomial degree becomes very large (e.g., degree = 10), the model starts fitting small fluctuations in the dataset.

This results in:

* Extremely low training error
* Poor generalization

This behavior is known as **overfitting** and occurs due to **high variance**.

---

## 4. Bias–Variance Tradeoff

The experiment demonstrates the importance of balancing model complexity.

A model that is too simple cannot learn the true pattern, while a model that is too complex memorizes the training data.

The optimal model lies between these extremes, achieving both low bias and low variance.

---

## Conclusion

This experiment highlights the critical role of model complexity in machine learning.
Choosing the right model complexity helps ensure that models generalize well to unseen data rather than memorizing training data.
