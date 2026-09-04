# Divisibility Analyzer

n = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number

largest = first_number
smallest = first_number

count_divisible_3 = 1 if first_number % 3 == 0 else 0
count_divisible_5 = 1 if first_number % 5 == 0 else 0
count_both = 1 if first_number % 3 == 0 and first_number % 5 == 0 else 0

total_divisible_3 = first_number if first_number % 3 == 0 else 0
total_divisible_5 = first_number if first_number % 5 == 0 else 0

for _ in range(n - 1):
    num = int(input("Enter number: "))

    total += num

    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

    if num % 3 == 0:
        count_divisible_3 += 1
        total_divisible_3 += num
    if num % 5 == 0:
        count_divisible_5 += 1
        total_divisible_5 += num
    if num % 3 == 0 and num % 5 == 0:
        count_both += 1

print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Divisible by 3:", count_divisible_3)
print("Divisible by 5:", count_divisible_5)
print("Divisible by both:", count_both)
print("Sum divisible by 3:", total_divisible_3)
print("Sum divisible by 5:", total_divisible_5)