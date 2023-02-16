"""Car Data

    You are working at a car dealership and store the car data in a dictionary:

    car = {
        'brand': 'BMW',
        'year': 2018,
        'color': 'red'
    }

    Your program needs to take the key as input and output the corresponding value.

    Sample Input
    year

    Sample Output
    2018
"""

car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

print(car[input("Please enter a category")])
