# Frequency of Every Digit

number = int(input("Enter number: "))

original = number

for target in range(10):
    count = 0
    number = original

    if original == 0 and target == 0:
        count = 1

    while number:
        digit = number % 10

        if digit == target:
            count += 1

        number //= 10

    print(target, "→", count)