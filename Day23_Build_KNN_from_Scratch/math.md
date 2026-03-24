# KNN Mathematics

## Distance Metric

### Euclidean Distance
d(x, y) = sqrt(sum((xi - yi)^2))

### Manhattan Distance
d(x, y) = sum(|xi - yi|)

---

## Algorithm Steps

1. Choose K
2. Compute distance of test point to all training points
3. Sort distances
4. Select K nearest
5. Majority voting

---

## Complexity

Training: O(1)  
Prediction: O(N log N)

---

## Key Observations

- Sensitive to scale
- No model training
- Works well for small datasets