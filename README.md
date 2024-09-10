# Hangman Game
This Hangman game is a simple word-guessing game according to the general established rules of a hangman game. The user can choose words from different types of movie titles. They than have to to guess a random title one character at the time. The user has 8 lives, correlating with a stick figure image which will have more sticks "drawn" onto the more lives are lost due to wrong guesses. The user either guesses the word correctly or, when there are no more lives left, looses and the full figure of the hanged man is shown.

Depending on how much knowdledge the user has about movie title the user will have it easiert or harder in this game. However this puzzle is meant to improve the user's critical thinking and problem solving abilities before they run out of lives.

There are visual clues as each line of the word to guess represents one character and the correct guessed ones will appear on the according position in the word. Moreover, the wrong guesses will be shown in a list and do not count as a second live once they have been entered.

Interested? Then check it out here: [Hang the man!](https://hang-the-man-3409a28c593c.herokuapp.com/)

![Hang the man! Am I Responsive Image](docs/am-i-responsive-hangman.png)

## Contents
- [HOW TO PLAY](#how-to-play)
- [SITE OWNER GOALS](#site-owner-goals)
- [USER EXPERIENCE (UX)](#user-experience-ux)
- [FLOW CHART / DECISION TREE](#flow-chart--decision-tree)
- [FEATURES](#features)
- [DATA MODEL](#data-model)
- [TESTING](#testing)
    - [User Stories Testing](#user-stories-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Known Bugs](#known-bugs)
- [TECHNOLOGIES USED](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs used](#frameworks-libraries-and-programs-used)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)
    - [Media](#media)
    - [Resources](#resources)
- [ACKNOWLEDGEMENTS](#acknowledgements)


## HOW TO PLAY
- The user can choose to play, see instructions, see leaderboard or exit the program
    - After viewing the instructions or leaderboard the user can return to the menu or exit the program
- The user can choose to guess movie titles from the following categories: Horror, Thriller & Fantasy
- The user has 8 lives, hence 8 chances, to guess the word
- A hint is given at the beginning of the game as blank lines for each letter in the word
- The user has to guess one character at the time
    - If the character is correct the hint will update with the location of the correct character and the user can guess again
    - If the character is wrong the a stick figure will appear with a "wrong guess"-statement and the user can guess again
    - The stick figure will continue to grow into a hanged man the more wrong guesses were placed
- When all characters are guessed a winning statement is shown and the user can decide on the following:
    - Playing the game again
    - Saving a username and score to the leaderboard
    - exit the programm
- When all lives are up a loosing statement is shown and the user can decide to return to the menu or exit the program


## SITE OWNER GOALS
- to provide the user with a fun short word-guessing game with different categories to choose from
- to prvide the user a a quick and challenging activity
- to prvide the user with a simple program that is easy to navigate through
- to provide the user with the option to save their score with their username, competing with other users for the first place


## USER EXPERIENCE (UX)
#### First Time User Goals
- I want to take a a word guessing quiz - hangman
- I want to understand the the program, its structure and how to play the game
- I want the quiz to be easy to use and navigate
- I want to be able to be tested on different categories
- I want to see how well I am doing during the game
- I want to take the quiz whenever, wherever


#### Returning User Goals
- I want to be able to be tested on different categories
- I want to be able to restart the game without reloading the page
- I want to get different words to be tested on when retaking the game

#### Frequent User Goals
- I want to be able to be tested on different categories
- I want to be able to restart the game without reloading the page
- I want to get different words to be tested on when retaking the game
- I want to save my best scores to a leaderboard to compete with other users


## FLOW CHART / DECISION TREE
![Hang the man! Flow Chart Image](docs/lucid-chart.png)

The flow chart was created with [Lucid Chart](https://www.lucidchart.com/pages/) to help easily visualizing the flow of the program while passing each step. Like most decision trees some steps repeat themselves while other are final or starting points.

I wanted to show that winning and lossing the game isn't really an ending step as the user can still decide what to do afterwwards. This way the user has a lot of freedom and is not forced by the program on which route to take.

### Final Look
Final Look of the website/program before any input by the user has been entered:
<img src="docs/hang-the-man-final-look.png" alt="Website with Python terminal at the beginning of the programm">


## FEATURES
### Game Title
![Game Title Images](docs/features/title-feature.png)
- An inviting title stlye was used so the user will not be too appalled by the basic black/white terminal design. Especially if the user has no knowledge of terminals they would still know that this is no error screen or that their pc didn't just crash.
 - The style was created by using [ASCII text](https://www.asciiart.eu/text-to-ascii-art) and applying one of their fonts on my title.

### Game Menu
![Game Menu Image](docs/features/game-menu-feature.png)
- The Game menu is made up of 4 options: Start the game, How to Play, Leaderboard and I am done.
- This simple set-up is common for most smaller games and quizzes, therefore most useres should be familiar with its structure.

#### Game Menu - Input Validation
![Game Menu Input Validation Image](docs/features/menu-input-validation-feature.png)
- If the user does not enter a number between 1 and 4 an Error Message will appear. This message repeats the input from the user and states that they will be given the chance to enter an input again.
- This message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

### How To Play?
![How To Play Section Image](docs/features/how-to-play-feature.png)
- If the user chooses option 2, the terminal will be cleared and the instructions with how this game will be played are displayed.
- To, again, leave a more visually pleasing for the user the instructions are bordered by [ASCII-Art](https://www.asciiart.eu/art-and-design/borders) that should look familiar to a scroll.
- Below the instructions the user can once again choose to return to the main menu or exit the program.

#### How To Play - Input Validation
![How To Play Input Validation Image](docs/features/htp-input-validation-feature.png)
- Unlike the above validator this validator takes full words as input (lower- or uppercase are fine) and returns an error message if the wrong data was entered.
- This was simply done to show that I am able to code various types of input validations.
- The error message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

### Leaderboard
![Leaderboard Section Image](docs/features/leaderboard-feature.png)
- If the user chooses option 3, the terminal will be cleared and the leaderboard will be displayed.
- The leaderboard is ordered according to how many lives are left and then alphabetically according to the username.
- This was done by using the open source data analysis toolkit pandas. 
- The leaderboard spreadsheet is accessed and used to keep the data of the user (username and score) via an API.
- Below the leaderboard the user can once again choose to return to the main menu or exit the program.

#### How To Play - Input Validation
![Leaderboard Input Validation Image](docs/features/leaderboard-input-validation-feature.png)
- The exact same as the How To Play - Input Validation

### Hangman Categories
![Categories Section Image](docs/features/categories-feature.png)
- If the user chooses option 1 three category options will be displayed for the user to choose from.

#### Categories- Input Validation
![Categories Input Validation Image](docs/features/categories-input-validation-feature.png)
- If the user does not enter a number between 1 and 3 an Error Message will appear. This message repeats the input from the user and states that they will be given the chance to enter an input again.
- This message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

### Game Section
![Game Section Image](docs/features/game-feature.png)
- No matter which category the user chooses, the terminal will be cleared and a hint of lines appears.

![Catgeory Worksheet Image](docs/features/game-categories-worksheet-feature.png)
- When the user enters the catageory Google Sheets were used to access the according sheet to the chosen category.

![Horror Worksheet Image](docs/features/game-horror-worksheet-feature.png)
- This is done by Google Sheets APIs though the Goggle Clout Platform.
- The data is stored in each sheet will be randomly chosen an stored in a variable as a list.
- This list is converted into the underlined hint.
- The user is then asked to enter their first character guess.




## DATA MODEL

## TESTING


### User Stories Testing
#### First Time User Goals


#### Returning User Goals


#### Frequent User Goals


### Fixed Bugs
1. 

### Known Bugs



## TECHNOLOGIES USED
### Languages


### Frameworks, Libraries and Programs used
- [Am I Responsive](https://ui.dev/amiresponsive) Used for the mockup image.


## DEPLOYMENT



## CREDITS
### Media


### Resources


## ACKNOWLEDGEMENTS
