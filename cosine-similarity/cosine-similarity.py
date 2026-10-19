import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    den = np.linalg.norm(a) * np.linalg.norm(b)

    if int(den) == 0:
        return float(0)
    
    return float((a @ b) / den)