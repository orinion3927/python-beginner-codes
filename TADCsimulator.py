import random
import time

# --- הגדרות צבעים ודמויות ---

COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "PURPLE": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "PINK": "\033[38;5;206m",
    "ORANGE": "\033[38;5;208m",
    "GRAY": "\033[90m",
    "RESET": "\033[0m"
}


CHARACTERS = {
    "CAINE": COLORS["RED"],
    "YOU": COLORS["GREEN"],
    "JAX": COLORS["PURPLE"],
    "POMNI": COLORS["BLUE"],
    "RAGATHA": COLORS["CYAN"],
    "KINGER": COLORS["YELLOW"],
    "ZOOBLE": COLORS["ORANGE"],
    "GANGLE": COLORS["PINK"]
}

# --- פונקציות עזר ---

def type_text(text, delay=0.05):
    parts = text.split(": ", 1)
    
    if len(parts) == 2:
        speaker = parts[0]
        dialogue = parts[1]
        
        if speaker in CHARACTERS:
            color = CHARACTERS[speaker]
            print(f"{color}{speaker}:{COLORS['RESET']} ", end="")
            
            for char in dialogue:
                print(char, end="", flush=True)
                time.sleep(delay)
            print()
            return
            
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def PickName():
    while True:
        mName = ["Kinger", "Jax", "Kaufmo"]
        fName = ["Pomni", "Ribbit", "Ragatha", "Zooble", "Gangle"]

        print(f"{COLORS['CYAN']}SYSTEM:{COLORS['RESET']} ", end="")
        gender = input("Male or Female? ").lower()

        if gender == "male":
            print("Randomizing Name...")
            time.sleep(0.9)
            chosen = random.choice(mName)
            print(f"Chosen name: {COLORS['YELLOW']}{chosen}{COLORS['RESET']}")
            return chosen

        elif gender == "female":
            print("Randomizing Name...")
            time.sleep(0.9)
            chosen = random.choice(fName)
            print(f"Chosen name: {COLORS['YELLOW']}{chosen}{COLORS['RESET']}")
            return chosen

        else:
            time.sleep(0.25)
            print(f"{COLORS['RED']}Invalid input{COLORS['RESET']}")

def LoadingScreen():
    time.sleep(0.75)
    lines = [
        "[BOOTING...]",
        "",
        "Loading system files... [OK]",
        "Connecting to C&A_network... [OK]",
        "",
        "> run protocol.exe",
        "> scanning...",
        "> scanning...",
        "",
        f"{COLORS['YELLOW']}WARNING: unknown file detected{COLORS['RESET']}",
        "",
        "> open file_███.log",
        "",
        "[LOG]",
        "subject active",
        "subject aware",
        "subject watching",
        "",
        "> attempting delete...",
        f"{COLORS['RED']}ACCESS DENIED{COLORS['RESET']}",
        "",
        "> ...",
        "",
        "Loading ended",
        "> _"
    ]

    for line in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.002)
        print()
        time.sleep(0.1)


name = PickName()
LoadingScreen()

time.sleep(1)
print("\n\n")

Caine1Speaks = [
    "Hello!",
    "My name is Caine,",
    "CAINE: and Welcome to the Amazing Digital Circus!!",
    "CAINE: And your name?"
]

for line in Caine1Speaks:
    type_text(line)
    time.sleep(0.2)

time.sleep(0.5)
print("\n")

User1speaks = [
    "YOU: W-what? Who are you? Where am I?",
    "YOU: And W-WHY CAN'T I REMEMBER MY NAME?"
]

for line in User1speaks:
    type_text(line)
    time.sleep(0.2)

time.sleep(0.5)
print("\n")

caine2Speaks = [
    "CAINE: Yeah, no one can remember his name, after entering the circus, because of that one of the things that I don't have control over is... your mind,",
    f"CAINE: But don't worry, we already got a name for ya, {COLORS['YELLOW']}{name}{COLORS['RESET']}!",
    f"CAINE: So, {name}, wanna meet the others?"
]

for line in caine2Speaks:
    type_text(line)
    time.sleep(0.2)

time.sleep(0.5)
print("\n")

User2speaks = [
    f"YOU: Ugh... no way this is real, I must be dreaming or something,"
]

for line in User2speaks:
    type_text(line)
    time.sleep(0.2)

time.sleep(0.5)
print("\n")

