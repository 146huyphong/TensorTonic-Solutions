def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    def get_distance(point1, point2):
        return sum([(a - b) ** 2 for a, b in zip(point1, point2)])
    distances = [[get_distance(point, centroid) for centroid in centroids] for point in points] 
    return [dis.index(min(dis)) for dis in distances]