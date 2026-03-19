# Conceptual Foundations — Pipelines

A Pipeline chains multiple steps into a single workflow.

Each step consists of:

• fit() — learn from training data  
• transform() — apply transformation  

---

# ColumnTransformer

ColumnTransformer applies different transformations
to different subsets of features.

This allows proper handling of mixed data types such as
numerical and categorical variables.

---

# Key Idea

Pipelines ensure that preprocessing steps are applied
consistently and correctly during both training and testing,
preventing data leakage.