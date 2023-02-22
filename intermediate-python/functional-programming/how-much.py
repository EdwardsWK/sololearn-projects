"""How Much?

    You are given code that should calculate the corresponding percentage of a price.
    Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
    Fix the code to output the given percentage of the price.

    Sample Input
    50
    10

    Sample Output
    5.0
"""

price = int(input("Input a price: "))
percentage = int(input("Input a discount amount: "))

result = (lambda x, y: x * y/100)(price, percentage)

print(result)
