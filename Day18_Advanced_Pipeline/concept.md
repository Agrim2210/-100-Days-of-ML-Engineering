# Conceptual Foundations — Advanced Pipelines

Pipelines allow chaining multiple transformations and models into a single workflow.

Nested pipelines enable handling of complex preprocessing tasks,
including missing value imputation and feature transformations.

ColumnTransformer applies different pipelines to different feature subsets.

This structure ensures consistent and leak-free transformations across training and testing data.