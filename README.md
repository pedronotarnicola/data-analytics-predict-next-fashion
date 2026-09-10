# Fashion Trend Forecasting

## Business problem
Fashion product lines can take a year or more from design to market. Anticipating which clothing trends are rising or falling in popularity helps avoid financial losses from producing items that will be out of trend by launch.

## Dataset
- **Source**: Le Wagon Data Analytics Bootcamp (real-world weekly social-media popularity index by clothing type, 2015-2019)
- **Format**: weekly time series, one column per clothing category (e.g., lace-up shoes, denim pants, spaghetti straps, tank tops)

## Approach
Time series forecasting on one clothing category (`top_tanksleeve_tshirtneck`), comparing two models:
1. **Naive Forecaster (baseline)**: assumes next year repeats last year exactly (seasonal naive)
2. **Holt-Winters Exponential Smoothing**: models trend (multiplicative) + seasonality (additive) explicitly

Data was split with the last 52 weeks held out as a test set. Seasonal decomposition was used first to confirm a clear yearly (52-week) cycle before modeling.

## Tools used
`Python` `pandas` `sktime` `statsmodels` `plotly`

## Key findings
| Model | MAE | MASE | SMAPE |
|---|---|---|---|
| Naive (baseline) | 0.00046 | 1.03 | 49.8% |
| Holt-Winters | 0.00030 | 0.68 | 39.0% |

Holt-Winters improved on the naive baseline by **33%** (MASE 1.03 → 0.68). Fashion popularity for this category shows a clear multiplicative downward trend combined with a strong yearly seasonal pattern (peaks in summer).

## Business recommendation
For categories with a clear, stable seasonal pattern, a Holt-Winters-style model gives a meaningfully better forecast than assuming "next year = last year" — worth building into planning cycles for design lead times. Categories should first be checked for a stable seasonal pattern (via decomposition) before trusting this approach; less seasonal categories would need a different model.

## Limitations
- Only one clothing category was modeled in depth here; the other categories in the dataset would need the same process repeated (and may respond differently).
- Only two models were compared — more advanced approaches (e.g., SARIMA, Prophet) could be benchmarked against Holt-Winters.
- The metric SMAPE is inflated here because the series values are very close to zero; MASE is the more reliable metric for this dataset.

## How to run this project
```bash
git clone https://github.com/pedronotarnicola/data-analytics-predict-next-fashion.git
cd data-analytics-predict-next-fashion
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```
Data loads directly from a URL inside the notebook — no manual download needed.

## Folder structure
```
data-analytics-predict-next-fashion/
├── notebooks/
│   └── analysis.ipynb
├── README.md
└── requirements.txt
```

---
[Portfolio](https://pedronotarnicola.github.io/) · [LinkedIn](https://www.linkedin.com/in/p-l-notarnicola/)
