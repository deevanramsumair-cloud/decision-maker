# Decision Maker

# Import Python Modules
import random
import time

# Display the Program Title and Introduction
def print_banner():

    print("THE ELIMINATOR")
    print("Add your choices. One will win.")

# Collect User Info
def get_choices():
    choices = []
    print("Enter your choices one by one.")
    print("Press Enter with no text when done.")
    print("(Minimum 2 choices required)")

# Infinite Loop to Keep Asking for Choices
    while True:
        choice = input(f"Enter choice {len(choices) + 1}: ").strip()
        if choice == "":
            if len(choices) < 2:
                print("Please enter at least 2 choices!")
            else:
                break
        else:
            choices.append(choice)
            print(f"✓ '{choice}' added!")
    
    return choices

# Display Current Choices
def show_choices(choices):
    print("Current choices:")
    for i, choice in enumerate(choices, 1):
        print(f"  {i}. {choice}")

# Eliminate Randomly 1 Choice
def eliminate_one(choices):
    eliminated = random.choice(choices)
    choices.remove(eliminated)
    return eliminated

# Main Elimination Function, Continue Eliminating Until 1 is left
def run_eliminator(choices):
    print("ELIMINATION BEGINS!")
    time.sleep(1)

    while len(choices) > 1:
        show_choices(choices)
        input("Press Enter to eliminate someone...")
        
# Dramatic Animation Effect
        print("🎲 Spinning...")
        time.sleep(1)
        print("🎲 Spinning...")
        time.sleep(1)
        print("🎲 Picking...")
        time.sleep(1)
        
# Randomly Eliminates One Choice
        eliminated = eliminate_one(choices)
        print(f"❌ ELIMINATED: {eliminated}!")
        time.sleep(1)

# Final Winner Announcement
    print(" WE HAVE A WINNER! ")
    print(f"🏆 THE WINNER IS: {choices[0].upper()}!")

# Display Main Menu Option
def show_menu():

    print(" THE ELIMINATOR ")

    print("1. Start new elimination")
    print("2. Quick demo")
    print("3. Quit")

# Function to Run a Demo to see how it works;
def run_demo():
    demo_choices = ["Pizza", "Burger", "Sushi", "Doubles", "Pasta"]
    print("Demo choices: Pizza, Burger, Sushi, Doubles, Pasta")
    run_eliminator(demo_choices)

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        print_banner()
        choices = get_choices()
        run_eliminator(choices)

    elif choice == "2":
        run_demo()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
