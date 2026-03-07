# Key Insights —

## 1. Gradient Descent Convergence

The loss curve shows a sharp decrease in Mean Squared Error during the first few hundred iterations, followed by a plateau as the model converges.

This indicates that gradient descent quickly moves toward the optimal region of the loss surface and then gradually stabilizes as parameter updates become very small.

Observation from the loss curve:

* Rapid loss reduction during early iterations
* Stable flattening of the curve afterward
* Indicates successful convergence of the optimization process

---

## 2. Impact of Increasing Epochs

Initially, the model was trained with a smaller number of epochs, which resulted in a higher MSE compared to the sklearn implementation.

After increasing the training iterations to:

```
epochs = 10000
```

the gradient descent algorithm had sufficient time to fully converge.

Result:

```
Scratch Implementation MSE ≈ Sklearn MSE
```

This confirms that the optimization process successfully reached the global minimum of the Mean Squared Error loss function.

---

## 3. Comparison with Scikit-Learn Implementation

The sklearn LinearRegression model computes the optimal parameters using linear algebra methods (closed-form solution), while this implementation uses iterative optimization through gradient descent.

After sufficient training iterations, both approaches converge to nearly identical solutions, validating the correctness of the custom implementation.

---

## 4. Learning Behavior Observed

The experiment highlights several important optimization behaviors:

* Gradient descent converges quickly during early iterations.
* Parameter updates become progressively smaller as the model approaches the minimum.
* Increasing training iterations improves convergence accuracy.
* Proper feature scaling stabilizes the optimization process.

---

## 5. Engineering Takeaway

Implementing linear regression from scratch provides deeper insight into:

* how gradient descent updates parameters
* how loss functions guide optimization
* how convergence occurs during training
* how iterative optimization compares with analytical solutions

These concepts form the foundation for training more complex machine learning models such as logistic regression and neural networks.

---

## Conclusion

This experiment demonstrates that a properly implemented gradient descent algorithm can achieve performance comparable to production machine learning libraries when given sufficient training iterations and properly scaled features.
