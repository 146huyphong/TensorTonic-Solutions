import numpy as np

def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """
    # Write code here
    y = np.asarray(y)
    split_mask = np.asarray(split_mask)

    y_left = y[split_mask]
    y_right = y[~split_mask]
    
    N_l = len(y_left)
    N_r = len(y_right)
    N = N_l + N_r

    if N == 0: return 0.0
    
    def H(s):
        if len(s) == 0: return 0.0

        counts = np.unique(s, return_counts=True)[1]
        p = counts / len(s)
        return float( -np.sum(p * np.log2(p)) )

    return float(H(y) - N_l * H(y_left) / N - N_r * H(y_right) / N)