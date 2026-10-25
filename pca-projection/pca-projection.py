import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    n = X.shape[0]
    X_centered = X - X.mean(axis=0, keepdims=True)
    
    Cov = X_centered.T @ X_centered / (n - 1) 
    engenvalues, engenvectors = np.linalg.eigh(Cov)

    top_indices = np.argsort(engenvalues)[::-1][:k]
    top_engenvectors = engenvectors[:, top_indices]

    X_proj = X_centered @ top_engenvectors
    
    return X_proj.tolist()