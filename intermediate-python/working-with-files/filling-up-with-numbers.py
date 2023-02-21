"""Filling Up With Numbers

    Take a number N as input and write the numbers 1 to N to the file "numbers.txt", each number on a separate line.

    Sample Input
    4

    Sample Output
    1
    2
    3
    4
"""

n = int(input("Enter a number: "))
file = open("numbers.txt", "w+")

for i in range(1,n+1):
    file.write(str(i) + "")
file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()
