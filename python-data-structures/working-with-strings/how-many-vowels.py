"""How Many Vowels

    You need to make a program that counts the number of vowels in a given text.
    The vowels are a, e, i, o, and u.

    Take a string as input and output the number of vowels.

    Sample Input:
    this is great

    Sample Output:
    4 vowels
"""

text = input("Input a string: ")
count = 0

for letter in text:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count += 1

print(count, "vowels")
