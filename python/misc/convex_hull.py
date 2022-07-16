"""
convex hull
"""


def convex_hull(points):
    if len(points) <= 2:
        return points

    def cross(o, a, b):
        """
        2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        Returns a positive value, if OAB makes a counter-clockwise turn,
        negative for clockwise turn, and zero if the points are collinear.
        """
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    points.sort()
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]


def test():
    """run test cases"""
    arr = [(0, 0), (1, 1), (2, 2), (3, 3), (1, 2)]
    print(convex_hull(arr))

    print(convex_hull([(i // 10, i % 10) for i in range(100)]))


if __name__ == "__main__":
    test()
