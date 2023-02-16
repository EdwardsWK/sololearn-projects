"""Collecting Reports

    You are working on an invoicing system.
    The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
    You need to add a decorator for the invoice() function, that will print the invoice in the following format:

    Sample Input
    42

    Sample Output
    ***
    INVOICE #42
    ***
    END OF PAGE
"""


def decor(function):
    def wrap(number):
        print("***")
        function(number)
        print("***")
        print("END OF PAGE")
    return wrap


@decor
def invoice(number):
    print("INVOICE #" + number)


invoice(input("Enter an invoice number: "))
