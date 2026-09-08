# Reverse a number

number = int(input("Enter number: "))
reverse = 0

while number:
    digit = number % 10
    number = number // 10
    reverse = reverse * 10 + digit

print("Reversed:", reverse)