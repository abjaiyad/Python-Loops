# Count Numbers Above Average

n = int(input("How many numbers: "))

total = 0

for _ in range(n):
    num = int(input("Enter number: "))

    total += num

average = total / n

above_average = 0

for _ in range(n):
    num = int(input("Enter number again: "))

    if num > average:
        above_average += 1

print("Average:", average)
print("Numbers above average:", above_average)