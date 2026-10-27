import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A = np.asarray(A)
    n = A.shape[0]
    
    return np.sum(A[np.arange(n), np.arange(n)])