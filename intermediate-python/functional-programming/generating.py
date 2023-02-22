"""Generating

    Finding prime numbers is a common coding interview task.
    The given code defines a function isPrime(x), which returns True if x is prime.

    You need to create a generator function primeGenerator(), that will take two numbers as arguments, and
    use the isPrime() function to output the prime numbers in the given range (between the two arguments).

    Sample Input
    10
    20

    Sample Output
    [11, 13, 17, 19]
"""


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n ==0:
            return False
    return True


def prime_generator(start, end):
    for number in range(start, end):
        if is_prime(number):
            yield number


start = int(input("Input the start of the range: "))
end = int(input("Input the end of the range: "))

print(list(prime_generator(start, end)))
