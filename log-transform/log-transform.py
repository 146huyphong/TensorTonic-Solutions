import math

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    # Write code here
    return list(map(lambda x: math.log(x + 1), values))