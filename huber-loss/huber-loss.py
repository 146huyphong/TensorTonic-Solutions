import numpy as np

def huber_loss(y_true: list, y_pred: list, delta: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    e = y_true - y_pred
    
    loss = np.where(np.abs(e) <= delta, e ** 2 / 2, delta * (np.abs(e) - delta / 2))
    return float(np.mean(loss))
