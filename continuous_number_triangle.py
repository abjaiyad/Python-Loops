# Continuous Number Triangle
# 1
# 23
# 456
# 78910

number = 1

for i in range(4):
    for j in range(i + 1):
        print(number, end="")
        number += 1
    print()