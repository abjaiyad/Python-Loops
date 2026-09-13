# Mixed Number-Star Diamond

number = 0

n = int(input("Enter a positive integer n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if (i + j) % 2 == 0:
            number += 1
            print(number, end="")
        else:
            print("*", end="")
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(2 * n - 3 - (2 * i)):
        if (n + i + j) % 2 == 0:
            number += 1
            print(number, end="")
        else:
            print("*", end="")
    print()