# data_storage.py
import os

def save_synthetic_data(data, output_directory):
    """Save synthetic data to the specified directory."""
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "synthetic_data.csv")
    try:
        data.to_csv(output_file, index=False)
        print(f"Synthetic data saved to {output_file}.")
    except Exception as e:
        print(f"Error saving synthetic data: {e}")
