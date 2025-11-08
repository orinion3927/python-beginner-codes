import random

number = random.randint(1, 87)
if number >= 60:
    print("you are an old man")
elif number >= 18:
    print("you are an adult")
elif number < 4:
    print("you are a baby")
else:
    print("you are a child")

print("your age is:" ,number)