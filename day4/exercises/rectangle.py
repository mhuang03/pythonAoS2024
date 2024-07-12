class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def print(self):
        # print(("*  " * self.width + "\n") * self.length)
        for i in range(self.length):
            for j in range(self.width):
                print("*", end="  ")
            print()


r1 = Rectangle(5, 6)
print(r1.length, r1.width)
print(r1.area())

r1.print()

r2 = Rectangle(10, 15)
print(r2.perimeter())
r2.print()