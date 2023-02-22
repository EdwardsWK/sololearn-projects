"""Apple of My Eye

    You are given a 2D matrix, which represents the number of people in a room, grouped by their eye color and gender.
    The first row represents the male gender, while the second row represents females.
    The columns are the eye colors, in the following order: brown, blue, green, black

    The data shows that, for example, there are 20 green eyed females in the room (2nd row, 3rd column).
    Our program needs to take eye color as input and output the percentage of people with that eye color in the room.

    Sample Input:
    blue

    Sample Output:
    36
"""

data = [
    [23, 11, 5, 14],
    [8, 32, 20, 5]
]

color = input("Input an eye color: ")
total = 118

if color == "brown":
    print(int((data[0][0] + data[1][0]) * 100 / total))
elif color == "blue":
    print(int((data[0][1] + data[1][1]) * 100 / total))
elif color == "green":
    print(int((data[0][2] + data[1][2]) * 100 / total))
else:
    print(int((data[0][3] + data[1][3]) * 100/total))
