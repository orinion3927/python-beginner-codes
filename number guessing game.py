import random
import time

number = random.randint(1, 5)
name=input("guess a number from 1 to 5: ")
if name == number:
  print("you won")
else:
  print("you lose")
print(number)
