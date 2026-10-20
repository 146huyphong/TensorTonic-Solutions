import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    X_centered = X - np.mean(X, axis=0)
    std = np.std(X_centered, axis=0, keepdims=True)

    with np.errstate(divide='ignore', invalid='ignore'):
        X_normalized = X_centered / std
        corr = X_normalized.T @ X_normalized / X.shape[0]

    return corr