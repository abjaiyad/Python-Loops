# Count Even & Odd Digits

even_count = 0
odd_count = 0

number =  int(input("Enter number: "))

while number:

    digit = number % 10

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = number // 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)