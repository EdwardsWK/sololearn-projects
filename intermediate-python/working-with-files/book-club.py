"""Book Club

    You are given a books.txt file, which includes book titles, each on a separate line.
    Create a program to output how many words each title contains, in the following format:
    Line 1: 3 words
    Line 2: 5 words
"""

with open("/usercode/files/books.txt") as file:
    j = 1
    for line in file:
        print("Line " + str(j) + ": " + str(len(line.split(" "))) + " words")
        j += 1
