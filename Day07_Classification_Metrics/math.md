# Mathematical Foundations — Classification Metrics

## Confusion Matrix

A confusion matrix summarizes classification predictions.

                Predicted Positive   Predicted Negative

Actual Positive       TP                  FN
Actual Negative       FP                  TN

TP = True Positive  
FP = False Positive  
FN = False Negative  
TN = True Negative

---

## Accuracy

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Accuracy measures the proportion of correct predictions.

However, accuracy can be misleading when datasets are imbalanced.

---

## Precision

Precision = TP / (TP + FP)

Precision measures how many predicted positives were actually correct.

This metric is important when false positives are costly.

---

## Recall

Recall = TP / (TP + FN)

Recall measures how many actual positives were correctly detected.

This metric is important when missing positive cases is dangerous.

---

## F1 Score

F1 = 2 * (Precision * Recall) / (Precision + Recall)

F1 Score balances precision and recall and is useful when
the dataset is imbalanced.