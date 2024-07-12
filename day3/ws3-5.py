# Problem 5: Collinear Points
# Design a function that accepts a list of n tuples, each representing the coordinates
# of a point in 2D space, and returns True if all the points are collinear, and False otherwise.
# Two or more points are collinear if they all lie on the same straight line.
# Hint: Use the slope formula to calculate the slope of the line between points.


def slope(a, b):
    if a[0] == b[0]:
        return None
    return (b[1] - a[1]) / (b[0] - a[0])


def is_collinear(points):
    if len(points) <= 2:
        return True

    first = points[0]
    s = slope(first, points[1])

    for point in points[2:]:
        if slope(first, point) != s:
            return False
    return True


print(is_collinear([(1, 1), (2, 2), (3, 3)])) # True
print(is_collinear([(1, 1), (2, 2), (3, 4)])) # False
print(is_collinear([(1, 1), (2, 1), (3, 1)])) # True
print(is_collinear([(1, 1), (1, 2), (1, 3)])) # True
