# Digit Occurrence Counter

number = int(input("Enter number: "))

target = int(input("Enter target digit: "))

count = 0

while number:
    digit = number % 10

    if digit == target:
        count += 1

    number //= 10

print(f"{target} appears {count} times")