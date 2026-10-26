import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    return x * (1 + np.vectorize(math.erf)(x / np.sqrt(2))) / 2