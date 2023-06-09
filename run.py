from random import randint



# This is a board for holding ship locations
SHIP_BOARD = [[' '] * 8 for x in range(8)]  
# This is a board displaying the hits and misses 
GUESS_BOARD = [[' '] * 8 for x in range(8)]

LETTERS_TO_NUMBERS = {
    'A': 0, 
    'B': 1, 
    'C': 2, 
    'D': 3, 
    'E': 4, 
    'F': 5, 
    'G': 6, 
    'H': 7
}


def print_board(board):
    print('  A B C D E F G H')
    print('  +-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print(f"%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# The computer create 5 ships
def create_battleships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def get_battleship_location():
    row = input('Please enter a row number from 1-8: ')
    while row not in '1,2,3,4,5,6,7,8,':
        print('Please enter a valid row number')
        row = input('Please enter a row number from 1-8: ')
    column = input('Please enter a column letter from A-H: ').upper()
    while column not in 'A,B,C,D,E,F,G,H,':
        print('Please enter a valid column letter')
        column = input('Please enter a column letter from A-H: ').upper()
    return int(row) - 1, LETTERS_TO_NUMBERS[column]


def count_hit_battlefield(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_battleships(SHIP_BOARD)
print_board(SHIP_BOARD)
turns = 15
while turns > 0:
    print('Welcome to Battleship')
    print_board(GUESS_BOARD)
    row, column = get_battleship_location()
    if GUESS_BOARD[row][column] == '/':
        print('You have aleady selected that area.')
    elif SHIP_BOARD[row][column] == 'X':
        print('Good shot, you have hit the battleship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed your target')
        GUESS_BOARD[row][column] = '/'
        turns -= 1
    if count_hit_battlefield(GUESS_BOARD) == 5:
        print('Congratulation, you have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you have ran out of turns. Game Over!')
        break