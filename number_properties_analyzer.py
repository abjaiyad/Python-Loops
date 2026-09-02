# Number Properties Analyzer

n = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number

largest = first_number
smallest = first_number

count_even = 1 if first_number % 2 == 0 else 0
count_odd = 1 if first_number % 2 != 0 else 0

total_even = first_number if first_number % 2 == 0 else 0
total_odd = first_number if first_number % 2 != 0 else 0

positive = 1 if first_number > 0 else 0
negative = 1 if first_number < 0 else 0
zero = 1 if first_number == 0 else 0

for _ in range(n - 1):
    current_num = int(input("Enter number: "))

    total += current_num

    if current_num > largest:
        largest = current_num
    if current_num < smallest:
        smallest = current_num

    if current_num % 2 == 0:
        count_even += 1
        total_even += current_num
    else:
        count_odd += 1
        total_odd += current_num

    if current_num > 0:
        positive += 1
    elif current_num < 0:
        negative += 1
    else:
        zero += 1

average = total / n

print("Total numbers:", n)
print("Sum:", total)
print(f"Average: {average:.2f}")
print("Largest:", largest)
print("Smallest:", smallest)

print("Even numbers:", count_even)
print("Odd numbers:", count_odd)

print("Even sum:", total_even)
print("Odd sum:", total_odd)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)