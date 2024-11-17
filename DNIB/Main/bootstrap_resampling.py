# bootstrap_resampling.py
import pandas as pd

def bootstrap_resample(data, n_samples):
    """Generate synthetic data using bootstrap resampling."""
    synthetic_data = data.sample(n=n_samples, replace=True)
    print("Synthetic data generated with bootstrap resampling.")
    return synthetic_data
