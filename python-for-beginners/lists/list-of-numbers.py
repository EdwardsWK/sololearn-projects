"""List of Numbers

    For loops allow you to easily iterate through lists.
    Given a list of numbers, calculate their sum using a for loop.
 """

number_array = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

total = 0

for number in number_array:
    total += number

print(total)
