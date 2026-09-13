# Hollow Number Pyramid

n = int(input("Enter a positive integer n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if i == n - 1 or j == 0 or j == 2 * i:
            print(i + 1, end="")
        else:
            print(" ", end="")
    print()