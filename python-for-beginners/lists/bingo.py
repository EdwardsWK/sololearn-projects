"""Bingo

    Given a list of numbers, output "bingo" if it contains the input number.
    Do not output anything if the number is not found.
"""

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

number = int(input("Input a number: "))

if number in x:
    print("bingo")
