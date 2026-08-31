# Second Smallest Number

n = int(input("How many numbers: "))

first = int(input("Enter number: "))
second = int(input("Enter number: "))

if first <= second:
    smallest = first
    second_smallest = second
else:
    second_smallest = first
    smallest = second

for _ in range(n - 2):
    num = int(input("Enter number: "))

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second smallest:", second_smallest)