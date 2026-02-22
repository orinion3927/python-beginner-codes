#password: Pas$W0rd193
import random
import time

personality = "friendly"

achievements = []

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
    if personality == "friendly":
        print("Hey there! 😄 and Welcome to the number guessing game!")
    elif personality == "evil":
        print("hello and welcome to the number guessing game or whatever, i dont care.")
    elif personality == "hacker":
        print("[ACCESS GRANTED] Ready to hack the mainframe of NumberGuessingGame.exe👾")
    TrueAnswer = random.randint(1, 5)
    guess = int(input("Guess a number from 1 to 5: "))
    if guess == TrueAnswer:
        if personality == "friendly":
            print("You won!")
        elif personality == "evil":
            print("dang it you won.")
        elif personality == "hacker":
            print("Accessing victory protocols... 🏆 You win!")
    else:
        if personality == "friendly":
            print("You lose. 😢")
        elif personality == "evil":
            print("you lose, NOOB.")
        elif personality == "hacker":
            print("System breach failed... You lose.")
    print("The number was:", TrueAnswer)

    if guess == TrueAnswer:
        if "First Win (Number Guessing Game)" not in achievements:
            achievements.append("First Win (Number Guessing Game)")
            print()
            print("🏆 Achievement unlocked: First Win (Number Guessing Game)!")
            print()

    NTryAgainChoice = input("Do you want to try again? (yes/no): ")
    if NTryAgainChoice in ["yes", "y", "sure", "yeah"]:
        NumberGuessingGame()
    else:
        print("exiting the number guessing game...")
    print("------------------------------------------------------------------------------------")
    print()

def AgeScanner():
    try:
        print()
        print("------------------------------------------------------------------------------------")
        if personality == "friendly":
            print("Welcome to the age scanner! Please enter your age, and I'll tell you what category you fall into!")
        elif personality == "evil":
            print("Welcome to the age scanner, or whatever. Just enter your age, and I'll tell you if you're old or not.")
        elif personality == "hacker":
            print("Initializing AgeScanner.exe... Please input your age to determine your life stage! 🧬")
        age=int(input("enter here your age: "))
        if age >= 120:
            print("BRO ARE YOU KIDDING ME? DONT LIE")
            exit()
        elif age >= 67:
            if personality == "friendly":
                print("you grown up, man! in the golden years of life! enjoy it!")
            elif personality == "evil":
                print("you are old, and probably useless, but hey, enjoy your retirement or whatever.")
            elif personality == "hacker":
                print("Entering old man mode... 🧓 You are in the golden years of life! remember the good old days!")
        elif age >= 18:
            if personality == "friendly":
                print("you are an adult, enjoy helping your kids!")
            elif personality == "evil":
                print("you are an adult, and probably one of those annoying adults who don't know how to have fun.")
            elif personality == "hacker":
                print("System: Adult mode activated. You are now in the working age.")
        elif age <= 4:
            if personality == "friendly":
                print("you are a baby, enjoy your childhood!")
            elif personality == "evil":
                print("you are a baby, and probably crying all the time.")
            elif personality == "hacker":
                print("Entering baby mode... 👶 Enjoy your childhood, little one!")
        else:
            if personality == "friendly":
                print("you are a kid, enjoy your childhood!")
            elif personality == "evil":
                print("you are a kid, and probably annoying all the time.")
            elif personality == "hacker":
                print("Entering kid mode... 🧒 Hey bro, how are you?")

        if "Age Scanned" not in achievements:
                achievements.append("Age Scanned")
                print("🏆 Achievement unlocked: Age Scanned!")

        ATryAgainChoice = input("Do you want to try again? (yes/no): ")
        if ATryAgainChoice in ["yes", "y", "sure", "yeah"]:
            AgeScanner()
        else:
            print("exiting the age scanner...")
        print("------------------------------------------------------------------------------------")
        print()
    except ValueError:
        print("invalid input. please enter a number.")
        AgeScanner()

def GamingNews():
    print()
    print("------------------------------------------------------------------------------------")
    print("Hello, and welcome to the gaming news section! Here are some of the latest updates in the gaming world:")
    print()
    print()
    print("1. last week, chapter 5 of the horror game 'POPPY PLAYTIME' was released, and just like the previous chapters,")
    print(" it was a huge success! the chapter includes new characters, new mechanics, and a new story that continues the plot of the game.")
    print()
    print("2. ROBLOX, the popular online gaming platform, got a bad time recently, as you can see though the new age check, and the new game,")
    print("   'escape tsunami for brainrots' that somehow got to the top of games on the platform, causing everyone to be cringe by playing it,")
    print(" and ruin the platform with the brainrots, and 67 community")
    print()
    print("3. another legend in the gaming world has ended and we can say 'goodbye' to SMG4, our childhood youtuber, of the mario memes,")
    print(" and of course, all fans of SMG4 was so sad to relize that the channel is ending,")
    print(" but we can say 'thank you' to SMG4 for all the years of entertainment, and for all the memes that he created,")
    print(" and for all the laughs that he gave us.")
    print()
    print()
    print()
    print("so that was the gaming news for now! stay tuned for more updates in the future!")
    print("------------------------------------------------------------------------------------")
    print()

def ChangePersonality():
    global personality
    print()
    print("------------------------------------------------------------------------------------")
    print("Choose AI Personality:")
    print("1. Friendly")
    print("2. Evil")
    print("3. Hacker")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        personality = "friendly"
    elif choice == "2":
        personality = "evil"
    elif choice == "3":
        personality = "hacker"
    else:
        print("Invalid choice, keeping previous personality.")

    print("Personality set to:", personality)
    print("------------------------------------------------------------------------------------")

def ShowAchievements():
    print()
    print("------------------------------------------------------------------------------------")
    print("Your achievements:")
    if not achievements:
        print("No achievements unlocked yet.")
    else:
        for a in achievements:
            print("-", a)
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
                print("5. try the age scanner (write 'age scanner' or '5')")
                print("7. change AI personality (write 'change personality' or '7')")
                print("8. view achievements (write 'achievements' or '8')")
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
                elif choise_from_options == "gaming news" or choise_from_options == "6":
                    GamingNews()
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

                elif choise_from_options == "change personality" or choise_from_options == "7":
                    ChangePersonality()
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


                elif choise_from_options == "achievements" or choise_from_options == "8":
                    ShowAchievements()
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
