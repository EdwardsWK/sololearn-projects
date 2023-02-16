"""Define The Methods

    The given code takes 2 numbers as input and calls the static area() method of the Shape class,
    to output the area of the shape, which is equal to the height multiplied by the width.

    To make the code work, you need to define the Shape class, and the static
    area() method, which should return the multiplication of its two arguments.
"""


class Shape:
    def __init__(self, w, h):
        self.w2 = w
        self.h2 = h

    @staticmethod
    def area(w2, h2):
        return w2 * h2


width = int(input("Enter a width: "))
height = int(input("Enter a height: "))

print(Shape.area(width, height))
