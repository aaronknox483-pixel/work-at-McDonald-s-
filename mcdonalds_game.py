"""
McDonald's Text-Based Game
Choose your role: Janitor, Cook, or Manager
"""

def main():
    print("Welcome to McDonald's!")
    print("Choose your role:")
    print("1. Janitor")
    print("2. Cook")
    print("3. Manager")
    role = input("Enter the number of your role: ")
    if role == '1':
        play_janitor()
    elif role == '2':
        play_cook()
    elif role == '3':
        play_manager()
    else:
        print("Invalid choice. Please restart the game.")

def play_janitor():
    print("\nYou are the Janitor!")
    print("Your tasks: Clean the lobby, take out trash, mop the floor.")
    tasks = ["Clean the lobby", "Take out trash", "Mop the floor"]
    for task in tasks:
        action = input(f"Type 'done' when you finish: {task}: ")
        if action.lower() == 'done':
            print(f"{task} completed!")
        else:
            print(f"You skipped {task}.")
    print("All janitor tasks finished! Shift complete!")

def play_cook():
    print("\nYou are the Cook!")
    print("Your tasks: Grill burgers, fry fries, assemble orders.")
    tasks = ["Grill burgers", "Fry fries", "Assemble orders"]
    for task in tasks:
        action = input(f"Type 'done' when you finish: {task}: ")
        if action.lower() == 'done':
            print(f"{task} completed!")
        else:
            print(f"You skipped {task}.")
    print("All cook tasks finished! Shift complete!")

def play_manager():
    print("\nYou are the Manager!")
    print("Your tasks: Supervise staff, handle complaints, manage inventory.")
    tasks = ["Supervise staff", "Handle complaints", "Manage inventory"]
    for task in tasks:
        action = input(f"Type 'done' when you finish: {task}: ")
        if action.lower() == 'done':
            print(f"{task} completed!")
        else:
            print(f"You skipped {task}.")
    print("All manager tasks finished! Shift complete!")

if __name__ == "__main__":
    main()
