import psycopg2
from W3D4_ExerciseXP1_menu_item import MenuItem

conn = psycopg2.connect(database="PyCharm", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()


view_an_item = 'V'
add_an_item = 'A'
delete_an_item = 'D'
update_an_item = 'U'
show_menu = 'S'
show_menu_exit = 'E'


def show_user_menu():
    print("Hello! You are in the program menu. Please select one of the option: ")
    print("View an item type : V")
    print("Add an item type : A")
    print("Delete an item type : D")
    print("Update an item type : U")
    print("Show the menu type : S")
    print("To exit type: E")

def add_item_to_menu():
    user_add_item = input("Please enter item you want to add to menu: ")
    user_add_price = int(input("Please enter price: "))
    item = MenuItem(user_add_item, user_add_price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    user_name_remove = input("Enter the name of the item to remove: ")
    item = MenuItem(user_name_remove)
    try:
        item.delete(user_name_remove)
        print("Item was deleted successfully.")
    except:
        print("Error: Item not found.")

def update_item_from_menu():
    name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name for the item: ")
    new_price = float(input("Enter the new price for the item: "))
    item = MenuItem(name)
    try:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    except:
        print("Error: Item not found.")

def all_items():
    try:
        cursor.execute("SELECT item_name FROM Menu_Items")
        items = cursor.fetchall()
        return items
    finally:
        cursor.close()
        conn.close()

def show_restaurant_menu():
    items = all_items()
    print("Restaurant Menu:")
    for item in items:
        print(f"{item[1]} - ${item[2]}")

def get_by_name(name):
    try:
        cursor.execute("SELECT item_name FROM Menu_Items WHERE item_name = %s", (name,))
        item = cursor.fetchone()
        if item:
            return ''.join(item)
        else:
            return None
    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()
        if choice == "V":
            name = (input("Enter the name of the item to view: ")).upper()
            item = get_by_name(name)
            if item:
                print(f"Name: {item}")
            else:
                print("Item not found.")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            print("Exiting program...")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




