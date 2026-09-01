# Number Classification Analyzer

n = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number
largest = first_number
smallest = first_number

positive = 1 if first_number > 0 else 0
negative = 1 if first_number < 0 else 0
zero = 1 if first_number == 0 else 0

total_positive = first_number if first_number > 0 else 0
total_negative = first_number if first_number < 0 else 0

for _ in range(n - 1):
    current_num = int(input("Enter number: "))
    total += current_num

    if current_num > largest:
        largest = current_num
    if current_num < smallest:
        smallest = current_num

    if current_num > 0:
        positive += 1
        total_positive += current_num
    elif current_num < 0:
        negative += 1
        total_negative += current_num
    else:
        zero += 1

average = total / n

print("Sum:", total)
print(f"Average: {average:.2f}")
print("Largest:", largest)
print("Smallest:", smallest)
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
print("Positive sum:", total_positive)
print("Negative sum:", total_negative)