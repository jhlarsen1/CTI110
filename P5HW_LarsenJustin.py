import random

def create_character(name=None, auto_select=False):
    """
    Creates a character with attributes determined by user choice or auto-generation.
    Parameters:
    - name: Predefined name for the character (e.g., 'Dice King' for auto-generation).
    - auto_select: If True, skips user input and randomly selects a number between 1 and 3.
    """
    if not name:
        name = input("Enter the character's name: ")

    if auto_select:
        choice = random.randint(1, 3)  # Auto-select a number for Dice King
    else:
        print("\nPick a number between 1 and 3:")
        print("1. Option 1 (Randomized stats)")
        print("2. Option 2 (Randomized stats)")
        print("3. Option 3 (Randomized stats)")

        while True:
            try:
                choice = int(input("Your choice (1-3): "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print("Please choose a valid number (1, 2, or 3).")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Generate random values for health, attack, and defense
    health = random.randint(140, 300)
    attack = random.randint(1, 70)
    defense = random.randint(1, 50)

    # Create and return the character dictionary
    return {
        "name": name,
        "health": health,
        "attack": attack,
        "defense": defense
    }

def game_structure():
    characters = []  # Store all characters created in the game

    print("Welcome to Dice Fighterz!")
    print("Are you ready to try your luck?")
    print("")
    print("This game is NOT intended for gambling and was instead made for friendly wagers.")
    print("")
    print("")
    print("")
    print("1. One-player mode")
    print("2. Two-player mode")

    # Choose game mode
    while True:
        try:
            mode = int(input("Choose a mode (1 or 2): "))
            if mode in [1, 2]:
                break
            else:
                print("Please choose a valid mode (1 or 2).")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    # Game setup
    if mode == 1:  # One-player mode
        print("\nPlayer, create your character:")
        player_character = create_character()  # User-created character
        characters.append(player_character)

        print("\nCreating Dice King (opponent):")
        dice_king = create_character(name="Dice King", auto_select=True)  # Auto-generated Dice King
        characters.append(dice_king)

    elif mode == 2:  # Two-player mode
        print("\nPlayer 1, create your character:")
        player1 = create_character()  # Player 1's character
        characters.append(player1)

        print("\nPlayer 2, create your character:")
        player2 = create_character()  # Player 2's character
        characters.append(player2)

    # Display all characters created
    print("\nAll characters have been created!")
    display_characters(characters)

    return characters

def display_characters(character_list):
    """Displays all characters in the game."""
    if not character_list:
        print("No characters have been created yet.")
        return
    for i, character in enumerate(character_list, start=1):
        print(f"\nCharacter {i}:")
        for key, value in character.items():
            print(f"  {key.capitalize()}: {value}")

#create a funtion for battle
def battle(character1, character2):
    """
    Simulates a battle between two characters.
    Parameters:
    - character1: Dictionary representing the first character.
    - character2: Dictionary representing the second character.
    """
    print("\nI am now selecting at random which character will attack first!")
    attacker, defender = random.choice([(character1, character2), (character2, character1)])
    print(f"{attacker['name']} will be attacking first!")
    makeMove = input("Enter any value to initiate attack: ")
    while makeMove =="":
        print("Are you ready yet? Enter a value when asked again if you want the round to begin.")
        makeMove = input("Enter any value to initiate attack: ")
    else:
        while character1['health'] > 0 and character2['health'] > 0:
            # Determine attack value
            attack_value = attacker['attack'] if defender['defense'] > 0 else random.randint(0, attacker['attack'])

            print(f"\n{attacker['name']} attacks {defender['name']} with {attack_value} damage!")

            # Apply damage to defense first
            if defender['defense'] > 0:
                if attack_value <= defender['defense']:
                    defender['defense'] -= attack_value
                    print(f"{defender['name']}'s defense reduced to {defender['defense']}.")
                else:
                    overflow_damage = attack_value - defender['defense']
                    defender['defense'] = 0
                    defender['health'] -= overflow_damage
                    print(f"{defender['name']}'s defense is depleted! {overflow_damage} damage dealt to health.")
                    print("")
            else:
                # Apply damage directly to health
                defender['health'] -= attack_value
                print(f"{defender['name']}'s health reduced to {defender['health']}.")
                print("")
                statBoost = int(input("Would you like to boost your attack or defense for next round?(Enter 1 for Attack and 2 for defense)"))
                while statBoost < 3 and statBoost > 0:
                    if statBoost == 1:
                        statBoost = random.randint(0,40)
                        print(f"Your attack stat will now by increased by: {statBoost}!")
                        print("")
                        attacker['attack'] = int(attacker['attack']+statBoost)
                        print(f"Your new attack stat is {attacker['attack']}")
                    elif statBoost == 2:
                        statBoost = random.randint(0,40)
                        print(f"Your defense stat will now by increased by: {statBoost}!")
                        print("")
                        attacker['defense'] = int(attacker['defense']+statBoost)
                        print(f"Your new defense stat is {attacker['defense']}")
                    else:
                        print("Wow! If you cant read and follow instructions you cant play this game! Sorry...... Bye bye")

            # Check if the defender is defeated
            if defender['health'] <= 0:
                print("")
                print(f"\n{defender['name']} has been defeated! {attacker['name']} wins the battle!")
                break

            # Switch attacker and defender for the next turn
            attacker, defender = defender, attacker

def main():
    """Main function to manage the game."""
    restart = "1"
    while restart == "1":
        charList = game_structure()
        character1 = charList[0]
        character2 = charList[1]
        battle(character1, character2)
        print(character1)
        print(character2)
        print("")
        print("")
        restart = input("Would you like to try your luck again?(Enter 1 for YES and 2 for NO) ")
    else:
        
    
    # Game end
        print("")
        print("")
        print("\nThank you for playing Dice Fighterz!")

# Start the game
if __name__ == "__main__":
    main()
