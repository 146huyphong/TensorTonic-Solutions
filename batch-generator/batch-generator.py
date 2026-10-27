import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    rng = np.random.default_rng(seed)
    
    X = np.asarray(X)
    y = np.asarray(y)
    n_samples = len(X)
    
    indices = np.arange(n_samples)
    rng.shuffle(indices)

    X_shuffle = X[indices]
    y_shuffle = y[indices]

    for start_idx in range(0, n_samples, batch_size):
        end_idx = start_idx + batch_size
        X_batch = X_shuffle[start_idx:end_idx]
        y_batch = y_shuffle[start_idx:end_idx]

        if drop_last and len(X_batch) < batch_size:
            break

        yield X_batch, y_batch