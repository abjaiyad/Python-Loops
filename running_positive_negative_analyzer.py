# Running Positive/Negative Analyzer

n = int(input("How many numbers: "))

total = 0

largest = None
smallest = None

positive_count = 0
negative_count = 0
zero_count = 0

positive_sum = 0
negative_sum = 0


for _ in range(n):
    num = int(input("Enter number: "))

    total += num

    if num > 0:
        positive_count += 1
        positive_sum += num
    elif num < 0:
        negative_count += 1
        negative_sum += num
    else:
        zero_count += 1


    if largest is None:
        largest = num
        smallest = num

    else:
        if num > largest:
            largest = num

        if smallest is not None and num < smallest:
            smallest = num

    print("Running sum:", total)
    print("Running positive count:", positive_count)
    print("Running negative count:", negative_count)
    print("Running zero count:", zero_count)
    print("Largest:", largest)
    print("Smallest:", smallest)

average = total / n

print("\n-----Results-----")
print("Final sum:", total)
print(f"Average: {average:.2f}")
print("Largest:", largest)
print("Smallest:", smallest)
print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Zero count:", zero_count)
print("Positive sum:", positive_sum)
print("Negative sum:", negative_sum)