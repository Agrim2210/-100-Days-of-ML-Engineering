# Day 3 — Bias vs Variance Experiment

## Problem

Machine learning models must generalize well to unseen data.

If a model is too simple, it cannot capture the true relationship between variables.
If a model is too complex, it may memorize the training data and fail to generalize.

This experiment investigates the **bias–variance tradeoff** using polynomial regression models of different complexities.

## Objective

Train models with different polynomial degrees and observe:

* Underfitting
* Proper model complexity
* Overfitting

We will compare training and validation errors to understand how model complexity affects generalization.

## Approach

1. Generate polynomial features of different degrees.
2. Train regression models with increasing complexity.
3. Compare prediction curves and errors.
4. Analyze bias–variance behavior.
