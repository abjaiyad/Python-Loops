# Binary Diamond

#     1
#    010
#   10101
#  0101010
# 101010101
#  0101010
#   10101
#    010
#     1


n = int(input("Enter a positive integer n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(2 * n - 3 - (2 * i)):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()