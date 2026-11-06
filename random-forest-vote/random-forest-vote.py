from collections import Counter

def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    return [
        min(Counter(prediction).keys(), key=lambda item: (-Counter(prediction)[item], item))
        for prediction in zip(*predictions)
    ]