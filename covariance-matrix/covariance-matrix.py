import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    X_c = X - X.mean(axis=0)
    return X_c.T @ X_c / (len(X) - 1)