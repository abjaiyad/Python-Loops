# Repeated Binary Row Pattern

# Expected output for n = 5:

# 1
# 00
# 111
# 0000
# 11111

n = int(input("Enter a positive integer n: "))

for i in range(n):
    for j in range(i + 1):
        if i % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()