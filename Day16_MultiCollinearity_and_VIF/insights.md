# Insights — Multicollinearity

The correlation heatmap revealed strong relationships between
size_sqft and area_sqft, indicating redundant information.

VIF values confirmed the presence of multicollinearity,
with very high values for correlated features.

The model trained with multicollinearity showed unstable
and less interpretable coefficients.

After removing one of the correlated features, VIF values are still very high,this shows there is also corelation btw other two feature,
so we remove one of that feature,hence  model coeff become stable

This demonstrates that multicollinearity affects model
interpretability more than prediction accuracy.

Proper feature selection is essential for building reliable
and interpretable machine learning models.