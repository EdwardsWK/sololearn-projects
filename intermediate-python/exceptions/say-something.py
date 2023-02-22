"""Say Something

    You are making a program to post tweets. Each tweet must not exceed 42 characters.
    Complete the program to raise an exception, in case the length of the tweet is more than 42 characters.
"""

tweet = input("Input a tweet: ")

try:
    if len(tweet) > 42:
        raise Exception("Error")

except Exception as e:
    print(e)

else:
    print("Posted")
