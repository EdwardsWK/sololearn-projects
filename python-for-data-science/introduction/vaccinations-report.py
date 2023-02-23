"""Vaccinations Report

    We have a report on the number of flu vaccinations in a class of 20 people.
    It has the following numbers:
    never: 5
    once: 8
    twice: 4
    3 times: 3

    What is the mean number of times those people have been vaccinated?
    Output the result using the print() statement.
"""

vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]

total = sum(vac_nums)
class_size = len(vac_nums)

mean = total / class_size

print(mean)
