# Number Category Analyzer

n = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number

largest = first_number
smallest = first_number

count_positive = 1 if first_number > 0 else 0
count_negative = 1 if first_number < 0 else 0
count_zero = 1 if first_number == 0 else 0

total_positive = first_number if first_number > 0 else 0
total_negative = first_number if first_number < 0 else 0

count_even = 1 if first_number % 2 == 0 else 0
count_odd = 1 if first_number % 2 != 0 else 0

count_divisible_3_and_5 = 1 if first_number % 3 == 0 and first_number % 5 == 0 else 0
total_divisible_3_and_5 = first_number if first_number % 3 == 0 and first_number % 5 == 0 else 0

for _ in range(n - 1):
    current_number = int(input("Enter number: "))

    total += current_number

    if current_number > largest:
        largest = current_number
    if current_number < smallest:
        smallest = current_number

    if current_number > 0:
        count_positive += 1
        total_positive += current_number
    if current_number < 0:
        count_negative += 1
        total_negative += current_number
    if current_number == 0:
        count_zero += 1

    if current_number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

    if current_number % 3 == 0 and current_number % 5 == 0:
        count_divisible_3_and_5 += 1
        total_divisible_3_and_5 += current_number

print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Positive:", count_positive)
print("Negative:", count_negative)
print("Zero:", count_zero)
print("Positive sum:", total_positive)
print("Negative sum:", total_negative)
print("Even numbers:", count_even)
print("Odd numbers:", count_odd)
print("Divisible by both:", count_divisible_3_and_5)
print("Sum divisible by both:", total_divisible_3_and_5)