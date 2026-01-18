def average_valid_measurements(values):
    """
    Calculate the average of valid (non-None) measurements.
    
    Args:
        values: List of measurement values (numbers or None)
        
    Returns:
        float: Average of valid measurements, or 0 if no valid measurements
        
    Raises:
        ValueError: If values is not a list
        
    Note:
        Values that cannot be converted to float are skipped silently.
        This may hide data quality issues - consider logging in production.
    """
    if not isinstance(values, list):
        raise ValueError("values must be a list")
    
    if not values:
        return 0
    
    total = 0
    valid_count = 0
    
    for v in values:
        # Skip None values
        if v is None:
            continue
        
        try:
            numeric_value = float(v)
            total += numeric_value
            valid_count += 1
        except (TypeError, ValueError):

            continue
    
    # Return 0 if no valid measurements
    if valid_count == 0:
        return 0
    
    return total / valid_count