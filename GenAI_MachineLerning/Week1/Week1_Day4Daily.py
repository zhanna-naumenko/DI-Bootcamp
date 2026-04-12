# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    print("Current menu:\n")
    for item, price in menu_dict.items():
        print(f"{item}: {price}₪")


def add_item(menu_dict):
    """Add a new drink to the menu."""
    user_drink = input("Enter new drink name: ")
    if user_drink not in menu_dict:
        drink_price = float(input("Enter price: "))
        if drink_price <=0:
            print("Invalid price.")
        else:
            menu_dict[user_drink] = drink_price
            print(f"{user_drink} added to the menu.")
    else:
        print("Drink already exists!")


def update_price(menu_dict):
    """Change the price of an existing drink."""
    update_drink = input("Which drink you want to update: ")
    if update_drink in menu_dict:
        new_price = float(input("Enter new price: "))
        menu_dict[update_drink] = new_price
        print("Price updated!")
    else:
        print("Drink doesn't exist!")


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    remove_drink = input("Which drink you want to remove: ")
    if remove_drink in menu_dict:
        del menu_dict[remove_drink]
    else:
        print("Drink doesn't exist!")



def show_options():
    """Print the available actions."""
    options_message = """What would you like to do?
                            1. Show menu
                            2. Add item
                            3. Update price
                            4. Delete item
                            5. Exit
                            6. Search the drink"""
    print(options_message)

def search_item(drink, menu_dict):
    """Check if a drink exists in the menu."""
    if drink in menu_dict:
        print(f"The price of {drink} is {menu_dict[drink]}₪")
    else:
        print("Drink doesn't exist in the menu!")


def run_coffee_shop():
    """Main loop of the program."""
    while True:
        show_options()
        user_choice = int(input("Enter your choice as a number: "))
        if user_choice == 1:
            show_menu(menu)
        elif user_choice == 2:
            add_item(menu)
        elif user_choice == 3:
            update_price(menu)
        elif user_choice == 4:
            delete_item(menu)
        elif user_choice == 6:
            search_drink = input("Which drink would you like to search: ")
            search_item(search_drink, menu)
        elif user_choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


# Start the program
run_coffee_shop()