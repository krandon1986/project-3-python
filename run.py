import random

SHIPS_LENGTH = [2,3,3,4,5]
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
GUESS_BOARD_PLAYER = [[" "] * 8 for i in range(8)]
GUESS_BOARD_COMPUTER = [[" "] * 8 for i in range(8)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

print_board(PLAYER_BOARD)

def ships_placed(board):
    pass

def check_ships_fit():
    pass

def overlap_ships():
    pass

def user_input():
    pass

def count_hit_ships():
    pass

def turn(board):
    pass

#while True:
