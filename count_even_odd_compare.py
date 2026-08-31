# Count Even and Odd Digits + Compare

number = int(input("Enter number: "))

count_even = 0
count_odd = 0


while number != 0:
    digit = number % 10

    if digit % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

    number = number // 10

if count_even > count_odd:
    message = "More even digits"
elif count_odd > count_even:
    message = "More odd digits"
else:
    message = "Equal number of even and odd digits"

print("Even digits:", count_even)
print("Odd digits:", count_odd)
print(message)