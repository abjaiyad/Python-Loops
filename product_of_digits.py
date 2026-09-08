# Product of Digits

product = 1

number = int(input("Enter number: "))

while number:
    digit = number % 10
    product *= digit
    number //= 10

print(product)