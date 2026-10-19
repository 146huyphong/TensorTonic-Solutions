import numpy as np
    
# def dot_product(x: list, y: list) -> float:
#     """
#     Returns the dot product as a float.
#     """
#     result = 0.0
#     for xi, yi in zip(x, y):
#         result += xi * yi
        
#     return result

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    return float(np.array(x) @ np.array(y))