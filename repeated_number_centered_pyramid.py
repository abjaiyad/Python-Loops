# Repeated Number Centered Pyramid

#       1
#      222
#     33333
#    4444444
#   555555555
#  66666666666
# 7777777777777

for i in range(7):
    for j in range(6 - i):
        print(" ", end="")

    for j in range(2 * i + 1):
        print(i + 1, end="")
    print()