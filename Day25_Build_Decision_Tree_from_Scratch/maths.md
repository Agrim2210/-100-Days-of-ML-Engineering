# Decision Tree Mathematics

## Entropy
H = -Σ (p * log2(p))

## Information Gain
IG = H(parent) - weighted avg of child entropy

## Gini Index
G = 1 - Σ (p^2)

---

## Key Idea

Choose split that:
- Maximizes Information Gain OR
- Minimizes Gini

---

## Why Trees Work?

They partition feature space into regions