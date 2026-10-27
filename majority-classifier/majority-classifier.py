import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here
    y_train = np.asarray(y_train)
    values, counts = np.unique(y_train, return_counts=True)
    
    most_frequent_values = values[counts == counts.max()]

    most_frequent_indices = [np.argmax(y_train == val) for val in most_frequent_values]
    majority_class = most_frequent_values[np.argmin(most_frequent_indices)]
    
    return np.full(len(X_test), majority_class)