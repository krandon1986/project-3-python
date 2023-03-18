



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
