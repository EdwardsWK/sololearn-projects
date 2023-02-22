"""Insect Control

    The number of insects in a lab doubles in size every month.

    Take the initial number of insects as input and output a list, showing the number of
    insects for each of the next 12 months, starting with 0, which is the initial value.

    Sample Input:
    10

    Sample Output:
    [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
"""

number = int(input("Input the number of insects: "))

insects = [number * 2 ** i for i in range(12)]

print(insects)
