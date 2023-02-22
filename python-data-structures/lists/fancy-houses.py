"""Fancy Houses

    You are analyzing house prices. The given code declares a list with house prices in the neighborhood.
    You need to calculate and output the number of houses that have a price that is above the average.
"""

prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

avg = sum(prices) / len(prices)
count = 0

for cost in prices:
    if cost > avg:
        count += 1

print(count)
