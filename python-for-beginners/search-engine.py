"""Search Engine

    You’re working on a search engine. Watch your back Google!
    The given code takes a text and a word as input and passes them to a function called search().
    The search() function should return "Word found" if the word is present in the text, or "Word not found", if not.

    Sample Input
    "This is awesome"
    "awesome"

    Sample Output
    Word found
"""

text = input("Enter a sentence: ")
word = input("Enter a search word: ")


def search(sentence, search_word):
    if search_word in sentence:
        return "Word found"
    else:
        return "Word not found"


print(search(text, word))
