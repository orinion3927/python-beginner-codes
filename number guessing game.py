import random
import time

number = random.randint(1, 5)
guess = int(input("Welcome to the number guessing game!\nGuess a number from 1 to 5: "))

if guess == number:
    print("You won!")
else:
    print("You lose.")

print("The number was:", number)
# do not copy this code or other codes from the repository "python beginner codes". (in github)