caine3Speaks = [
    f"CAINE: Oh, you're not dreaming, and this is very real, but I understand that you don't believe me, well let me show you the others.",
    f"CAINE: Come everyone! a new one has joined us."
]

for line in caine3Speaks:
    type_text(line)
    time.sleep(0.2)

time.sleep(0.5)
print("\n")

OthersSpeaks1 = [
    "JAX: Great, another one. just what we needed.",
    f"RAGATHA: Welcome {name}! We're all a little confused at first, but you'll fit right in!",
    "GANGLE: Hi! im Gangle",
    "KINGER: oh, hi there!"
]

for line in OthersSpeaks1:
    if line.startswith(f"{name.upper()}:"):
        continue
        
    type_text(line)
    time.sleep(0.4)

time.sleep(0.5)
print("\n")

def main_game_hub():
    actions_taken = 0 
    
    available_characters = ["JAX", "POMNI", "RAGATHA", "KINGER", "ZOOBLE", "GANGLE"]
    

    if name.upper() in available_characters:
        available_characters.remove(name.upper())

    while True:
        if actions_taken >= 3:
            start_adventure()
            actions_taken = 0 
            continue 

        print(f"\n{COLORS['CYAN']}--- DIGITAL CIRCUS HUB ---{COLORS['RESET']}")
        print("What do you want to do?")
        print("1. Talk to someone")
        print("2. Look around")
        print("3. Do nothing and wait")
        
        choice = input("\nEnter your choice (1-3): ")
        print("\n")

        if choice == "1":
            print(f"{COLORS['CYAN']}Who do you want to talk to?{COLORS['RESET']}")
            for i, char in enumerate(available_characters, 1):
                print(f"{i}. {char}")
            
            char_choice = input("\nChoose a character number: ")
            
            if char_choice.isdigit() and 1 <= int(char_choice) <= len(available_characters):
                chosen_char = available_characters[int(char_choice) - 1]
                trigger_chat(chosen_char)
                actions_taken += 1
            else:
                print("Invalid choice!")
                
        elif choice == "2":
            type_text(f"YOU: You look around the tent. Everything looks colorful but terrifyingly artificial.")
            actions_taken += 0.5
            
        elif choice == "3":
            type_text(f"YOU: You just sit there, staring at the digital void.")
            actions_taken += 1
        else:
            print("Caine stares at you... that's not an option!")

def trigger_chat(character):
    if character == "JAX":
        type_text("JAX: What do you want, newbie? I'm busy doing... nothing. Go away.")
        type_text("YOU: Wow, you're as charming as they say.")
    elif character == "RAGATHA":
        type_text("RAGATHA: Hey! Just making sure you're doing okay. It's a lot to take in at first.")
        type_text("YOU: Thanks, Ragatha. You're probably the only normal one here.")
    elif character == "POMNI":
        type_text("POMNI: (Whispering) Have you seen a door? An exit? I swear I saw one...")
        type_text("YOU: I'm looking too, Pomni. Don't worry.")
    elif character == "KINGER":
        type_text("KINGER: GAH! Oh, it's just you. You startled my insect collection! Oh wait, I don't have one here.")
    elif character == "ZOOBLE":
        type_text("ZOOBLE: I'm not in the mood to talk. My leg just fell off again.")
    elif character == "GANGLE":
        type_text("GANGLE: Jax stepped on my comedy mask again...")

def start_adventure():
    """פונקציה שמפעילה הרפתקה אקראית של קיין"""
    print(f"\n{COLORS['RED']}!!! WARNING !!!{COLORS['RESET']}")
    type_text("CAINE: INCOMING ADVENTURE! Gather around, my little digital friends!")
    

    adventures = [
        "The Mystery Of Mildenhall Manor!",
        "Gather the Gloinks!",
        "The Fast Food simulator!"
    ]
    
    current_adv = random.choice(adventures)
    
    type_text(f"CAINE: Today's adventure is going to be: {COLORS['YELLOW']}{current_adv}{COLORS['RESET']}!")
    type_text("CAINE: Let's go!!!")
    
    time.sleep(1)
    print(f"\n{COLORS['CYAN']}--- (Adventure placeholder - you completed the adventure!) ---{COLORS['RESET']}\n")
    type_text("CAINE: Wow! What a splendid adventure! Now back to the tent we go.")


main_game_hub()


# do not copy this code or other codes from the repository "python beginner codes". (in github)
