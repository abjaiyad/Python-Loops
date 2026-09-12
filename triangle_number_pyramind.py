# Triangle Number Pattern

#     1
#    222
#   33333
#  4444444
# 555555555

for i in range(5):

    for j in range(4 - i):
        print(" ", end="")

    for k in range(2 * i + 1):
        print(i + 1, end="")

    print()