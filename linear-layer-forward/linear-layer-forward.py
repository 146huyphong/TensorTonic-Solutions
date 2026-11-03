def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    return [
        [
            sum(X_ik * W_kj for X_ik, W_kj in zip(row_a, col_b)) + b_j 
            for col_b, b_j in zip(zip(*W), b)
        ]
        for row_a in X
    ]
