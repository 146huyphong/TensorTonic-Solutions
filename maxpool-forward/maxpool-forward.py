def maxpool_forward(X: list, pool_size: int, stride: int) -> list:
    """
    Returns the maximum value from every pooling window.
    """
    # Write code here
    H, W = len(X), len(X[0])
    h = (H - pool_size) // stride + 1
    w = (W - pool_size) // stride + 1

    return [
        [
            # submatrix = [row[c_start:c_end] for row in A[r_start:r_end]]
            max(
                val
                for row in X[i * stride : i * stride + pool_size]
                for val in row[j * stride : j * stride + pool_size]
            ) 
             for j in range(w)
        ]
        for i in range(h)
    ]