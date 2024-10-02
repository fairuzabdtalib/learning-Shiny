import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, AutoCES, MSTL


def sales_forecast_fn(df, forecast_horizon):
    # Load the data
    data = df
    data.insert(0, 'unique_id', 'Peninsular_Malaysia_Sales_GWh')
    data = data.rename(columns={'Month': 'ds', 'Sales': 'y'})

    # Create a list of models to run
    models = [
        AutoARIMA(season_length=12),
        AutoCES(season_length=12),
        MSTL(season_length=12)
    ]

    sf = StatsForecast(
        df=data,
        models=models,
        freq='MS',  # Monthly start frequency
        n_jobs=-1  # Use all available CPU cores
    )

    # Make forecasts for the next h months
    forecasts = sf.forecast(h=forecast_horizon, df=data, fitted=True)
    fitted_values = sf.forecast_fitted_values()
    
    return forecasts, fitted_values