# Number Frequency

count = int(input("How many numbers: "))

total = 0
count_positive = 0
count_negative = 0
count_zero = 0

for _ in range(count):
    number = int(input("Enter number: "))

    total += number

    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1
    else:
        count_zero += 1

print("Positive:", count_positive)
print("Negative:", count_negative)
print("Zero:", count_zero)
print("Sum:", total)