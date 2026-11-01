# Model provenance

The current integrated notebook writes `retail_demand_forecaster.joblib` when its serialization cell executes. That artifact is not present at this update. It stores tuned LightGBM and feature metadata; its recorded WMAE is $1,491.80. Random Forest has the lower reported WMAE ($1,471.72).

The existing `sales_forecaster.joblib`, `anomaly_model.joblib` and `store_segmentation.joblib` belong to the superseded analysis. They are retained for provenance and must not be treated as models from the integrated notebook. The integrated notebook does not serialize K-means or Isolation Forest.

See [the current report](../docs/project_report.md) for validation limitations and input requirements.
