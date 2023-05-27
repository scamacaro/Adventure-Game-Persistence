"""
Sanyerlis Camacaro - CSC235 - Sancamac@uat.edu Assignment:
Read and Writing Files in Python.

"Adventure Game"

This code demonstrates how to:
Add a new function to write data to a text file.
Add a new function to read data to a text file.
Your read and writes should add something useful to your application,
not just demo how to read and write to and from a text file.

The Game functions demonstrates:

- `start_game` is the main function that starts and controls the game.
- `hall`, `kitchen`, `library`, `garden` and `basement` are functions for different game scenarios.
They all take a game state as an argument and return an updated game state. This way, they can affect the game
and pass on the results of their actions.
- `if __name__ == "__main__":` is a special construct that checks if the script is being run directly. If it is,
it starts the game by calling the `start_game` function.

Each scenario function prints out a description of the current location and asks for input. Depending on the input
,the function may change the game state (for example, change the location or set `has_treasure` to `True`).

This code will save the game state to save_game.txt in the same directory whenever the player chooses to save
the game. The game state will be saved in JSON format. The load_game function will load the game state from the same
file if it exists.

In the case when the player wants to load a game that doesn't exist. We catch
the FileNotFoundError and start a new game.
"""
import json


def save_game(game_state, file_name='save_game.txt'):
    """
    Function to save the current game state to a file.
    """
    with open(file_name, 'w') as f:
        json.dump(game_state, f)

    print("\nYour game has been saved successfully!")


def load_game(file_name='save_game.txt'):
    """
    Function to load a game state from a file.
    """
    try:
        with open(file_name, 'r') as f:
            game_state = json.load(f)

        print("\nYour game has been loaded successfully!")
        return game_state
    except FileNotFoundError:
        print("\nNo saved game found.")
        return None


def start_game():
    """
    The main function that starts the game. It uses other functions to control the flow of the game.
    """

    print("****** Welcome to the Adventure Game! ******")
    # Ask the user if they want to load a saved game
    load_choice = input("\nWould you like to load a saved game? (yes/no) ")
    if load_choice.lower() == 'yes':
        game_state = load_game()
        if game_state is None:
            print("\nStarting a new game.")
            game_state = {
                "location": "hall",
                "has_treasure": False
            }
    else:
        print("\nStarting a new game.")
        game_state = {
            "location": "hall",
            "has_treasure": False
        }

    # Game loop
    while not game_state["has_treasure"]:
        # Allow the player to save the game after each move
        save_choice = input("\nWould you like to save your game? (yes/no) ")
        if save_choice.lower() == 'yes':
            save_game(game_state)

        if game_state["location"] == "hall":
            game_state = hall(game_state)
        elif game_state["location"] == "kitchen":
            game_state = kitchen(game_state)
        elif game_state["location"] == "library":
            game_state = library(game_state)
        elif game_state["location"] == "garden":
            game_state = garden(game_state)
        elif game_state["location"] == "basement":
            game_state = basement(game_state)

    print("Congratulations, you've found the treasure and won the game!")


def hall(game_state):
    """
    Function for the hall scenario. The player can go enter different doors.
    """
    print("\nYou're in the hall. There are four doors. These doors leads to the kitchen, library, garden and basement.")
    choice = input("Where do you want to go? (kitchen/library/garden/basement) ")

    if choice == "kitchen":
        game_state["location"] = "kitchen"
    elif choice == "library":
        game_state["location"] = "library"
    elif choice == "garden":
        game_state["location"] = "garden"
    elif choice == "basement":
        game_state["location"] = "basement"

    return game_state


def kitchen(game_state):
    """
    Function for the kitchen scenario. The player can return to the hall or open the fridge.
    The treasure is in the fridge.
    """
    print("\nYou're in the kitchen. You can see a fridge and a door leading back to the hall.")
    choice = input("What do you want to do? (open fridge/go back) ")

    if choice == "open fridge":
        game_state["has_treasure"] = True
    elif choice == "go back":
        game_state["location"] = "hall"

    return game_state


def library(game_state):
    """
    Function for the library scenario. The player can return to the hall or read a book. Reading a book does nothing.
    """
    print("\nYou're in the library. There are many books on the shelves and a door leading back to the hall.")
    choice = input("What do you want to do? (read book/go back) ")

    if choice == "read book":
        print("You pick up a book and start reading. It's interesting but doesn't help you find the treasure.")
    elif choice == "go back":
        game_state["location"] = "hall"

    return game_state


def garden(game_state):
    """
    Function for the garden scenario. The player can return to the hall or water the plants.
    Watering the plants does nothing.
    """
    print("\nYou're in the garden. There are many beautiful plants and a door leading back to the hall.")
    choice = input("What do you want to do? (water plants/go back) ")

    if choice == "water plants":
        print("You water the plants. They seem to appreciate it, but it doesn't help you find the treasure.")
    elif choice == "go back":
        game_state["location"] = "hall"

    return game_state


def basement(game_state):
    """
    Function for the basement scenario. The player can return to the hall or search the boxes.
    Searching the boxes might reveal the treasure.
    """
    print("\nYou're in the basement. It's dark and there are many boxes around.")
    print("There's also a staircase leading back to the hall.")
    choice = input("What do you want to do? (search boxes/go back) ")

    if choice == "search boxes":
        print("You found nothing in the boxes!")
    elif choice == "go back":
        game_state["location"] = "hall"

    return game_state


if __name__ == "__main__":
    start_game()
