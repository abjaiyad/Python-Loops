# Inverted Star Pyramid

#  *********
#   *******
#    *****
#     ***
#      *

for i in range(5):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(9 - 2 * i):
        print("*", end="")
    print()