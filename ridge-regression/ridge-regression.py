import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    return list(np.linalg.inv(X.T @ X + lam * np.identity(X.shape[1])) @ X.T @ y)