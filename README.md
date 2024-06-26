<h1 align="center">Battleship</h1>

## Description

Battleship is single player python terminal game that runs in Heroku terminal.

The user is giving 15 turns to find and destroy all five of the computer's ships. Each ship occupies one squard of the board. After 15 turns and the user doesn't destroy all the ships, the user loses and it's game over. 


The battleship game is available [here](https://project-3-python-battleship.herokuapp.com)

![Responsive Mockup](assets/screenshots/iamresponsive.png)

## How to play

Battleship is based on the classic strategy type guessing game for two players. You can learn more about classic game on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, it is single player game in which the computer generates five ships and randomly spaces it across the board. The user is given 15 turns to take out all the ships. 

The ship as well as a hit is represented as a '-', while the miss is represented as a '/'.

You will lose the game if you hit 15 areas on the board and haven't destroy all the ships. However, you will gain two more turn for each ship destroyed. 

## Features

- __Random Board__
    - The ship board is where it show the location of computer's ships. For this instance, this will displayed only once when the program runs. 
    - The guess board is the replica of the ship board where computer's ships are invisible but are still in the same place in the ship board. 

![battleship](assets/screenshots/battleship.png) 

- __Error-checking 1__
    - Enter a number value that is greater than 8 or any letter values.
    - It would not take the invalid value and it repeats the statement again.

![invalid number](assets/screenshots/invalid-row-number.png)

- __Error-checking 2__
    - Enter a letter value that isn't on the board or any number value.
    - The game would again not accept the value and again repeat the statement until its condition is met.

![invalid letter](assets/screenshots/invalid-column-letter.png)

- __Error-checking 3__
    - Enter no values on the row.
    - It will display the error message, telling the user to enter a valid number to the row.

![empty string row](assets/screenshots/empty-string-row.png)

- __Error-checking 4__
    - As for the letter column, enter no values inside.
    - There will be an error message displayed, telling the user to enter a valid error message to the letter column.  

![empty string column](assets/screenshots/empty-string-column.png)

- __Error-checking 5__
    - Selecting an area that has already been labeled as a miss.
    - An error message will be displayed, informing the user that they have aleady selected the area. 
    - This mistake wouldn't affect the user's turn. If the user has 6 turns before selecting the missed area, they will still have 6 turns left.

![same-area](assets/screenshots/same-area.png)

- __Input Validaton 1__
    - Enter any number value from 1 to 8 on the number row.
    - Enter any letter from A to H on the letter column. 
    - If the computer's ship isn't on the area that the user have selected, '/' will be displayed on that area as a miss.
    - The program will display a message, informing the user that they have miss the target.
    - A second message is printed at the same time as the first, reminding the user that they have used a turn and it is subtracted from the remaining turns. 

![miss target](assets/screenshots/miss.png)

- __Input Validaton 2__
    - If the computer's ship is on the area that the user have selected, '-' will be displayed on that area as a hit.
    - The first message will be printed, praising the user on hitting a ship.
    - The direct hit will award you with two extra lives.  
    - The second message will show the remaining turns the user has left, plue the addition two.

![hit target](assets/screenshots/hit-2.png)

- __Input Validaton 3__
    - The user selects the area where the last ship is located at, which resulted in the game ending.
    - The first message printed is the same message the user receive when they hit a ship.
    - The second and last message is printed congratulate the user for winning the game. 

![won game](assets/screenshots/won_game.png)

- __Input Validaton 4__
    - If user has only one turn left, the game will end with a loss whether or not they hit or missed a ship.
    - One of two alternative messages will be printed, either praising the user for hitting a ship or informing the user that they have missed the target. 
    - The last message is printed, informing the user that the game is over as they have run out of turns.
    - The Ship Board will be displayed, showing the location of the battleship to th user. 

![loss game](assets/screenshots/lost_game-2.png) 


## Data Model

I created two instance of the board that holds the computer's and guess' board. 

Each number row and columns of the board will be 8, with each value be an empty string.

As the column will be labeled in letters, I need to convert it into numbers.

Create print_board function to create a template board with '8' rows and '8' columns. Start the row number with '1' so that first row doesn't start at '0'. 

I create a function that create the computer ships on the board. The 'For' statement create five ships, and place them across the row and column from '0' to '7'. In the while loop, each ship is represented with a 'X' and they place randomly across the row and columns from '0' to '7'. 

The get_battleship_location function allow the user to start the game by selecting a row number and then column letter. If the value that the user inputed matchs row and column criteria, they both return the value. In row, the value returns as a integer minus 1. In column, the letters are coverted into numbers. To make that an empty string isn't entered in the row and column field which cause the game to crash out, the 'While True' construct is used to display an invalid error message to inform the user to enter a valid value. 

The count_hit_battlefield function using the 'for loop' and 'if' statement to loops the rows and columns on the board to if the 'X' exist. If the 'X' does exist in area that is selected, the counter will count as 1 and return it to the counter which upgraded from this "count = 0" to "count = 1". 

The final lines of code is to print out the two boards (ship board and guess board) and write the if and else statments under while loop,so the user can run the game. Before while loop, I have enter '15' as the amount of turns the user uses. Each time is played, the amount of turn is subtract from start of the while loop. The if/else and elif statements will ensure that games run smoothly. If the user hits a target, elif statement will print the suitable message inform the user of their success and place a '-' on the board. If the user miss, the else statement will print out a suitable and place a '/' on the board. The last two 'if' statements ends the game when the value of battleship hit on the 'GUESS_BOARD' equal to '5', or when turn counter 'turns = 15' hit '0'. Former lead to a win, while the latter lead to a loss. 



## Testing 
I have manually testing project by:
- Passing the code through PEP8 Python Validator and encounter lots of problems, but managed to cut down to eleven. Nine of them is about trailing whitespace
- Given invalid inputs: enter a string value into a number field, input out-of-bound values, input the same value
- Tested the program on the gitpod terminal and Heroku terminal

### Bug
- When I entered '12' in row input, the program crashed. The reason for this is in the while loop under get_battlefield_location function,  it was suppose to display an error message if the value doesn't match the list of numbers from 1 to 8 inside a single string. The eight numbers wasn't separated with a comma, so any double figures like '12' '23' '34' '45' '56' '67' '78' that is inputted would pass the criteria, which resulted in the program to crash.
- I encountered the same problem when I entered double letter values in the row input. Like the last problem, I place comma between every letter. 
- After entering no values in the both row and column values, it crash the program. So I use the while true construct to display an error message if an empty string is being entered in the row and column field. 

## Deployment
This project was deployed in Heroduk using the Code Institute's terminal.
- Step for deployment:
    - Clone the the battleship repository.
    - Create a new Heroku app.
    - Name the new Heroku app.
    - Go on setting and click the 'Reveal Config Vars' button.
    - Enter 'PORT' as a key and 8000 as value.
    - Set the buildbacks to 'Python' and 'NodeJS' in that order. 
    - Link the Heroku app to the battleship repository.
    - Click [Deploy Branch](https://project-3-python-battleship.herokuapp.com/)

## Credit
- The framework I used to build this battleship game is from a Youtube python tutorial created by [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
