# Challenge 40 — Divisibility Analyzer

# Now let's make the analyzer slightly smarter.

# 🎯 Goal

# Write a program that asks for n numbers and determines:

# Sum of all numbers
# Largest number
# Smallest number
# Count of numbers divisible by 3
# Count of numbers divisible by 5
# Count of numbers divisible by both 3 and 5
# Sum of numbers divisible by 3
# Sum of numbers divisible by 5
# 📥 Input

# First:

# How many numbers: 6

# Then enter 6 numbers.

# 📤 Expected Output

# For:

# 10
# 15
# 7
# 30
# 9
# 20

# Output:

# Sum: 91
# Largest: 30
# Smallest: 7
# Divisible by 3: 3
# Divisible by 5: 3
# Divisible by both: 2
# Sum divisible by 3: 54
# Sum divisible by 5: 75

# Constraints
# Use a for loop.
# No lists.
# Don't use sum(), max(), or min().
# Process each number once.
# Handle negative numbers and zero correctly.
# n >= 1.
# 🧪 Test Cases

# Test 1

# 4
# 3
# 5
# 10
# 15

# Expected:

# Sum: 33
# Largest: 15
# Smallest: 3
# Divisible by 3: 2
# Divisible by 5: 3
# Divisible by both: 1
# Sum divisible by 3: 18
# Sum divisible by 5: 30

# Test 2

# 3
# -15
# -6
# -10

# Expected:

# Sum: -31
# Largest: -6
# Smallest: -15
# Divisible by 3: 2
# Divisible by 5: 2
# Divisible by both: 1
# Sum divisible by 3: -21
# Sum divisible by 5: -25

# Test 3

# 5
# 1
# 2
# 4
# 7
# 11

# Expected:

# Sum: 25
# Largest: 11
# Smallest: 1
# Divisible by 3: 0
# Divisible by 5: 0
# Divisible by both: 0
# Sum divisible by 3: 0
# Sum divisible by 5: 0

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