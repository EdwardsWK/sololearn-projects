"""Spelling Backwards

    Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

    Sample Input
    HELLO

    Sample Output
    O
    L
    L
    E
    H
"""


def spell(text):
    print(text[::-1])


text = input("Input a word: ")

spell(text)
