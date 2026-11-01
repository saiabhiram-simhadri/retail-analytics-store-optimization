# Integrated notebook chart gallery

These 20 PNGs are extracted from the integrated notebook's saved outputs. Initial snapshots retain their embedded resolution. Run the notebook's export setup appendix before an ordered analysis rerun to enable fresh 200-DPI exports. See [the report](../../docs/project_report.md) for interpretation and validation limits. The superseded chart set has been removed.

## Cleaned and log-transformed sales

![Cleaned and log-transformed sales](01_sales_distribution.png)

The left panel uses clipped sales despite its raw-sales title.

## Store physical size by format

![Store physical size by format](02_store_size.png)

Box and individual store observations.

## Outlet and revenue shares by type

![Outlet and revenue shares by type](03_store_type_shares.png)

Cumulative revenue shares reflect store count and size.

## Active markdown distribution

![Active markdown distribution](04_markdown_distribution.png)

Zeros excluded; fliers hidden; department-row weighting.

## Temperature exposure

![Temperature exposure](05_temperature.png)

Store-week context repeats across department rows.

## Mean department sales by format

![Mean department sales by format](06_sales_by_type.png)

Department-row means, not total weekly store sales.

## Holiday versus regular mean sales

![Holiday versus regular mean sales](07_holiday_sales.png)

Descriptive association, not causal uplift.

## Fuel price and chain sales

![Fuel price and chain sales](08_fuel_and_sales.png)

Separate axis scales; timing alone does not imply causality.

## Active MarkDown1 versus sales

![Active MarkDown1 versus sales](09_markdown1_sales.png)

Sample of up to 5,000 positive-event rows.

## Unemployment and sales

![Unemployment and sales](10_unemployment_sales.png)

4,000 sampled rows colored by store format.

## Numeric correlation heatmap

![Numeric correlation heatmap](11_correlation_heatmap.png)

Linear relationships on cleaned sales.

## Time trends by format

![Time trends by format](12_sales_trends_by_type.png)

Mean weekly department sales.

## Four-feature exploratory store PCA

![Four-feature exploratory store PCA](13_store_pca.png)

Separate from the eight-feature segmentation PCA.

## Top-ten department correlations

![Top-ten department correlations](14_department_correlation.png)

Complete co-observed Store-Date rows.

## Signed target correlations

![Signed target correlations](15_target_correlations.png)

Correlation does not establish causal influence.

## K-means diagnostics

![K-means diagnostics](16_cluster_diagnostics.png)

Inertia, silhouette and Davies-Bouldin for k=2–6.

## Three store personas

![Three store personas](17_store_segments.png)

PCA projection and group sizes; k=3 is explicitly specified.

## Department rule space

![Department rule space](18_association_rules.png)

503,958 filtered high-sales co-movement rules; no customer baskets.

## Tuned LightGBM holdout diagnostics

![Tuned LightGBM holdout diagnostics](19_forecast_residuals.png)

Parity sample and adjusted-target residual distribution.

## LightGBM feature split counts

![LightGBM feature split counts](20_feature_importance.png)

Default split importance; the chart axis incorrectly says gain.




