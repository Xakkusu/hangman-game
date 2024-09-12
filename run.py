import gspread
import random
# to get rid of empty string values in list
import functools
import os
import time
import pandas as pd
import colorama
from colorama import Fore, Back
from google.oauth2.service_account import Credentials
from hangman_figure import HANGMAN_FIGURES

SCOPE = [
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
    os.system('cls||clear')

    print(r"""
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗     ████████╗██╗  ██╗███████╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝     ╚══██╔══╝██║  ██║██╔════╝
        ███████║███████║██╔██╗ ██║██║  ███╗       ██║   ███████║█████╗
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║       ██║   ██╔══██║██╔══╝
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝       ██║   ██║  ██║███████╗
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝

        ███╗   ███╗ █████╗ ███╗   ██╗██╗
        ████╗ ████║██╔══██╗████╗  ██║██║
        ██╔████╔██║███████║██╔██╗ ██║██║
        ██║╚██╔╝██║██╔══██║██║╚██╗██║╚═╝
        ██║ ╚═╝ ██║██║  ██║██║ ╚████║██╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝
    """)
    time.sleep(0.15)
    print("Read through the menu and choose one option\n")
    print(f"    1. Start the game!\n    2. How to play?"
          + f"\n    3. Leaderboard\n    4. I am done!")
    valid_choice = False
    while valid_choice is False:
        user_choice = input("What is your choice: \n")
        valid_choice = validate_menu_choice(user_choice, ["1", "2", "3", "4"])
    if int(user_choice) == 1:
        category = choose_game_category()
        game_data = get_hangman_data(category)
        play_game(game_data)
    elif int(user_choice) == 2:
        get_game_instructions()
    elif int(user_choice) == 3:
        username_worksheet = SHEET.worksheet("leaderboard")
        update_leaderboard(username_worksheet)
    elif int(user_choice) == 4:
        time.sleep(2)
        print("\nbye bye...")
        exit()


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
        print(Fore.LIGHTRED_EX +
              f"\nInvalid data: {e}\n"
              + "You will be redirected to enter again...\n"
              + Fore.RESET)
        return False
    else:
        return True


def get_game_instructions():
    """
    Instructions are displayed as well as the option to
    return to the main menu
    """
    os.system('cls||clear')
    instructions = r"""
          ____________________________________________________
        /  \                                                   \.
       |    |                   How to play                     |.
        \_  |                                                   |.
            |  Guess the title of a movie one character by one  |.
            |  Each blank line stands for one character         |.
            |                                                   |.
            |  If correct the according blank space will be     |.
            |  filled in with the letter, you have 8 lives      |.
            |                                                   |.
            |  With each mistake the stick figure of a person   |.
            |  being hung will be drawn until the drawing of the|.
            |  hanged man is completed & the player lost.       |.
            |                                                   |.
            |  Try your best & save the man, or not...          |.
            |   ________________________________________________|___
            |  /                                                    /.
            \_/____________________________________________________/."""
    print(instructions + "\n")
    get_back_to_menu()


def choose_game_category():
    """
    Three different topics in which the game will
    be played are displayed, user can choose which
    game they want to play
    """
    valid_choice = False
    while valid_choice is False:
        print("\nOn which topic shall you be quized?\n")
        print("    1. Horror Movies\n    2. Thriller Movies\n"
              + "    3. Fantasy Movies\n")
        option = input("Enter the number: \n")
        valid_choice = validate_menu_choice(option, ["1", "2", "3"])
    if int(option) == 1:
        category = "horror"
    elif int(option) == 2:
        category = "thriller"
    elif int(option) == 3:
        category = "fantasy"
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
    movie names. information on how to get rid of empty
    string values in lists:
    https://sparkbyexamples.com/python/
    python-remove-empty-strings-from-list/
    """
    reduced_string_row = functools.reduce(lambda a, b: a+[b] if b else a,
                                          string_list, [])
    return reduced_string_row


def play_game(data):
    """
    Play the hangman game according to the string to be
    played with. With each wrong answer the hangman
    figure will be extended until the live run out.
    """
    os.system('cls||clear')

    print("Let's start\nGuess the following word:")
    blank_string = ""
    for i in data:
        blank_string += "_"
    print("     " + blank_string + "\n")

    guessed_list = []
    j = 0
    hangman_index = 0
    checked_word = blank_string
    while j < 8:
        valid_letter = False
        while valid_letter is False:
            guessed_character = input("Character guess: \n")
            guessed_character = guessed_character.lower()
            valid_letter = validate_letter(guessed_character, 1)
        if guessed_character in guessed_list:
            print(f"You already had this character before, your"
                  + f" enterd guesses: {guessed_list}\n")
            continue
        for i in data:
            is_correct = False
            if guessed_character in data:
                is_correct = True
            else:
                is_correct = False
        if is_correct is True:
            guessed_character, checked_word, j = guess_is_correct(
                                                 guessed_character,
                                                 data, checked_word, j)
        else:
            hangman_index = guess_is_wrong(guessed_character,
                                           HANGMAN_FIGURES, data,
                                           hangman_index, checked_word,
                                           j)
        guessed_list.append(guessed_character)
        print(f"Your guessed characters so far: {guessed_list}\n")
        j += 1


def guess_is_correct(guessed_character, data, checked_word, j):
    """
    Will use correct guess, check how often it is in title, and
    if it is the final correct guess
    For finding all instances of a character in data, this helped:
    https://stackoverflow.com/questions/44307988/
    find-all-occurrences-of-a-character-in-a-string
    """
    print(Fore.BLACK + Back.WHITE
          + f"\nCorrect! {guessed_character} is in the movie title"
          + Fore.RESET + Back.RESET + "\n")
    index_checked_word = [i for i,
                          character in enumerate(data)
                          if character == guessed_character]
    checked_word_list = list(checked_word)

    for i in index_checked_word:
        checked_word_list[i] = guessed_character.upper()
    checked_word = "".join(checked_word_list)
    print(checked_word)

    if checked_word == "".join(data).upper():
        os.system('cls||clear')

        print(Back.GREEN + Fore.BLACK
              + f"Congrats you figured it out!\nThe correct title"
              + f" is: {checked_word} and have {8-j} lives left\n"
              + Fore.RESET + Back.RESET)
        valid_choice = False
        while valid_choice is False:
            print(f"    1. Play again\n    2. Add"
                  + " lives left to the leaderboard\n    3. Exit\n")
            round_finished = input("What do you want to do now: \n")
            valid_choice = validate_menu_choice(round_finished,
                                                ["1", "2", "3"])
        if int(round_finished) == 1:
            os.system('cls||clear')
            try_again()
        elif int(round_finished) == 2:
            os.system('cls||clear')
            add_to_scorboard(j)
        elif int(round_finished) == 3:
            time.sleep(2)
            print("\nbye bye...")
            exit()
    j -= 1
    return guessed_character, checked_word, j


def guess_is_wrong(guessed_character, HANGMAN_FIGURES, data,
                   hangman_index, checked_word, j):
    """
    Will use wrong guess, check if it is the final correct
    guess or not & either and game or continue
    """
    if j == 7:
        print(Fore.BLUE
              + f"\nWrong! {guessed_character} is not in the movie title\n"
              + Fore.RESET)
        print("     " + HANGMAN_FIGURES[hangman_index])
        print(f"\nYour lives are up!\nThe man is dead...\nThe correct"
              + f" title was {"".join(data).upper()}\n")
        get_back_to_menu()
    else:
        print(Fore.BLUE + f"\nWrong! {guessed_character} is not"
              + f" in the movie title\n" + Fore.RESET)
        print("     " + HANGMAN_FIGURES[hangman_index])
        hangman_index += 1
        print(checked_word)
    return hangman_index


def try_again():
    """
    At the end of the game the user can restart the game
    from the choosing topic
    """
    os.system('cls||clear')
    category = choose_game_category()
    game_data = get_hangman_data(category)
    play_game(game_data)


def validate_letter(data, number):
    """
    Validate the choice of the user when entering a letter
    to guess the word of the hangman game as only one singular
    letter and no other character.
    """
    try:
        if not data.isalpha() or len(data) > number:
            raise ValueError(
                f"You entered {data}"
            )
    except ValueError as e:
        print(Fore.LIGHTRED_EX + f"\nInvalid data: {e}\nYou need"
              + f" to enter max {number} letter/s, try again\n" + Fore.RESET)
        return False
    else:
        return True


def add_to_scorboard(data):
    """
    User enters username and lives left will be added
    to the scoreboard.
    """
    lives_left = 8-data
    valid_username = False
    while valid_username is False:
        username = input("\nEnter a username (max. 15 characters,"
                         + " letters only): \n")
        username = username.lower()
        valid_username = validate_letter(username, 15)
    username_score_row = []
    username_score_row.append(username)
    username_score_row. append(lives_left)
    username_worksheet = SHEET.worksheet("leaderboard")
    username_worksheet.append_row(username_score_row)
    update_leaderboard(username_worksheet)


def update_leaderboard(worksheet):
    """
    Update the leaderboard according to the score
    and the name. Display it accordingly.
    Guidance: https://realpython.com/pandas-sort-python/,
    https://pandas.pydata.org/docs/reference/frame.html
    """
    os.system('cls||clear')
    user_data_all = worksheet.get_all_values()
    columns = user_data_all[0]
    user_data = user_data_all[1:]
    user_data_frame = pd.DataFrame(user_data, columns=columns)
    pd.set_option('display.colheader_justify', 'center')
    user_data_frame = user_data_frame.sort_values(
        by=['Lives Left', 'Name'],
        ascending=[False, True])
    user_data_frame = user_data_frame.reset_index(drop=True)
    user_data_frame.index = user_data_frame.index + 1

    print(Fore.GREEN + f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + Fore.RESET)
    print(user_data_frame)
    print(Fore.GREEN + f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + Fore.RESET)
    get_back_to_menu()


def get_back_to_menu():
    """
    When there is a non numeric menu the user can either
    go to the menu or exit the program.
    """
    print("To go back to the menu enter 'menu'.\nTo exit enter 'exit'\n")
    instruction_choice_user = input("Enter here: \n")
    while True:
        if instruction_choice_user.lower() == "menu":
            os.system('cls||clear')
            game_menu()
            break
        elif instruction_choice_user.lower() == "exit":
            time.sleep(2)
            print("\nbye bye...")
            exit()
        else:
            print(Fore.LIGHTRED_EX + "\nLook who the cat dragged in..."
                  + " Once again to go back to the menu enter 'menu'."
                  + "\nTo exit enter 'exit'\n"
                  + Fore.RESET)
            instruction_choice_user = input("Enter here: \n")


def main():
    """
    Runs the whole program by loading the game menu.
    """
    game_menu()


main()
