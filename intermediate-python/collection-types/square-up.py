"""Square Up

    Tuples can be used to output multiple values from a function.
    You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
    The perimeter is the sum of all sides, while the area is the square of the side length.

    Sample Input
    3

    Sample Output
    Perimeter: 12
    Area: 9
"""


def calculate(x):
    return x * 4, x ** 2


side = int(input("Enter the length of the square: "))
perimeter, area = calculate(side)

print("Perimeter: " + str(perimeter))
print("Area: " + str(area))
