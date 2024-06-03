# A simple terminal based implementation of the well
# known game Tic Tac Toe, programmed in python.
# Programmed By: Stephen Adams

# Board Setup
board = [[0 for i in range(3)] for i in range(3)]

# Outputs Playing Grid
def output():
    for row in range(3):
        print(str(board[row]).replace('0','_').replace('3','X').replace('4','O'))

# Returns Current Players Value
def player():
    empty = sum(row.count(0) for row in board)
    return 3 if (9-empty) % 2 == 0 else 4

# Checks Horizontal & Vertical
def check_axis():
    for y in range(3):
        row_total = sum(board[y])
        column_total = sum(board[x][y] for x in range(3))
        if row_total in [9, 12] or column_total in [9, 12]:
            return True

# Checks Diagonals
def check_diagonals():
    left_diagnonal = sum(board[n][n] for n in range(3))
    right_diagnonal = sum(board[2-n][n] for n in range(3))
    if left_diagnonal in [9,12] or right_diagnonal in [9,12]:
        return True

# Checks For A Winner
def check_winner():
    if check_axis() or check_diagonals():
        output()
        if player() == 3:
            print('O Wins!')
        else:
            print('X Wins!')
    elif sum(row.count(0) for row in board) == 0:
        print('Draw!')
    else:
        play()

# Main Function
def play(start=False):
    if start:
        print('\nWelcome To Tic-Tac-Toe\nPlease Enter Coordinates In The Format XY')
    try:
        output()
        position = input('Enter Coordinates: ')
        x = int(position[0])-1
        y = int(position[1])-1
        if board[y][x] == 0:
            board[y][x] = player()
            check_winner()
        else:
            print('Space Already Occupied')
            play()
    except:
        print('Invalid Move')
        play()
play(start=True)