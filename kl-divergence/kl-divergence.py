import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p = np.asarray(p)
    q = np.asarray(q)
    ratio = p / q
    ratio = np.where(np.isclose(ratio, 0.0), eps, ratio)
    
    return float(np.sum(p * np.log(ratio)))