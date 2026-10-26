import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    return [x_i if x_i >= 0 else alpha * (math.exp(x_i) - 1) for x_i in x]