# Mathematical Foundations — Regression Metrics

## Mean Squared Error

MSE = (1/n) Σ (y - ŷ)²

This metric squares prediction errors, which penalizes large errors more heavily.

---

## Root Mean Squared Error

RMSE = √MSE

RMSE converts squared error into the same unit as the target variable.

---

## Mean Absolute Error

MAE = (1/n) Σ |y - ŷ|

MAE treats all errors equally by using absolute differences.

---

## R² Score

R² = 1 - (SSres / SStot)

This metric measures how much variance in the data is explained by the model.

R² ranges from negative values to 1, where higher values indicate better model performance.
