import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y)
    num_classes = num_classes if num_classes else np.max(y) + 1
    one_hot_vector = np.zeros((y.size, num_classes), dtype=float)
    one_hot_vector[np.arange(y.size), y] = 1.0
    return one_hot_vector