import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    mean = sum(x) / n

    var = sum([(xi - mean) ** 2 for xi in x]) / (n - 1)
    return {
        "variance": var,
        "standard_deviation": float(np.sqrt(var))
    }