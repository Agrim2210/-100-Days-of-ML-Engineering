# Key Insights — Day 4 (L1 vs L2 Regularization)

## 1. Baseline Model (Linear Regression)

The linear regression model was trained without any regularization.
Its objective is purely to minimize prediction error (Mean Squared Error).

As a result, the model chooses coefficients that best fit the training data without considering model complexity.

Observed coefficients:

```
x1 ≈ 1.58
x2 ≈ 0.88
x3 ≈ 0.44
```

This model provides the baseline for comparison.

---

## 2. Effect of L2 Regularization (Ridge Regression)

Ridge regression modifies the loss function by adding a penalty on the squared magnitude of the weights.

Loss = MSE + λ Σ w²

This discourages very large coefficients and stabilizes the model.

In the experiment, the ridge coefficients became:

```
x1 ≈ 1.45
x2 ≈ 0.94
x3 ≈ 0.49
```

Although some coefficients increased slightly, the **overall magnitude of the weight vector decreased**. This is expected because ridge regularization minimizes the **total squared weight magnitude**, not each coefficient individually.

Key takeaway:

* Ridge stabilizes the model
* Coefficients are redistributed and slightly shrunk
* All features remain in the model

---

## 3. Effect of L1 Regularization (Lasso Regression)

Lasso regression uses a different penalty:

Loss = MSE + λ Σ |w|

This penalty has a special property: it can push some coefficients **exactly to zero**.

In the experiment:

```
x1 increased slightly
x2 decreased
x3 became approximately zero
```

This indicates that Lasso considered **x3 less important** and removed it from the model.

This demonstrates the **feature selection capability of L1 regularization**.

---

## 4. Interpretation of the Coefficient Comparison Plot

The coefficient comparison plot shows how different regularization methods affect model parameters.

Observations from the plot:

* Linear regression produces unrestricted coefficients.
* Ridge regression stabilizes coefficients by penalizing large values.
* Lasso regression simplifies the model by eliminating less important features.

This visualization clearly illustrates how regularization influences model complexity.

---

## 5. Bias–Variance Tradeoff

Regularization introduces a small increase in bias but significantly reduces variance.

This tradeoff helps improve the model’s ability to generalize to unseen data.

---

## Conclusion

This experiment highlights the key differences between L1 and L2 regularization.

* Ridge regression reduces model variance by shrinking coefficients.
* Lasso regression performs feature selection by driving some coefficients to zero.

Both techniques are powerful tools for controlling model complexity and preventing overfitting.
