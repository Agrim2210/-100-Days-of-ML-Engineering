# Day 4 — Regularization (L1 vs L2)

## Problem

Machine learning models often suffer from **overfitting**, where the model learns noise in the training data instead of the true pattern.

Overfitting usually occurs when model parameters (weights) become excessively large, allowing the model to fit the training data too closely.

Regularization techniques help control model complexity by penalizing large weights.

This experiment investigates two common regularization techniques:

* **L2 Regularization (Ridge Regression)**
* **L1 Regularization (Lasso Regression)**

---

## Objective

The objective of this experiment is to:

* Understand why regularization is necessary
* Compare L1 and L2 regularization
* Observe how regularization affects model weights
* Analyze how different penalties influence model complexity

---

## Approach

1. Train a standard linear regression model.
2. Train a Ridge regression model (L2 regularization).
3. Train a Lasso regression model (L1 regularization).
4. Compare model coefficients and predictions.
