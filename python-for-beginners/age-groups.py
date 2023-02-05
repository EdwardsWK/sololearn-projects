"""Age Groups

    Given the age of a person as an input, output their age group.

    Here are the age groups you need to handle:
    Child: 0 to 11
    Teen: 12 to 17
    Adult: 18 to 64

    Sample Input
42
Sample
Output
Adult
Remember, you
can
use
the
Boolean and operator
to
combine
conditions, like
x > 0 and x < 20.
age = int(input())
if age <= 11:
    print("Child")
elif age <= 17:
    print("Teen")
else:
    print("Adult")