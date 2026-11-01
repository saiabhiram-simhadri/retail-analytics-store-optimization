"""Export the integrated notebook's charts, including on subsequent executions."""
from pathlib import Path
import json
import base64

CHART_NAMES = (
    '01_sales_distribution', '02_store_size', '03_store_type_shares',
    '04_markdown_distribution', '05_temperature', '06_sales_by_type',
    '07_holiday_sales', '08_fuel_and_sales', '09_markdown1_sales',
    '10_unemployment_sales', '11_correlation_heatmap', '12_sales_trends_by_type',
    '13_store_pca', '14_department_correlation', '15_target_correlations',
    '16_cluster_diagnostics', '17_store_segments', '18_association_rules',
    '19_forecast_residuals', '20_feature_importance',
)


def enable_chart_exports():
    """Save existing outputs and enable 200-DPI exports for the next ordered run.

    Execute the notebook's export appendix once before rerunning the analysis.
    Repeated setup resets the sequence without wrapping show more than once.
    """
    import matplotlib.pyplot as plt

    root = Path.cwd()
    notebook = root / 'Integrated_Retail_Analytics_Store_Optimization.ipynb'
    if not notebook.exists():
        raise FileNotFoundError('Run from the repository root containing the integrated notebook.')
    destination = root / 'outputs' / 'figures'
    destination.mkdir(parents=True, exist_ok=True)
    document = json.loads(notebook.read_text(encoding='utf-8'))
    images = [
        output['data']['image/png']
        for cell in document['cells']
        for output in cell.get('outputs', [])
        if 'image/png' in output.get('data', {})
    ]
    if len(images) != len(CHART_NAMES):
        raise ValueError(f'Expected {len(CHART_NAMES)} charts, found {len(images)}. Save the completed notebook first.')
    for name, encoded in zip(CHART_NAMES, images):
        destination.joinpath(name + '.png').write_bytes(base64.b64decode(''.join(encoded)))

    original_show = getattr(plt.show, '_retail_original_show', plt.show)
    sequence = iter(CHART_NAMES)

    def show_and_save(*args, **kwargs):
        figures = [plt.figure(number) for number in plt.get_fignums()]
        for figure in figures:
            name = next(sequence, None)
            if name is None:
                raise RuntimeError('Rerun the chart-export appendix to reset the export sequence.')
            figure.savefig(destination / (name + '.png'), dpi=200,
                           bbox_inches='tight', facecolor=figure.get_facecolor())
        result = original_show(*args, **kwargs)
        for figure in figures:
            plt.close(figure)
        return result

    show_and_save._retail_original_show = original_show
    plt.show = show_and_save
    print(f'Exported {len(images)} saved charts to {destination}.')
    print('Live exports enabled: run analysis chart cells in order, or rerun the analysis from the top.')

