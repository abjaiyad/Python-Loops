# Diamond pattern

for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(5):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(7 - 2 * i):
        print("*", end="")
    print()