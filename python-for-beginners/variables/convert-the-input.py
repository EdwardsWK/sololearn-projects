"""Convert The Input

    Write a program to take a string and a number as input and output the string, repeated x times.

    Sample Input
    hi
    3

    Sample Output
    hihihi
"""

text = input("Input a sentence: ")
repetitions = int(input("Input number of repetitions: "))

print(text * repetitions)
