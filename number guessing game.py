import random
import time

number = random.randint(1, 5)
guess = int(input("welcome to the number guessing game!
Guess a number from 1 to 5: "))

if guess == number:
    print("You won!")
else:
    print("You lose.")

print("The number was:", number)
