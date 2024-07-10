def is_isosceles(points):
    x, y, z = points
    if x == y or y == z or x == z:
        return False

    dists = set()
    dists.add(dist(x, y))
    dists.add(dist(y, z))
    dists.add(dist(x, z))

    if len(dists) < 3:
        return True
    return False


def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


print(is_isosceles(((1, 5), (5, 1), (7, 7))))
print(is_isosceles(((2, 4), (2, 6), (10, 5))))
print(is_isosceles(((1, 1), (2, 1), (3, 2))))