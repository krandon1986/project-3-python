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


def ships_placed(board):
    #looping through the length of the ships
    for ship_position in SHIPS_LENGTH:
        #loop until ship fits and does not overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H","V"]), random.randint(0, 7), random.randint(0, 7)
                if check_ships_fit(ship_position, row, column, orientation):

def check_ships_fit(ship_position, row, column, orientation):
    if orientation == "H":
        if column + ship_position > 8:
            returns False
        else:
            return True
    else:
        if row + ship_position > 8:
            return False
        else:
            return True


def overlap_ships():
    pass

def user_input():
    pass

def count_hit_ships():
    pass

def turn(board):
    pass

#while True:
