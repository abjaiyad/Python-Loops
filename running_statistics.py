# Running Statistics

n = int(input("How many numbers: "))

total = 0

largest = None
smallest = None

for _ in range(n):

    num = int(input("Enter number: "))

    total += num

    if largest is None:
        largest = num
        smallest = num

    else:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    print("Running sum:", total)
    print("Largest:", largest)
    print("Smallest:", smallest)


average = total / n

print("Final sum:", total)
print(f"Average: {average:.2f}")
print("Largest:", largest)
print("Smallest:", smallest)