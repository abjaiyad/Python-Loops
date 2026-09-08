# Count digits

number = int(input("Enter number: "))

count = 0

while number:
    number = number // 10
    count += 1

print(count)