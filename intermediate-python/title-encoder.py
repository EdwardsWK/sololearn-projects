"""Title Encoder

    You are given a file named "books.txt" with book titles, each on a separate line.x
    To encode the book titles you need to take the first letters of each word in the title and combine them.
    For example, for the book title "Game of Thrones" the encoded version should be "GoT".

    Complete the program to read the book title from the file and output the encoded versions, each on a new line.
"""

file = open("/usercode/files/books.txt", "r")

for x in file:
    title = x.split()
    for a in title:
        print(a[0], end="")
    print()

file.close()
