#password: Pas$W0rd193
import random
import time
import turtle


def write_with_outline(text, x, y, font=("Arial", 30, "normal"), color="white", outline="black"):
    turtle.penup()

    
    for dx, dy in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
        turtle.goto(x + dx, y + dy)
        turtle.color(outline)
        turtle.write(text, align="center", font=font)

    
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align="center", font=font)



screen = turtle.Screen()
screen.title("AI.PROTOTYPE_385")
screen.setup(width=1300, height=800)


screen.bgpic("LoadingScreen.gif")



turtle.hideturtle()
turtle.speed(0)

write_with_outline("AI.PROTOTYPE_385", 0, 0, font=("Arial", 30, "normal"), color="white", outline="black")
write_with_outline("Loading...", 0, -40, font=("Arial", 20, "normal"), color="white", outline="black")

time.sleep(2)
turtle.bye()


def List():
    print()
    print("------------------------------------------------------------------------------------")
    print("password: Pas$W0rd193")
    print("version: 3.8")
    print("credits: created by orinion")
    print("------------------------------------------------------------------------------------")
    print()

def AboutMe():
    print()
    print("------------------------------------------------------------------------------------")
    print("i am an AI prototype created by orinion.")
    print("i am currently in version 3.8")
    print("i am constantly learning and improving, so stay tuned for future updates!")
    print("------------------------------------------------------------------------------------")
    print()

def NumberGuessingGame():
    print()
    print("------------------------------------------------------------------------------------")
    TrueAnswer = random.randint(1, 5)
    guess = int(input("Welcome to the number guessing game!\nGuess a number from 1 to 5: "))
    if guess == TrueAnswer:
        print("You won!")
    else:
        print("You lose.")
    print("The number was:", TrueAnswer)
    NTryAgainChoice = input("Do you want to try again? (yes/no): ")
    if NTryAgainChoice in ["yes", "y", "sure", "yeah"]:
        NumberGuessingGame()
    else:
        print("exiting the number guessing game...")
    print("------------------------------------------------------------------------------------")
    print()

def AgeScanner():
    print()
    print("------------------------------------------------------------------------------------")
    age=int(input("please enter your age: "))
    if age >= 120:
        print("BRO ARE YOU KIDDING ME? DONT LIE")
        exit()
    elif age >= 67:
        print("you are an old man")
    elif age >= 18:
        print("you are an adult")
    elif age <= 4:
        print("you are a baby")
    else:
        print("you are a child")
    ATryAgainChoice = input("Do you want to try again? (yes/no): ")
    if ATryAgainChoice in ["yes", "y", "sure", "yeah"]:
        AgeScanner()
    else:
        print("exiting the age scanner...")
    print("------------------------------------------------------------------------------------")
    print()


while True:
    Try = input("please Enter password: ")
    if Try == "Pas$W0rd193":
        print("------------------------------------------------------------------------------------")
        print()
        print("checking...")
        print()
        time.sleep(1)
        print()
        print("access granted")
        choise = input("do you want to continue to the smart_AI test? (yes/no): ")
        if choise == "yes" or choise == "yeah" or choise == "y" or choise == "sure":
            time.sleep(0.1)
            print("continuing...")
            time.sleep(1)
            print("opening files...")
            time.sleep(1)
            print("starting program...")
            time.sleep(1)
            print("------------------------------------------------------------------------------------")
            print()
            name = input("hello, what is your name? ")
            time.sleep(0.1)
            print("loading...")
            time.sleep(1)
            print()
            print("------------------------------------------------------------------------------------")
            print()
            while True:
                print("hello, " + name)
                print("my name is AI.PROTOTYPE_385.")
                print()
                print()
                print("so what do you want to do " + name + "?")
                print("the options are:")
                print()
                print("1. get to know more about me (write 'about me' or '1')")
                print("2. exit the program (write 'exit' or '2')")
                print("3. check the list (write 'list' or '3')")
                print("4. play the number guessing game (write 'number guessing game' or '4')")
                print("5. age scanner (write 'age scanner' or '5')")
                print()
                choise_from_options = input("please enter your choise: ")

                if choise_from_options == "about me" or choise_from_options == "1":
                    AboutMe()
                    print()
                    back_to_options=input("wanna go back to the options menu? (yes/no): ")
                    if back_to_options in ["yes","y","sure","yeah"]:
                        time.sleep(0.1)
                        print("going back to options menu...")
                        time.sleep(1)
                        continue
                    else:
                        time.sleep(0.1)
                        print("exiting...")
                        time.sleep(1)
                        print("goodbye! see ya later!")
                        print()
                        print()
                        print()
                        print()
                        print()
                        print("==test completed==")
                        exit()

                elif choise_from_options == "exit" or choise_from_options == "2":
                    time.sleep(0.1)
                    print("exiting...")
                    time.sleep(1)
                    print("goodbye! see ya later!")
                    print()
                    print()
                    print()
                    print()
                    print()
                    print("==test completed==")
                    exit()

                elif choise_from_options == "list" or choise_from_options == "3":
                    List()
                    print()
                    back_to_options=input("wanna go back to the options menu? (yes/no): ")
                    if back_to_options in ["yes","y","sure","yeah"]:
                        time.sleep(0.1)
                        print("going back to options menu...")
                        time.sleep(1)
                        continue
                    else:
                        time.sleep(0.1)
                        print("exiting...")
                        time.sleep(1)
                        print("goodbye! see ya later!")
                        print()
                        print()
                        print()
                        print()
                        print()
                        print("==test completed==")
                        exit()

                elif choise_from_options == "number guessing game" or choise_from_options == "4":
                    NumberGuessingGame()
                    print()
                    back_to_options=input("wanna go back to the options menu? (yes/no): ")
                    if back_to_options in ["yes","y","sure","yeah"]:
                        time.sleep(0.1)
                        print("going back to options menu...")
                        time.sleep(1)
                        continue
                    else:
                        time.sleep(0.1)
                        print("exiting...")
                        time.sleep(1)
                        print("goodbye! see ya later!")
                        print()
                        print()
                        print()
                        print()
                        print()
                        print("==test completed==")
                        exit()

                elif choise_from_options == "age scanner" or choise_from_options == "5":
                    AgeScanner()
                    print()
                    back_to_options=input("wanna go back to the options menu? (yes/no): ")
                    if back_to_options in ["yes","y","sure","yeah"]:
                        time.sleep(0.1)
                        print("going back to options menu...")
                        time.sleep(1)
                        continue
                    else:
                        time.sleep(0.1)
                        print("exiting...")
                        time.sleep(1)
                        print("goodbye! see ya later!")
                        print()
                        print()
                        print()
                        print()
                        print()
                        print()
                        print()
                        print("==test completed==")
                        exit()

        else:
            print("invalid choise. exiting...")
            time.sleep(1)
            print("goodbye! see ya later!")
            print()
            print()
            print()
            print()
            print()
            print("==test completed==")
            exit()

    else:
        time.sleep(0.1)
        print("wrong password. trying again...")
        time.sleep(1)
        continue

# do not copy this code or other codes from the repository "python beginner codes". (in github)
