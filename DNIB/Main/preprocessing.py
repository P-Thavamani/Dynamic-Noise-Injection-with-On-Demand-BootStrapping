# preprocessing.py
def preprocess_data(data):
    """Clean and format the combined data."""
    # Example preprocessing: Remove duplicates and reset index
    data = data.drop_duplicates().dropna().reset_index(drop=True)
    print("Data preprocessing complete.")
    return data
