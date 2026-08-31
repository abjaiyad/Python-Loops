# Average + Largest + Smallest

count = int(input("How many numbers: "))

first_number = int(input("Enter number: "))

total = first_number

largest = first_number
smallest = first_number

for _ in range(1, count):
    current_number = int(input("Enter number: "))

    total += current_number

    if current_number > largest:
        largest = current_number

    if current_number < smallest:
        smallest = current_number

average = total / count

print("Sum:", total)
print(f"Average: {average:.2f}")
print("Largest:", largest)
print("Smallest:", smallest)