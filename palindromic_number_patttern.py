# Palindromic Number Pyramid

# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(5):
    for j in range(i + 1):
        print(j + 1, end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()