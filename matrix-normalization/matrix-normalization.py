import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    X = np.asarray(matrix, dtype=float)
    
    if (norm_type == 'l1'):
        X_norm = np.sum(np.abs(X), axis=axis, keepdims=True)
    elif (norm_type == 'l2'):
        X_norm = np.sqrt(np.sum(X ** 2, axis=axis, keepdims=True))
    elif (norm_type == 'max'):
        X_norm = np.max(np.abs(X), axis=axis, keepdims=True)

    X_norm = np.where(X_norm == 0, 1.0, X_norm)
    
    return matrix / X_norm