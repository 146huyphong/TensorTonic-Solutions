from collections import defaultdict

def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    map_target = defaultdict(lambda: [0.0, 0])
    
    for category, target in zip(categories, targets):
        map_target[category][0] += target
        map_target[category][1] += 1

    means = {category:  total / count for category, (total, count) in map_target.items()}

    return [means[category] for category in categories]