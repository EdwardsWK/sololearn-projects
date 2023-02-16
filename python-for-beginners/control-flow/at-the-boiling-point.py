"""At The Boiling Point

    Write a program that checks if the water is boiling.
    Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.

    Sample Input
    105

    Sample Output
    Boiling

    Do not output anything if the water is not boiling.
"""

temperature = int(input("Input a temperature: "))

if temperature >= 100:
    print("Boiling")
