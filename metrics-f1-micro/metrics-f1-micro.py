def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    TP = sum(a == b for a, b in zip(y_pred, y_true))
    FP = FN = sum(a != b for a, b in zip(y_pred, y_true))
 
    return TP / (TP + FP)