def average_pooling_2d(X: list, pool_size: int) -> list:
    """
    Returns non-overlapping average-pooled windows.
    """
    # Write code here
    H, W = len(X), len(X[0])
    h = H // pool_size
    w = W // pool_size

    return [
        [
            sum(
                val
                for row in X[i * pool_size : (i + 1) * pool_size]
                for val in row[j * pool_size : (j + 1) * pool_size] 
            ) / (pool_size ** 2)
            for j in range(w)
        ]
        for i in range(h)
    ]