import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    return {
        "pmf": np.asarray(list(map(lambda s: p if s else 1 - p, x))), 
        "mean": float(p), 
        "variance": float(p * (1 - p))
    }