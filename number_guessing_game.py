# Number guessing program

# generate the number between 1 and 100
import random
jackpot = random.randint(1, 100)

guess = int(input("Guess the number: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Wrong! guess higher")
    else:
        print("Wrong! guess lower")
    
    guess = int(input("Guess again: "))
    counter += 1
else:
    print("Correct guess")
    print("Attempts =", counter)