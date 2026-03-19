# Mathematical Foundations — Multicollinearity & VIF

## Multicollinearity

Multicollinearity occurs when independent variables
are highly correlated with each other.

This leads to instability in coefficient estimation.

---

## Variance Inflation Factor (VIF)

VIF = 1 / (1 - R²)

Where R² is obtained by regressing one feature
against all other features.

---

## Interpretation

VIF = 1 → No correlation  
VIF > 5 → Moderate correlation  
VIF > 10 → High multicollinearity  

---

## Key Insight

High VIF increases variance of coefficient estimates,
making them unreliable even if prediction performance remains stable.