# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def game_menu():
    """
    Function to display when first running program with the menu.
    Menu has options to either start the game, show instrucions, 
    show leaderboard or exit from program.
    """
    print("Hang the Man!")
    print("However you ended here really doesn't matter does it, it only matters what you want to do now\n")
    print("Read through the menu and chose one option")
    print(f"1. Start the game!\n2. How to play?\n3. Leaderboard\n4. I am done!\n")
    user_choice = input("What is your choice: ")
    print(user_choice)
    validate_menu_choice(user_choice)
    if int(user_choice) == 2:
       get_game_instructions() 


def validate_menu_choice(data):
    """
    Validate the choice of the user when entering a menu-number
    as an integer between 1 and 4. The try statement raises 
    an error if the entered data cannot be tranformed into an 
    integer or is not between 1 and 4
    """
    try:
        nmbr = int(data)
        if nmbr<=0 or nmbr>=5:
            raise ValueError(
                f"You entered {nmbr}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\nRemember your choice needs to be a number between 1 and 4.\nYou will be redirected to the start of the menu...\n")
        game_menu()


def get_game_instructions():
    """
    Instructions are displayed as well as the option to 
    return to the main menu
    """
    instructions = """
       ____________________________________________
     / \                                            \.
    |   |               How to play                 |.
     \_ |                                           |.
        |  Each blank line stands for a character   |.
        |  in a secret word.                        |.    
        |                                           |.
        |  Guess the letters for each line ony by   |.
        |  one.                                     |.
        |                                           |.
        |  If correct the according blank space     |.
        |  will be filled in with the letter.       |.
        |                                           |.
        |  You have 7 tries.                        |.
        |                                           |.
        |  With each mistake the stick figure of    |.
        |  a person being hung will be drawn until  |.
        |  the drawing of the hanged man is         |.
        |  completed & the player lost.             |.
        |                                           |.
        |  Try your best & save the man, or not...  |.    
        |                                           |.            
        |   ________________________________________|___
        |  /                                            /.
        \_/____________________________________________/.\n"""
    print(instructions)
    print("To go back to the menu enter 'menu'.\nTo exit enter 'exit'\n")
    instruction_choice_user = input("Enter here: ")
    while True:
        if instruction_choice_user.lower() == "menu":
            game_menu()
            break
        elif instruction_choice_user.lower() == "exit":
            #will be added once function is written
            break
        else:
            print("Look who the cat dragged in... Once again to go back to the menu enter 'menu'.\nTo exit enter 'exit'\n")
            instruction_choice_user = input("Enter here: ")

def go_to_main_menu():
    """"""
def choose_game_category():
    """"""
def start_game():
    """"""
def get_hangman_data(data):
    """"""
def try_gain():
    """"""
def won_round():
    """"""
def end_game():
    """"""
def main ():
    """"""
game_menu()
