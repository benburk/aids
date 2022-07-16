from itertools import combinations
from operator import itemgetter


def dist(point1, point2) -> float:
    """squared euclidean distance"""
    return ((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2) ** 0.5


def bruteforce(points: list[tuple]) -> float:
    """brute force O(n^2)"""
    return min(dist(i, j) for i, j in combinations(points, 2))


def closest_pair(points: list) -> float:
    """find the closest pair of points

    Time: O(nlog^2n)

    Can be made O(nlogn) by not sorting points in strip from scratch each time.
    Each recursive returns two lists: all points sorted by y coordinate,
    and all points sorted by x coordinate.
    Sort by merging two pre-sorted lists.
    """
    # base case
    if len(points) <= 3:
        return bruteforce(points)

    # compute separation line, dividing points in half
    mid = len(points) // 2

    # recurse on left half and right half
    left = closest_pair(points[mid:])
    right = closest_pair(points[:mid])
    min_dist = min(left, right)

    # Delete points further than `min_dist` from separation line
    points = [x for x in points if abs(x[0] - points[mid][0]) < min_dist]
    # sort remaining points by y coordinate
    points.sort(key=itemgetter(1))

    # Scan points in y-order and compare min_dist between each point and next 6
    # neighbors. Update min_dist if smaller found
    # https://www.cs.mcgill.ca/~cs251/ClosestPair/proofbox.html
    for i, point in enumerate(points):
        for neighbour in points[i + 1 : i + 7]:
            if (distance := dist(point, neighbour)) < min_dist:
                min_dist = distance
    return min_dist


def test():
    """run test cases"""
    points = [(2, 3), (12, 30)]
    points = [(0, 0), (1, 1)]
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

    print(closest_pair(points))


if __name__ == "__main__":
    test()
