# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import random
# to get rid of empty string values in list
import functools
from google.oauth2.service_account import Credentials
from hangman_figure import HANGMAN_FIGURES

SCOPE =[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Hangman-game")

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
    valid_choice = False
    while valid_choice is False:
        user_choice = input("What is your choice: ")
        print(user_choice)
        valid_choice = validate_menu_choice(user_choice, ["1", "2", "3", "4"])
    if int(user_choice) == 1:
        category = choose_game_category()
        game_data = get_hangman_data(category)
        play_game(game_data)
    elif int(user_choice) == 2:
       get_game_instructions() 


def validate_menu_choice(data, list_to_validate):
    """
    Validate the choice of the user when entering a menu-number
    as an integer between 1 and 4. The try statement raises 
    an error if the entered data cannot be tranformed into an 
    integer or is not between 1 and 4
    """
    try:
        if data not in list_to_validate:
            raise ValueError(
                f"You entered {data}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\nYou will be redirected to the start of the menu...\n")
        return False
    else:
        return True


def get_game_instructions():
    """
    Instructions are displayed as well as the option to 
    return to the main menu
    """
    instructions = r"""
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
        |  You have 8 lives.                        |.
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
        \_/____________________________________________/."""
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

def choose_game_category():
    """
    Three different topics in which the game will
    be played are displayed, user can choose which
    game they want to play
    """
    print("On which topic shall you be quized?\n")
    print("1. Horror Movies\n2. Thriller Movies\n3. Fantasy Movies\n")
    option = input("Enter the number: ")
    while True:
        if int(option) == 1:
            #will be added once function is written
            category = "horror"
            break
        elif int(option) == 2:
            #will be added once function is written
            #print("load game data...")
            category = "thriller"
            break
        elif int(option) == 3:
            #will be added once function is written
            category = "fantasy"
            break
        else:
            print("Well well well.. Once again enter a number between 1 and 3\n")
            option = input("Enter here: ")
    return category


def get_hangman_data(topic):
    """
    Retrieve data from worksheet according to topic 
    that has been picked by the user. Will pick a 
    random string/movie-name from the chosen worksheet 
    and return the according list.
    """
    random_number = random.randrange(11)
    game_string = SHEET.worksheet(topic).get_all_values()
    game_string_row = game_string[random_number]
    final_game_string_row = reduce_empty_values(game_string_row)
    return final_game_string_row


def reduce_empty_values(string_list):
    """
    Get rid off empty string values in list of shorter
    movie names. information on how to get rid of empty string values in lists: 
    https://sparkbyexamples.com/python/python-remove-empty-strings-from-list/
    """
    reduced_string_row = functools.reduce(lambda a, b: a+[b] if b else a, string_list, [])
    return reduced_string_row


def play_game(data):
    """
    Play the hangman game according to the string to be
    played with. With each wrong answer the hangman
    figure will be extended until the live run out.
    """
    print("Let's start\nGuess the following word:")
    blank_string = ""
    # add blank _ for the word to guess according to its length
    for i in data:
        blank_string += "_"
    print("     " + blank_string +"\n")
    # check to see if character is in movie title
    j = 0
    hangman_index = 0
    checked_word = blank_string
    while j < 8:
        guessed_characer = input("Character guess: ")
        guessed_characer = guessed_characer.lower()
        for i in data:
            is_correct = False
            if guessed_characer in data:
                is_correct = True
            else: 
                is_correct = False
        if is_correct is True:
            print(f"Correct! {guessed_characer} is in the movie title\n")
            index_checked_word = int(data.index(guessed_characer))
            checked_word_list = list(checked_word)
            checked_word_list[index_checked_word] = guessed_characer.upper()
            checked_word = "".join(checked_word_list)
            print(checked_word)
            j-=1
        else: 
            print(f"Wrong! {guessed_characer} is not in the movie title\n")
            print("     " + HANGMAN_FIGURES[hangman_index])
            hangman_index += 1
            print(checked_word)
        j += 1
    print(data)
def try_again():
    """"""
def won_round():
    """"""
def end_game():
    """"""
def main ():
    """"""
    #game_menu()
    #get_hangman_data(category)
    #play_game(reduced_string_row)
game_menu()
#get_hangman_data("horror")

#play_game(["p","s","y","c","h","o"])
