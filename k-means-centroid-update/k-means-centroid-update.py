def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    new_c = []
    
    for i in range(k):
        points_in_centroid = [point for point, assignment in zip(points, assignments) if assignment == i]

        deno = len(points_in_centroid)

        if deno == 0:
            centroid = [0 for _ in range(len(points[0]))]
        else:
            centroid = [sum(a) / deno for a in zip(*points_in_centroid)]
                 
        new_c.append(centroid)

    return new_c