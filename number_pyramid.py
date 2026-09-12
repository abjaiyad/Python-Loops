# Number Pyramid

# 1
# 12
# 123
# 1234
# 12345
# 123456

for i in range(6):
    for j in range(i + 1):
        print(j + 1, end="")
    print()