"""Basketball Players

    The given code includes a list of heights for various basketball players.
    You need to calculate and output how many players are in the range of one standard deviation from the mean.
"""

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
total = sum(players)
num_of_players = len(players)

mean = total / num_of_players
std = (sum((v - mean) ** 2 for v in players) / len(players)) ** 0.5
low = mean - std
high = mean + std

count = len([v for v in players if low < v < high])

print(count)
