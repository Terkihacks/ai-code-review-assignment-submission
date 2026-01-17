# Corrected implementation
from typing import List, Dict, Any
from statistics import mean

def calculate_average_order_value(orders: List[Dict[str, Any]]) -> float:
    """
    Calculate average order value excluding cancelled orders.
    
    Args:
        orders: List of order dicts with 'status' (str) and 'amount' (numeric) keys
        
    Returns:
        Average amount of non-cancelled orders (0.0 if none found)
        
    Raises:
        ValueError: If orders isn't a list or contains invalid structure
    """
    if not isinstance(orders, list):
        raise ValueError("orders must be a list")
    
    if not orders:
        return 0.0
    
    valid_amounts = []
    for order in orders:
        if not isinstance(order, dict):
            continue  # Skip invalid orders gracefully
            
        status = order.get("status")
        amount = order.get("amount")
        
        if (status == "cancelled" or 
            not isinstance(amount, (int, float))):
            continue
            
        valid_amounts.append(float(amount))
    
    return mean(valid_amounts) if valid_amounts else 0.0
