"""Shape Factory

    We are improving our drawing application.
    Our application needs to support adding and comparing two Shape objects.
    Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.

    The addition should return a new object with the sum of the widths and heights of the operands,
    while the comparison should return the result of comparing the areas of the objects.
"""


    class Shape:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def __add__(self, other):
            return Shape(self.width + other.width, self.height + other.height)

        def __gt__(self, other):
            return self.area() > other.area()


width1 = int(input("Enter a width: "))
height1 = int(input("Enter a height: "))
width2 = int(input("Enter another width: "))
height2 = int(input("Enter another height: "))

shape1 = Shape(width1, height1)
shape2 = Shape(width2, height2)

result = shape1 + shape2

print(result.area())
print(shape1 > shape2)
