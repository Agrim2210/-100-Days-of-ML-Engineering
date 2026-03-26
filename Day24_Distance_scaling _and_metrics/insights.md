# Insights — Distance & Scaling

## Observations

1. Without scaling:
   - Salary dominates distance
   - Model gives biased predictions

2. With scaling:
   - Balanced feature contribution
   - Better accuracy

3. Manhattan vs Euclidean:
   - Manhattan works better with outliers
   - Euclidean works well for smooth distributions

---

## Key Learning

Distance is NOT absolute.
It depends on:

- Scale
- Metric choice
- Data distribution

---

## Golden Rule

ALWAYS scale data before using:
- KNN
- SVM
- K-Means
- PCA