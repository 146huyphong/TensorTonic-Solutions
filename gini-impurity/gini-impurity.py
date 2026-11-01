import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)
    
    N_l = len(y_left)
    N_r = len(y_right)
    N = N_l + N_r
    if N == 0: return 0.0
        
    def G(s):
        if len(s) == 0:
            return 0.0

        counts = np.unique(s, return_counts=True)[1]
        p = counts / len(s)
        return float(1 - np.sum(p ** 2))
    
    return float((N_l * G(y_left) + N_r * G(y_right)) / N)