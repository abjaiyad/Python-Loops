# Number Analyzer

n = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number
largest = first_number
smallest = first_number

positive = 1 if first_number > 0 else 0
negative = 1 if first_number < 0 else 0
zero = 1 if first_number == 0 else 0

for _ in range(n - 1):
    num = int(input("Enter number: "))
    total += num

    if num > largest:
        largest =  num
    if num < smallest:
        smallest = num

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
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