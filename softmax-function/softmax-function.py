import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x)
    max_nums = np.max(x, axis=-1, keepdims=True)
    exps =  np.exp(x - max_nums) 
    return exps / exps.sum(axis=-1, keepdims=True)