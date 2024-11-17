# differential_privacy.py
import numpy as np

def apply_differential_privacy(query_result, sensitivity, epsilon):
    """Inject noise into query results to maintain privacy."""
    noise = np.random.laplace(0, sensitivity / epsilon)
    noised_result = query_result + noise
    print("Differential privacy applied.")
    return noised_result
