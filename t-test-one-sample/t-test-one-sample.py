import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    s = np.sqrt(np.sum((x - mean) ** 2) / (x.shape[0] - 1))

    return float((mean - mu0) / (s / np.sqrt(x.shape[0])))