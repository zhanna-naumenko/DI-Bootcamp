from game import Game

def get_user_menu_choice():
    print("Welcome to the Rock Paper Scissors game!")
    print("To a new game input: n\nTo Show scores input: s\nQuit input: q")
    # return input("Enter your choice: ").lower()
    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice in ["n", "s", "q"]:
            return user_choice
        print("Invalid choice. Please try again.")

def print_results(results):
    print(f"Results:\nWins: {results['win']}\nLosses: {results['loss']}\nDraws: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
       user_choice = get_user_menu_choice()
       if user_choice == "n":
           user_name = input("Enter your name: ")
           new_game = Game(user_name)
           result = new_game.play()
           results[result] += 1

       elif user_choice == "s":
           print_results(results)
       elif user_choice == "q":
           print("Thank you for playing! Goodbye!")
           break


if __name__ == "__main__":
    main()