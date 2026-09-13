# Number-Star Triangle

number = 0

n = int(input("Enter a positive integer n: "))

for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            number += 1
            print(number, end="")
        else:
            print("*", end="")
    print()