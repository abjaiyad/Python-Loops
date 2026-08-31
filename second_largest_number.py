# Second Largest Number

count = int(input("How many numbers: "))

first_number = int(input("Enter number: "))
second_number = int(input("Enter number: "))

if first_number >= second_number:
    largest = first_number
    second_largest = second_number
else:
    largest = second_number
    second_largest = first_number

for _ in range(count - 2):
    current_number = int(input("Enter number: "))

    if current_number > largest:
        second_largest = largest
        largest = current_number
    elif current_number > second_largest:
        second_largest = current_number

print("Largest:", largest)
print("Second largest:", second_largest)