# data_input.py
import pandas as pd
import os

def load_data_from_files(directory_path):
    """Load data from all files in a given directory."""
    dataframes = []
    try:
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if file_name.endswith(".csv"):  # Adjust for the file types you're using
                df = pd.read_csv(file_path)
                dataframes.append(df)
                print(f"Loaded data from {file_name}.")
        combined_data = pd.concat(dataframes, ignore_index=True)
        print("All files loaded successfully.")
        return combined_data
    except Exception as e:
        print(f"Error loading files: {e}")
        return None
