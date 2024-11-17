# jit_processing.py
def jit_access_control(data, query_condition):
    """Provide controlled access to data based on query conditions."""
    filtered_data = data.query(query_condition)
    print("JIT processing applied.")
    return filtered_data
