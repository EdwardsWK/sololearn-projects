"""Welcome, Sololearner!

    We have a function that outputs "Welcome, user" as it is called. We want to make it more personalized, so redesign the given function so that it will take the name of the user as input and output the welcome message with it.

    Sample Input
    Tommy

    Sample Output
    Welcome, Tommy
"""


def welcome():
    name = input("Input your name: ")
    print("Welcome, " + name)


welcome()
