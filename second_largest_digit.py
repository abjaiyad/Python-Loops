# Second Largest Digit

number = int(input("Enter number: "))

largest = 0
second_largest = None

while number:
    digit = number % 10

    if digit > largest:
        second_largest = largest
        largest = digit

    elif second_largest is None:
        second_largest = digit

    elif digit < largest and digit > second_largest:
        second_largest = digit

    number //= 10

print("Largest:", largest)
print("Second largest:", second_largest)