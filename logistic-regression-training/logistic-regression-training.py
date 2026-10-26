import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    w, b = np.zeros(X.shape[1]), 0.0
    
    for _ in range(steps):
        p = _sigmoid(X @ w + b)
        diff = p - y
        
        dw = (X.T @ diff) / X.shape[0]
        db = diff.mean()
      
        w -= lr * dw
        b -= lr * db

    return w, b