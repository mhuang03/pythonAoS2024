# Problem 4: Quadratic Equation
# Design a function that accepts three numbers, a, b, and c, representing the coefficients of a
# quadratic equation of the form ax^2 + bx + c = 0, and returns the roots of the equation.
# The function should return a list containing all the real roots of the equation, or an empty list
# if there are no real roots or if the equation is not quadratic (if a=0).
# Hint: The square root of a number x can be calculated as x**0.5.

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0 or a == 0:
        return []

    if discriminant == 0:
        return [-b / (2*a)]

    return [(-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a)]


print(quadratic_roots(1, 2, 1))
print(quadratic_roots(1, 2, 3))
