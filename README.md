# Integrated Retail Analytics for Store Optimization and Demand Forecasting

The source of truth is [Integrated_Retail_Analytics_Store_Optimization.ipynb](Integrated_Retail_Analytics_Store_Optimization.ipynb), with 15 exploratory figures, anomaly handling, store segmentation, department association rules, forecasting and illustrative inventory policies.

[Detailed report](docs/project_report.md) | [Chart gallery](outputs/figures/README.md)

## Reported forecast results

| Model | Test WMAE ($) | Test RMSE ($) | Test MAE ($) | Test R² |
|---|---:|---:|---:|---:|
| Ridge | 1,808.42 | 3,271.17 | 1,778.71 | 0.9778 |
| Random Forest | **1,471.72** | 2,988.12 | **1,404.11** | 0.9815 |
| Default LightGBM | 1,484.42 | **2,944.74** | 1,436.34 | **0.9820** |
| Tuned LightGBM | 1,491.80 | 2,967.83 | Not printed | 0.9818 |

These are the supplied notebook's saved-run results. Random Forest leads WMAE; the notebook serializes tuned LightGBM. Tuning did not improve LightGBM test WMAE. Full-period target preprocessing and row-based cross-validation limit these scores; see the report.

## Data and findings

- 421,570 sales rows, 8,190 feature rows, 45 stores and 143 sales weeks.
- 1,285 negative sales records are audited and clipped to zero in the clean target.
- Seasonal residual analysis flags 3,665 rows; Isolation Forest flags 6,324. The modeling target winsorizes 2,280 unexplained surges.
- Three prescribed store personas contain 18, 19 and 8 stores.
- Apriori produces 4,095 frequent itemsets and 503,958 filtered department co-movement rules.
- After lag warm-up: 408,436 rows, split into 325,663 training and 82,773 test rows at 20 April 2012.

## Reproduce and export charts

Use Python 3.12 and install requirements.txt. Start Jupyter from the repository root. The notebook currently loads shared Google Drive CSVs and needs network access; supplied local equivalents are under data/.

Run the **chart-export setup cell near the end of the notebook first**, then run the analysis cells from the top in order. Setup exports the 20 embedded charts immediately and enables live saving before subsequent plt.show() calls. Live exports use 200 DPI, tight margins and the figure's dark background. Rerun setup to reset the sequence before another ordered run. Initial snapshot exports retain their embedded resolution.

Keep [retail_chart_exports.py](retail_chart_exports.py) beside the notebook. Full execution includes Random Forest fitting, 18 LightGBM search fits plus refitting, and a large Apriori rule table.

## Artifacts and interpretation

Current figures are in outputs/figures/. Running the serialization cell generates models/retail_demand_forecaster.joblib; that model file is not included at this update. Existing model files are legacy outputs and do not represent the new analysis. Superseded notebooks and charts have been removed.

Store personas are not customer segments. Department co-movement is not customer basket evidence. Forecasts and inventory buffers are in dollars, not units; a 95% realized service level has not been measured.

**Repository:** https://github.com/saiabhiram-simhadri/integrated-retail-analytics-store-optimization


