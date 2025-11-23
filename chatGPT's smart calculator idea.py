import time

print("------------------------------------------------------------------------------------")
print()
print("hello, whats your name?")
print()
name = input()
print("------------------------------------------------------------------------------------")
print()
print("hello, " + name)
print()
print("------------------------------------------------------------------------------------")
print()
print("my name is AI.PROTOTYPE385 — your personal calculator assistant!")
print()
print("------------------------------------------------------------------------------------")

while True:
    print()
    print("Type any math expression and I'll solve it for you!")
    print("For example: 12 + 5 * 2")
    expression = input("Enter your calculation: ")

    print()
    print("Analyzing your input...")
    time.sleep(1.5)
    print("Thinking...")
    time.sleep(1.5)
    print("Almost done...")
    time.sleep(1.2)

    try:
        result = eval(expression)
        print()
        print("------------------------------------------------------------------------------------")
        print("The answer is:", result)
        print("------------------------------------------------------------------------------------")
    except:
        print()
        print("------------------------------------------------------------------------------------")
        print("Sorry, I couldn't understand that. Try again!")
        print("------------------------------------------------------------------------------------")

    again = input("Do you want to calculate something else? (yes/no): ").lower()
    if again != "yes":
        print("------------------------------------------------------------------------------------")
        print("Goodbye, " + name + "! See you next time!")
        print("------------------------------------------------------------------------------------")
        break
# do not copy this code or other codes from the repository "python beginner codes". (in github)
