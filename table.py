# Create a program that prompts the user for a number and displays the table of that number using a loop.

# Prompt the user for a number
num = int(input("Enter a number: "))

# Use for loop to iterate through the range 1 to 11
for i in range(1, 11):
    # Display multiplication table entry
    print(num,"*",i,"=",(num * i))