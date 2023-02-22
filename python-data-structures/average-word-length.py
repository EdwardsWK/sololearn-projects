"""Average Word Length

    Given a sentence as input, calculate and output the average word length of that sentence.

    Sample Input:
    this is some text

    Sample Output:
    3.5
"""

text = input("Input a sentence: ")
words = text.split()

total = sum(map(len,words)) / len(words)

print(total)
