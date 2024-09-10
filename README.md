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
- [TESTING](#testing)
    - [PEP8](#pep8)
    - [Input Testing](#input-testing)
    - [Browser Testing](#browser-testing)
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
- This is done by using the open source data analysis toolkit pandas. Pandas sorted and displayed the data from the spreadsheet into the leaderboard.
- The leaderboard spreadsheet is accessed and used to keep the data of the user (username and score) via an API.
- Below the leaderboard the user can once again choose to return to the main menu or exit the program.

#### How To Play - Input Validation
![Leaderboard Input Validation Image](docs/features/leaderboard-input-validation-feature.png)
- The exact same as the [How To Play - Input Validation](#how-to-play---input-validation)

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

#### Correct Answer - Lives Left
![Correct Answer - Lives Left Image](docs/features/correct-answer-feature.png)
- When the player enters a correct guess a statement that their answer was correct will be displayed.
- The hint will be updated with the position of the guess. If the guess occurs multiple times in the word, it will be shown accordingly in the hint.
- Below that a list will appear to show which characters have been guessed so far. This list is indedpendent if the answer was wrong or right, this is solely done to show the user what was already guessed in case they have forgotten.
- The updated hint will be in uppercase to give the user a better visualization of what movie title needs to be find out.
#### Wrong Answer - Lives Left
![Wrong Answer - Lives Left Image](docs/features/wrong-answer-feature.png)
- When the player enters a wrong guess a statement that their answer was wrong will be displayed.
- For the first wrong guess the hangman figure will be displayed for the first time.

![Wrong Answer 2 - Lives Left Image](docs/features/wrong-answer2-feature.png)
- The more wrong guesses the user makes the more sticks will be "drawn" on to the figure.
- As most people are familiar with the game it was chosen to not write how many lives are left with each wrong guess, as it is visualized through the stick figure.
- The hint remains the same, the guesses character list will be updated.

#### Repeated Answer
![Repeated Answer Image](docs/features/repeated-answer-feature.png)
- When the user enters a guess they already entered a message will be displayed that they already had this guess. This is done independently if the guess is correct or not.
- The hint will not be shown again as this message does not take that much space and the hint should hence still be visible.

#### Correct Answer - No Lives Left
![Correct Answer - No Lives Left Image](docs/features/final-correct-answer-feature.png)
- When the user enters their final correct guess the terminal will be cleared.
- A winning statement will be displayed as well as further options for the user on how to proceed: Play again, Add lives left to the leaderboard or Exit.
- When choosing playing again the user will be redirected to choose a category.

#### Wrong Answer - No Lives Left
![Wrong Answer - No Lives Left Image](docs/features/final-wrong-answer-feature.png)
- When the user enters their final wrong guess the full hangman figure will be displayed.
- The loosing statement will also reveal the correct movie title.
- The user can then choose to return to the menu or exit the game. As this game is over this attempt was chosen because the user might want to re-read the isntructions. Therefore they have the opportunity to go back to the menu.

#### Guess Input Validation
![Guess Input Validation Image](docs/features/guess-input-validation-feature.png)
- The user is only allowed to enter singular character form a-z at the time.
- There will be a red error message for the user to see what they did wrong and how to correct it.
- As the correct input is vital for the game the hint what type of input is needed is given.
- This message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

#### Final Correct Answer Input Validation
![Final Correct Answer Input Validation Image](docs/features/final-correct-input-validation-feature.png)
- If the user does not enter a number between 1 and 4 an Error Message will appear. This message repeats the input from the user and states that they will be given the chance to enter an input again.
- This message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

#### Final Wrong Answer Input Validation
![Final Wrong Answer Input Validation Image](docs/features/final-wrong-input-validation-feature.png)
- The exact same as the [How To Play - Input Validation](#how-to-play---input-validation)


### Update Leaderboard
![Enter Username Image](docs/features/username-feature.png)
- After guessing the title correctly and choosing to add lives left to the leaderboard the user can enter their username.

![Leaderboard Sheet Image](docs/features/scoreboard-sheet-feature.png)
- The Goggle worksheet also has a leaderboard spreadsheet here the username and the lives left of the current user and previous users are storedan retrieved through an API.
- As many names as people will play can hence be saved to the document. The leaderboard will always be updated as soon as it is called.

#### Username Input Validation
![Username Input Validation Image](docs/features/username-input-validation-feature.png)
- As the username should max. be 15 characters long and should only consists out of letter from a to z, every other input is wrong.
- No matter what a user enters only within the given rules the input is accepted, else an error will be shown and the option to enter a username again is given.
- This message, as all error messages in this game, are printed out in red to indicate to the user that an error occured and their inputed data was invalid.

#### Updated Leaderboard
![Updated Leaderboard Image](docs/features/updated-leaderboard-feature.png)
- With every new user the leaderboard will be updated when the user either choses it in the game menu or after winning a game.
- The way the data is retrieved, displayed and what the user can do afterwards is the same as [above](#leaderboard).

### Future Features
- Allowing the user to enter possible titles as well.
- Adding more categories.
- Adding difficulty levels to the categories. 


## DATA MODEL
DO I NEED THIS IF I DO NOT HAVE CLASSES???


## TESTING
### PEP8 
No errors were returned for all python files from the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) testing:
<details>
<summary>run.py</summary>
No errors or warnings.

<img src="docs/pep8-runpy.png" alt="run.py PEP8 result">
</details>
<details>
<summary>hangman_figure.py</summary>
No errors or warnings.

<img src="docs/pep8-hangmanpy.png" alt="hangman_figure.py PEP8 result">
</details>


### Input Testing
As shown in the feature section above all input fields were manually tested by me and returned the correct output depending if the input was valid or not.
All input fields only accepted the type of data that is needed to advance in the code to the next step. This has been tested in Gitpod IDF environment and on the deployed website.


### Browser Testing
The website was successfully tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge

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
