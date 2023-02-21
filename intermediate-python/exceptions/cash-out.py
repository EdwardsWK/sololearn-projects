"""Cash Out

    An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
    In case the input is not a number, the machine should output "Please enter a number".

    Use exception handling to take a number as input, call the withdraw() method with the input
    as its argument, and output "Please enter a number", in case the input is not a number.
"""


def withdraw(amount):
    print(str(amount) + " withdrawn!")


withdrawal = input("Enter a withdrawal amount: ")

try:
    int(withdrawal)
    withdraw(withdrawal)

except ValueError:
    print("Not a number")
