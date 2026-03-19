# Insights — Pipelines

Manual preprocessing can lead to data leakage if applied before train-test splitting.

Pipelines enforce correct order of operations and ensure that transformations are learned only from training data.

ColumnTransformer enables flexible preprocessing for different feature types within the same dataset.

Using pipelines leads to cleaner, more reliable, and production-ready machine learning workflows.