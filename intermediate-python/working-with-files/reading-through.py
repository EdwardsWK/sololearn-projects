"""Reading Through

    You need to make a program to read the given number of characters of a file.
    Take a number N as input and output the first N characters of the books.txt file.
"""

file = open("/usercode/files/books.txt")
word = int(input("Input a word number: "))

print(file.read(word))

file.close()
