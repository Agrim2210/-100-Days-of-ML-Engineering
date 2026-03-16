# Mathematical Foundations — Cross Validation

## K-Fold Cross Validation

The dataset is divided into K equal parts (folds).

The model is trained K times, each time using
K-1 folds for training and 1 fold for validation.

Final performance is computed as:

Mean Score = (1/K) * Σ(score_i)

where score_i is the evaluation score of fold i.

---

## Stratified K-Fold

Stratified K-Fold maintains the class distribution
in every fold.

This is especially important in classification tasks
with imbalanced datasets.

Maintaining consistent class proportions ensures
that each fold represents the dataset properly.