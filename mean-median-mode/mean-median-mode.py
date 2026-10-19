from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    n = len(x)
    mean_num = float(sum(x) / n)

    x.sort()
    
    median_num = float(x[n >> 1] if n & 1 else (x[n >> 1] + x[(n >> 1) - 1]) / 2)
    
    counts = Counter(x)
    mode_num = float(max(counts.items(), key=lambda item: item[1])[0])
    
    return {
        "mean": mean_num,
        "median": median_num,
        "mode": mode_num,
    }

# def mean_median_mode(x: list) -> dict:
#     """
#     Returns a dictionary with mean, median, and mode.
#     """
#     # Write code here
#     counts = Counter(x)
#     mean_num = float(np.mean(x))
#     median_num = float(np.median(x))
#     mode_num = float(max(counts.items(), key=lambda item: item[1])[0])
    
#     return {
#         "mean": mean_num,
#         "median": median_num,
#         "mode": mode_num,
#     }