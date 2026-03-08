# Key Insights — Day 2 (Logistic Regression From Scratch)

## 1. Initial Loss Behavior

The training loss started around **0.69**, which is expected for logistic regression when model parameters are initialized to zero.

At initialization:

```
w = 0
b = 0
```

The sigmoid function outputs:

```
sigmoid(0) = 0.5
```

This means the model initially predicts a **50% probability for all samples**, which corresponds to a log-loss of approximately **0.693**. This represents the baseline performance before learning begins.

---

## 2. Rapid Early Convergence

During the early iterations of training, the loss decreases rapidly.

This indicates that:

* Gradient descent is correctly adjusting model parameters.
* The dataset contains meaningful signal that allows the model to separate the two classes.
* The learning rate is appropriate and allows efficient progress toward the optimal solution.

This phase represents the model quickly moving toward the optimal region of the loss surface.

---

## 3. Gradual Stabilization

After several thousand iterations, the loss curve begins to flatten.

This behavior indicates that:

```
gradients ≈ 0
```

which means parameter updates become very small and the model approaches convergence.

At this stage, additional iterations produce only minor improvements in the loss value.

---

## 4. Final Convergence

After training for **10,000 epochs**, the loss stabilized around approximately:

```
~0.06 – 0.07
```

A low cross-entropy loss indicates that the model is producing **confident and accurate probability estimates** for the classification task.

This confirms that the gradient descent optimization successfully minimized the binary cross-entropy objective.

---

## 5. Numerical Stability Considerations

During implementation, a small constant (`1e-9`) was added inside the logarithm during loss calculation:

```
log(p + 1e-9)
log(1 - p + 1e-9)
```

This prevents numerical issues such as:

```
log(0) → -∞
```

which would otherwise cause instability during training.

This technique is commonly used in practical machine learning implementations to ensure stable computations.

---

## 6. Engineering Takeaways

Implementing logistic regression from scratch provides deeper understanding of:

* probabilistic classification models
* sigmoid activation behavior
* binary cross-entropy optimization
* gradient descent convergence dynamics
* numerical stability in machine learning algorithms

These concepts form the foundation for training more advanced models such as neural networks and deep learning architectures.

---

## Conclusion

This experiment demonstrates that logistic regression can be effectively implemented using gradient descent and basic numerical operations.

The observed training behavior — starting from baseline loss, rapidly improving, and eventually converging — validates both the mathematical formulation and the correctness of the implementation.
