# Distance Metrics & Scaling

## Euclidean Distance
sqrt(sum((xi - yi)^2))

## Manhattan Distance
sum(|xi - yi|)

## Minkowski Distance
(sum(|xi - yi|^p))^(1/p)

---

## Feature Scaling

### Standardization
x' = (x - mean) / std

### Min-Max Scaling
x' = (x - min) / (max - min)

---

## Key Insight

Distance-based models are highly sensitive to scale.

Without scaling:
- Large-value features dominate

With scaling:
- Fair contribution from all features