"""Line Them Up

    Take a string as input and output each letter of the string on a new line,
    repeated N times, where N is the position of the letter in the string.

    Sample Input:
    data

    Sample Output:
    d
    aa
    ttt
    aaaa
"""

text = input("Input a word: ")
i = 0

while i < len(text):
    print(text[i] * (i + 1))
    i += 1
