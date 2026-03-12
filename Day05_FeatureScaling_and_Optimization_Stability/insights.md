# Key Insights — Day 5 (Feature Scaling & Optimization)

## 1. Feature Magnitude Matters for Optimization

In the dataset used for this experiment, the feature **size_sqft** had values in the thousands, while **rooms** had values between 1 and 6.

Because gradient descent updates depend on feature values, large-scale features produce much larger gradients.

As a result, optimization becomes imbalanced when features have very different scales.

---

## 2. Behavior Without Feature Scaling

When the regression model was trained without scaling:

* gradient updates were dominated by the larger feature (size_sqft)
* optimization followed an inefficient zig-zag path
* convergence became slower

This happens because the loss surface becomes **elongated**, making it harder for gradient descent to reach the minimum efficiently.

---

## 3. Effect of Standardization

Standardization transforms each feature using:

x' = (x − μ) / σ

This ensures that all features have:

* mean = 0
* standard deviation = 1

After applying scaling, feature magnitudes become comparable, which balances gradient updates.

---

## 4. Convergence Experiment

The gradient descent experiment compared loss curves for:

* raw features
* scaled features

The results showed that:

* the scaled model converged significantly faster
* optimization became more stable
* the loss decreased more smoothly

This confirms that feature scaling improves the numerical behavior of gradient-based optimization algorithms.

---

## 5. Important Observation About Coefficients

After scaling, the regression coefficients appeared larger.
This is expected because scaling changes the **units of the features**.

The model adjusts the coefficients accordingly so that predictions remain consistent.

Therefore, coefficients from scaled and unscaled models should not be compared directly.

---

## 6. Practical Takeaway

Feature scaling does not change the underlying relationships in the data.
Instead, it improves the efficiency and stability of optimization algorithms.

For this reason, scaling is a critical preprocessing step for many machine learning models.

Models that benefit from scaling include:

* Linear Regression (with gradient descent)
* Logistic Regression
* Support Vector Machines
* K-Nearest Neighbors
* Neural Networks

Tree-based models such as Decision Trees and Random Forests generally do not require feature scaling.
