# Find the largest digit

largest = 0

number = int(input("Enter the positive integer: "))

while number:
    digit = number % 10
    number = number // 10

    if digit > largest:
        largest = digit

print("Largest digit:", largest)