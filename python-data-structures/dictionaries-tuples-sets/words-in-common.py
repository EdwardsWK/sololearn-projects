"""Words In Common

    Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

    Sample Input:
    this is some text
    I would like this tea and some cookies

    Sample Output:
    2
"""

text1 = input("Input a sentence: ")
text2 = input("Input another sentence: ")

list1 = text1.split()
list2 = text2.split()

print(len(set(list1) & set(list2)))
