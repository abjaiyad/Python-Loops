# Find Smallest Digit

smallest = 9

number = int(input("Enter the positive integer: "))

while number:
    digit = number % 10
    number //= 10

    if digit < smallest:
        smallest = digit

print("Smallest digit:", smallest)