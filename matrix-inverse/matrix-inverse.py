import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.asarray(A)

    if A.shape[0] != A.shape[1]: return None
    n = A.shape[0]

    I = np.eye(n, dtype=float)
    augmented = np.concatenate((A, I), axis=1)
    
    for k in range(n):
        pivot_row = k + np.argmax(np.abs(A[k: , k]))

        if np.isclose(augmented[pivot_row, k], 0): return None

        if pivot_row != k:
            augmented[[pivot_row, k]] = augmented[[k, pivot_row]]

        pivol_val = augmented[k, k]
        augmented[k] /= pivol_val

        for i in range(n):
            if i != k:
                factor = augmented[i, k]
                augmented[i] -= factor * augmented[k]


    return augmented[:, n:]
            