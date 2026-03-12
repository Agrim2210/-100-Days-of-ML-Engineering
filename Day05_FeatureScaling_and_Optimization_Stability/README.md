# Day 5 — Feature Scaling and Optimization

## Problem

Many machine learning algorithms rely on gradient-based optimization.
When input features have very different numerical scales, optimization becomes inefficient and unstable.

For example:

* house size may range from 500 to 5000
* number of rooms may range from 1 to 6

In such cases, gradient descent updates become imbalanced, causing slow convergence.

## Objective

This experiment investigates the effect of feature scaling on model training.

Specifically, we compare model behavior:

* without feature scaling
* with standardization

## Approach

1. Train a regression model on raw features.
2. Apply feature scaling using standardization.
3. Train the same model again.
4. Compare convergence and model coefficients.

This demonstrates how scaling improves optimization stability.
