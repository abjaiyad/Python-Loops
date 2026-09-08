# Sum of Digits

number = int(input("Enter number: "))
total = 0

while number:
    digit = number % 10
    total += digit
    number = number // 10

print("Sum of digits:", total)