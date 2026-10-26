# Integrated Retail Analytics for Store Optimization and Demand Forecasting

Analysis of weekly store-department sales, covering data quality, store segmentation, department co-movement and sales forecasting.

**Repository:** https://github.com/saiabhiram-simhadri/integrated-retail-analytics-store-optimization

## Start here

- [Completed, executed notebook](Retail%20Analytics%20Submission.ipynb): data checks, 10 exploratory charts and 5 analysis/evaluation charts, three hypothesis tests, anomaly detection, store segmentation, department association proxy, forecasting, evaluation and conclusions.
- [Detailed report](docs/project_report.md): methodology, measured findings, charts and recommendations.
- [Project brief](project_overview.md) and [original template](Sample%20ML%20Submission%20Template.ipynb): supplied reference materials.

## Files

| Location | Contents |
|---|---|
| `data/` | Supplied `sales.csv`, `Features.csv`, `stores.csv` |
| `outputs/figures/` | Saved exploratory, anomaly, segmentation and forecasting charts |
| `models/` | Forecast pipeline, IQR anomaly bounds and store segmentation artifacts |
| `requirements.txt` | Package versions used by the notebook |

## Reproduce

Use Python 3.12 and install `requirements.txt` in your environment. Open **Retail Analytics Submission.ipynb** with the repository root as the working directory and run all cells in order. The notebook displays result tables and regenerates charts and model artifacts. Charts use a consistent seaborn style and save as 200-DPI PNGs with the custom dark background and tight margins. Random seed: 47. Model fitting may take several minutes depending on the computer.

The main forecast uses two expanding 8-week validation blocks and a final 8-week test. Selection uses validation MAE only. A historical store-department mean is the baseline; decision trees and random forests receive a small depth comparison. A separate 26-week seasonal baseline illustrates longer planning horizons. Full-period EDA is descriptive; fitted thresholds and preprocessing use past data.

## Interpretation

The verified run selected historical store-department means: validation MAE **2,665.83** and final-test MAE **2,266.30**. The tested tree models did not beat this baseline. The separate 26-week seasonal experiment reduced MAE from **3,384.78** to **2,063.45** on its own earlier block; scores across different periods are not directly comparable. Store segmentation selected **2 clusters**, with silhouette **0.345**. The completed notebook has **24 code cells**, no recorded errors and **15 saved charts**.

Sales are monetary values, not demand units. No customer identities or baskets exist: segmentation groups **stores**, and association rules represent **department high-sales co-movement**. Historical external-factor forecasts assume those inputs are available; operations need planned promotions and forecasts/scenarios for unknown indicators. Correlation, cluster labels and proxy lift do not establish causal effects or profit improvements.
