# Number Spiral

n = int(input("Enter a positive integer n: "))

top = 0
bottom = n - 1
left = 0
right = n - 1
number = 1

matrix = []

for i in range(n):
    matrix.append([0] * n)

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = number
        number += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = number
        number += 1
    right -= 1
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = number
        number += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = number
        number += 1
    left += 1

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()