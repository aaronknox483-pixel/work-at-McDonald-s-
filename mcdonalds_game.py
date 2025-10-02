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
        print("The manager role costs 100 rubux to play.")
        pay = input("Type 'pay' to spend 100 rubux and play as manager, or anything else to go back: ")
        if pay.lower() == 'pay':
            play_manager()
        else:
            print("Returning to role selection.")
            main()
    else:
        print("Invalid choice. Please restart the game.")

def play_janitor():
    print("\nYou are the Janitor!")
    print("Your tasks: Clean the lobby, take out trash, mop the floor.")
    import threading
    import sys
    import time
    tasks = ["Clean the lobby", "Take out trash", "Mop the floor"]
    def timed_input(prompt, timeout):
        print(prompt)
        result = [None]
        def get_input():
            result[0] = sys.stdin.readline().strip()
        thread = threading.Thread(target=get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print("Time's up!")
            return None
        return result[0]
    for task in tasks:
        action = timed_input(f"Type 'done' within 10 seconds to finish: {task}: ", 10)
        if action and action.lower() == 'done':
            print(f"{task} completed!")
        else:
            print(f"You missed {task}.")
    print("All janitor tasks finished! Shift complete!")

def play_cook():
    print("\nYou are the Cook!")
    print("Your tasks: Grill burgers, fry fries, assemble orders.")
    import threading
    import sys
    import time
    tasks = ["Grill burgers", "Fry fries", "Assemble orders"]
    def timed_input(prompt, timeout):
        print(prompt)
        result = [None]
        def get_input():
            result[0] = sys.stdin.readline().strip()
        thread = threading.Thread(target=get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print("Time's up!")
            return None
        return result[0]
    for task in tasks:
        action = timed_input(f"Type 'done' within 10 seconds to finish: {task}: ", 10)
        if action and action.lower() == 'done':
            print(f"{task} completed!")
        else:
            print(f"You missed {task}.")
    print("All cook tasks finished! Shift complete!")

def play_manager():
    print("\nYou are the Manager!")
    print("Your tasks: Supervise staff, handle complaints, manage inventory.")
    import threading
    import sys
    import time
    tasks = ["Supervise staff", "Handle complaints", "Manage inventory"]
    def timed_input(prompt, timeout):
        print(prompt)
        result = [None]
        def get_input():
            result[0] = sys.stdin.readline().strip()
        thread = threading.Thread(target=get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print("Time's up!")
            return None
        return result[0]
    completed = 0
    for task in tasks:
        action = timed_input(f"Type 'done' within 10 seconds to finish: {task}: ", 10)
        if action and action.lower() == 'done':
            print(f"{task} completed!")
            completed += 1
        else:
            print(f"You missed {task}.")
    if completed == len(tasks):
        print("All manager tasks finished! You earned 100 rubux!")
    else:
        print("Shift complete! No bonus earned.")

if __name__ == "__main__":
    main()
