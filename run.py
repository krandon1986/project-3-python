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
                #checking to see if ship overlaps
                    if overlap_ships(board, row, column, orientation, ship_position) == False:
                        #place the ship
                        if orientation == "H":
                            for i in range(column, column + ship_position):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_position):
                                board[i][column] = "X"
                        break
                    else:
                        ship_placed = True
                        print('Place a ship with a length of' + str(ship_position))
                        row, column, orientation = user_input(ship_placed)
                        if check_ships_fit(ship_position, row, column, orientation):
                            #check if the ship has overlap
                                if overlap_ships(board, row, column, orientation, ship_position) == False:
                                    #place your ship
                                    if orientation == "H":
                                        for i in range(column, column + ship_position):
                                            board[row][i] = "X"
                                    else:
                                        for i in range(row, row + ship_position):
                                            board[i][column] = "X"
                                    print_board(PLAYER_BOARD)
                                    break

def check_ships_fit(SHIP_POSITION, row, column, orientation):
    if orientation == "H":
        if column + SHIP_POSITION > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_POSITION > 8:
            return False
        else:
            return True


def overlap_ships(board, row, column, orientation, ship_position):
    if orientation == "H":
        for i in range(column, column + ship_position):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_position):
            if board[i][column] == "X":
                return True
    return False

def user_input(ship_placed):
    if ship_placed == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Please enter a valid orientation H or V')
        while True:
            try:
                row = input("Enter the row 1-8 for your ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the column A-H for your ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
            return row, column, orientation
        else:
            while True:
                try:
                    row = input("Enter the column of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid number between 1-8')
            while True:
                try:
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGH':
                        column = LETTERS_TO_NUMBERS[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column 

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def turn(board):
    pass

#while True:
