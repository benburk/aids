"""
Implementation of Bresenham's line drawing algorithm
See https://en.wikipedia.org/wiki/Bresenham's_line_algorithm
"""


from typing import Iterator


def bresenham(x0: int, y0: int, x1: int, y1: int) -> Iterator[tuple[int, int]]:
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    err = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if err >= 0:
            y += 1
            err -= 2 * dx
        err += 2 * dy


"""

def get_octant(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    octant = 0
    if dy < 0:
        dx, dy = -dx, -dy  # rotate by 180 degrees
        octant += 4
    if dx < 0:
        dx, dy = dy, -dx  # rotate clockwise by 90 degrees
        octant += 2
    if dx < dy:
        # no need to rotate now
        octant += 1
    return octant


def to_zero(octant, x, y):
    if octant == 0:
        return (x, y)
    if octant == 1:
        return (y, x)
    if octant == 2:
        return (y, -x)
    if octant == 3:
        return (-x, y)
    if octant == 4:
        return (-x, -y)
    if octant == 5:
        return (-y, -x)
    if octant == 6:
        return (-y, x)
    if octant == 7:
        return (x, -y)


def from_zero(octant, x, y):
    if octant == 0:
        return (x, y)
    if octant == 1:
        return (y, x)
    if octant == 2:
        return (-y, x)
    if octant == 3:
        return (-x, y)
    if octant == 4:
        return (-x, -y)
    if octant == 5:
        return (-y, -x)
    if octant == 6:
        return (y, -x)
    if octant == 7:
        return (x, -y)


def plot_line(x0, y0, x1, y1):
    octant = get_octant(x0, y0, x1, y1)
    print("octant {}".format(octant))
    x0, y0 = to_zero(octant, x0, y0)
    x1, y1 = to_zero(octant, x1, y1)

    dx = x1 - x0
    dy = y1 - y0
    err = 2 * dy - dx
    y = y0

    for x in range(x0, x1 + 1):
        plot(octant, x, y)
        if err > 0:
            y += 1
            err += -2 * dx
        err += 2 * dy


def plot_line2(x0, y0, x1, y1):
    octant = get_octant(x0, y0, x1, y1)
    x0, y0 = to_zero(octant, x0, y0)
    x1, y1 = to_zero(octant, x1, y1)

    dx = x1 - x0
    dy = y1 - y0
    err = 2 * dy - dx

    print("octant {}, dx {}, dy {}, err {}".format(octant, dx, dy, err))
    print("({}, {}) to ({}, {})".format(x0, y0, x1, y1))

    for _ in range(dx + 1):
        plot(octant, x0, y0)
        x0 += 1
        if err > 0:
            y0 += 1
            err += 2 * dy - 2 * dx
        else:
            err += 2 * dy


def plot(octant, x, y):
    x, y = from_zero(octant, x, y)
    print("{}, {}".format(x, y))


# plot_line(4, 9, 0, 2)
print("\n")
plot_line2(2, 1, 9, 5)


# print([([1, 2], [8, 7]), ([4, 3], [5, 6])][dx < 0][dy < 0][abs(dx) < abs(dy)] - 1)

"""
