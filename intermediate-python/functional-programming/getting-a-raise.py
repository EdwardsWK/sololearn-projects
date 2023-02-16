"""Getting A Raise

    You work on a payroll program.
    Given a list of salaries, you need to take the bonus everybody is
    getting as input and increase all the salaries by that amount.

    Output the resulting list.
"""

salaries = [2000, 1800, 3100, 4400, 1500]

bonus = int(input("Enter a bonus amount: "))


def add_things(wages):
    return wages + bonus


result = list(map(add_things,salaries))

print(result)
