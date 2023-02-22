"""Ignore The Vowels

    Given a word as input, output a list, containing only the letters of the word that are not vowels.
    The vowels are a, e, i, o, u.

    Sample Input
    awesome

    Sample Output
    ['w', 's', 'm']
    """

text = input("Input a word or sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']

letters = [i for i in text if i not in vowels]

print(letters)
