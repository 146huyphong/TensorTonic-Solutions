import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    p_hat = [min(1 - eps, max(eps, a)) for a in y_pred]
    return [-(a * math.log(b) + (1 - a) * math.log(1 - b)) for a, b in zip(y_true, p_hat)]
    