def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    # Write code here
    return list(map(lambda x: [x ** i for i in range(degree + 1)], values))