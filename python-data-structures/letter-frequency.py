"""Letter Frequency

    You are making a program to analyze text.
    Take the text as the first input and a letter as the second input, and
    output the frequency of that letter in the text as a whole percentage.

    Sample Input:
    hello
    l

    Sample Output:
    40
"""

text = input("Input a sentence: ")
letter = input("Input a letter: ")

print(int(text.count(letter) / len(text) * 100))
