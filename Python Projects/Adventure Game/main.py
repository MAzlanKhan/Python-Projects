inventory = []

locations = {
    "forest": "You are in a dark forest. You hear strange noises.",
    "cave": "You have entered a damp cave. It's very cold here.",
    "river": "You are standing by a river. The water is flowing quickly."
}
items = {
    "forest": "wooden stick",
    "cave": "glowing crystal",
    "river": "shiny stone"
}

print("Welcome to the Adventure Game!")
print("Type 'quit' to exit the game.\n")

while True:
    # Display available locations
    print("Available locations:", ", ".join(locations.keys()))
    
    # Ask the player where to go
    choice = input("Where would you like to go? ").lower().strip()
    
    if choice == "quit":
        print("Thanks for playing! Goodbye!")
        break
    elif choice in locations:
        print(f"\nYou moved to the {choice}.")
        print(locations[choice])

        if choice == "forest":
            print(f"You got {items['forest']}")
            item_choice = input("Do you want to Collect it (Yes/No): ").lower().strip()
            if item_choice == "yes":

                choice2 = input("Do you want to quite (type yes or no): ").lower().strip()
                if choice2 == "yes":
                    print(f"Goodbye! Your final inventory: {inventory}")
                    break
                elif choice2 == "no":
                    pass

                inventory.append(items['forest'])
                print(f'You have {inventory[0]} in your inventory')
                
            elif item_choice == "no":
                pass   

        elif choice == "cave":
            print(f"You got {items['cave']}")
            item_choice = input("Do you want to Collect it (Yes/No): ").lower().strip()
            if item_choice == "yes":
                choice2 = input("Do you want to quite (type yes or no): ").lower().strip()
                if choice2 == "yes":
                    print(f"Goodbye! Your final inventory: {inventory[0:]}")
                    break
                elif choice2 == "no":
                    pass

                inventory.append(items['cave'])
                print(f'You have {inventory[0:]} in your inventory')
            elif item_choice == "no":
                pass   

        elif choice == "river":
            print(f"You got {items['river']}")
            item_choice = input("Do you want to Collect it (Yes/No): ").lower().strip()
            if item_choice == "yes":

                choice2 = input("Do you want to quite (type yes or no): ").lower().strip()
                if choice2 == "yes":
                    print(f"Goodbye! Your final inventory: {inventory}")
                    break
                elif choice2 == "no":
                    pass

                inventory.append(items['river'])
                print(f'You have {inventory[0:]} in your inventory')
            elif item_choice == "no":
                pass   
        updated_locations = locations.pop(choice)

        if not locations:
            print("Do you want to quit the game or view inventory (type inventory/quit)")
            choice2 = input("Type Quit or Inventory: ").lower().strip()
            if choice2 == "quit":
                print(f"Goodbye! Your final inventory: {inventory}")
                break
            elif choice2 == "inventory":
                print(inventory)
    else:
        print("Invalid location. Please choose a valid location.")
