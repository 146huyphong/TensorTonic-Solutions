import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    y_true_mean = y_true.mean()

    num = np.sum((y_true - y_pred) ** 2)
    deno = np.sum((y_true - y_true_mean) ** 2)

    if (np.isclose(deno, 0.0)):
        return 1.0 if np.isclose(num, 0.0) else 0.0
    
    return float(1 - num / deno)