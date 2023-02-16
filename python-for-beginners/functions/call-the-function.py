"""Call The Function

    The given program defines a function print_bill(), which takes one string argument and outputs formatted text.
    You need to take the user input and call the function by passing the input as its argument.
    You need to only call the function, as it will take care of the output.
 """


def print_bill(text):
    print("======")
    print(text)
    print("======")


print_bill(input("Enter a word: "))
