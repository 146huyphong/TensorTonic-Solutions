import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    LAMBDA = 1.0507
    ALPHA = 1.6733
    return [LAMBDA * x_i if x_i > 0 else LAMBDA * ALPHA * (math.exp(x_i) - 1) for x_i in x]