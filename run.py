from random import randint



#This is a board for holding ship locations
SHIP_BOARD = [[' '] * 8 for x in range(8)]
#This is a board displaying the hits and misses. 
GUESS_BOARD = [[' '] * 8 for x in range(8)]

LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    print('  A B C D E F G H')
    print('  +-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print(f"%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#The computer create 5 ships
def create_battleships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def get_battleship_location():
    row = input('Please enter a row number from 1-8 ')
    while row not in '12345678':
        print('Please enter a valid row number')
        row = input('Please enter a row number from 1-8 ')
    column = input('Please enter a column letter from A-H ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column letter')
        column = input('Please enter a column letter from A-H' ).upper()
    return int(row) - 1, LETTERS_TO_NUMBERS[column]
