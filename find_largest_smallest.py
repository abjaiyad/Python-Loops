# Find Largest and Smallest

count = int(input("How many number: "))

first_number = int(input("Enter number: "))

total =  first_number

largest = first_number
smallest = first_number

for _ in range(1, count):
    current_number = int(input("Enter number: "))

    total += current_number

    if current_number > largest:
        largest = current_number

    if current_number < smallest:
        smallest = current_number

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)