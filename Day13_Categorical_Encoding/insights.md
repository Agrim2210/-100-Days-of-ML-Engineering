# Insights — Categorical Encoding

Label Encoding can introduce unintended ordinal relationships
between categories, which can mislead certain models.

One Hot Encoding avoids this issue by representing categories
independently.

The choice of encoding method significantly affects model
performance, especially for linear models.

Tree-based models are less sensitive to encoding methods,
while distance-based and linear models require careful encoding.