"""Date Picker

    You are creating a date picker for a website and need to output all of the years in a given period.
    Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.

    The output sequence should start with the first input number
    and end with the second input number, without including it.

    Sample Input
    2005
    2011

    Sample Output
    [2005, 2006, 2007, 2008, 2009, 2010]
"""

start_year = int(input("Enter a start year: "))
end_year = int(input("Enter an end year: "))

dates = list(range(start_year, end_year))

print(dates)
