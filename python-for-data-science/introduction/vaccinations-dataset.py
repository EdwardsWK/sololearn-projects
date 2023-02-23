"""Vaccinations Dataset

    Using the same vaccinations dataset, which includes the number of times people got the flu vaccine.
    The dataset contains the following numbers:
    never: 5
    once: 8
    twice: 4
    3 times: 3

    Calculate and output the variance.
    We will soon learn about easier ways to calculate the variance and other summary statistics using Python.
    For now, use Python code to calculate the result using the corresponding equation.
"""

vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]


def variance(data):
    total = sum(data)
    class_size = len(data)
    # Mean of the data
    mean = total / class_size
    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]
    # Variance
    spread = sum(deviations) / class_size
    return spread


print(variance(vac_nums))
