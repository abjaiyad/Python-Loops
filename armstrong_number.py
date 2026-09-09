# Armstrong Number

number = int(input("Enter number: "))

original = number
total = 0

while number:
    digit = number % 10
    total += digit ** 3
    number //= 10

if original == total:
    print("Armstrong")
else:
    print("Not Armstrong")