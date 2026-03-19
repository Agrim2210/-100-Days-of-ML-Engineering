##  Results Summary

### ✅ Linear Regression

* Scores: `[0.9889, 0.9254, 0.8666]`
* Mean Score: **0.927**

**Insights:**

* Consistently high performance across all folds
* Low variance → stable model
* Indicates strong **linear relationship** between features (`area`, `rooms`) and target (`price`)

---

### ❌ K-Nearest Neighbors (KNN)

* Scores: `[-0.006, -6.96, -1.77]`
* Mean Score: **-2.91**

**Insights:**

* Negative R² → worse than baseline (mean prediction)
* Highly sensitive to small dataset
* Poor generalization due to insufficient neighbors/data points

---

### ❌ Decision Tree

* Scores: `[0.54, -3.91, -16.0]`
* Mean Score: **-6.45**

**Insights:**

* Very high variance across folds
* Severe overfitting:

  * Performs okay on some folds
  * Fails badly on others
* Model is memorizing training data instead of learning patterns

---

## 🔍 Key Observations

### 1. Dataset Characteristics

* Likely **small dataset**
* Relationship between features and target appears **linear**

---

### 2. Model Behavior

| Model             | Bias | Variance  | Performance |
| ----------------- | ---- | --------- | ----------- |
| Linear Regression | Low  | Low       | ✅ Best      |
| KNN               | Low  | High      | ❌ Poor      |
| Decision Tree     | Low  | Very High | ❌ Worst     |

---

### 3. Why Linear Regression Works Best

* Simple model matches data pattern
* No overfitting
* Stable across folds

---

### 4. Why Others Failed

#### KNN:

* Needs more data to find meaningful neighbors
* Sensitive to noise and small sample size

#### Decision Tree:

* Overfits easily on small datasets
* Learns noise instead of general patterns

---



## 🎯 Final Conclusion

> For this dataset, **simpler models outperform complex ones**.

* Linear Regression is:

  * Stable ✅
  * Accurate ✅
  * Interpretable ✅

* Complex models:

  * Overfit ❌
  * Unstable ❌

---


