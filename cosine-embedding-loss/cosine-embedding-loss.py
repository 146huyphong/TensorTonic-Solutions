import math

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    def norm(x):
        return  math.sqrt(sum(x_i ** 2 for x_i in x))

    norm1 = norm(x1)
    norm2 = norm(x2)

    if norm1 == 0 or norm2 == 0:
        cosine = 0.0
    else:
        cosine = sum([x_i * x_j for x_i, x_j in zip(x1, x2)]) / (norm1 * norm2)
    
    return float(1 - cosine) if label == 1 else float(max(0, cosine - margin))