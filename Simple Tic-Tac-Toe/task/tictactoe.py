# write your code here
# line = str(input('Enter cells: '))
line = '_________'
DASH = '|'
X: str = str('X')
O: str = 'O'
UNDERSCORE = '_'
GAME_NOT_FINISHED = 'Game not finished'
DRAW = 'Draw'
X_WINS = 'X wins'
O_WINS = 'O wins'
IMPOSSIBLE = 'Impossible'
current_player = X
global turn
turn = 0
mark = [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]]


# mark0 = line[0]  # (1, 1)
# mark1 = line[1]  # (1, 2)
# mark2 = line[2]  # (1, 3)
# mark3 = line[3]  # (2, 1)
# mark4 = line[4]  # (2, 2)
# mark5 = line[5]  # (2, 3)
# mark6 = line[6]  # (3, 1)
# mark7 = line[7]  # (3, 2)
# mark8 = line[8]  # (3, 3)

def print_table():
    print("---------")

    print(DASH, line[0], line[1], line[2], DASH)
    print(DASH, line[3], line[4], line[5], DASH)
    print(DASH, line[6], line[7], line[8], DASH)

    print("---------")


print_table()
## AKCJE UŻYTKOWNIKA

# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

cell = [11, 12, 13, 21, 22, 23, 31, 32, 33]


def print_table_mark():
    print("---------")

    print(DASH, mark[0], mark[1], mark[2], DASH)
    print(DASH, mark[3], mark[4], mark[5], DASH)
    print(DASH, mark[6], mark[7], mark[8], DASH)

    print("---------")


def arbitraz():
    if o_wins() == True and x_wins() == True:
        print(IMPOSSIBLE)
        exit()
    if line.count(X) + 2 == line.count(O) or line.count(X) == line.count(O) + 2:
        print(IMPOSSIBLE)
        exit()
    if o_wins() == None and x_wins() == None and UNDERSCORE not in line:
        print(DRAW)
        exit()
    if o_wins() == None and x_wins() == None and UNDERSCORE in line:
        gra()
    if o_wins() == True:
        print(O_WINS)
        exit()
    if x_wins() == True:
        print(X_WINS)
        exit()

## OKUPACJA KOMÓREK





## REGUŁY WYGRANEJ
def x_wins():
    if mark[0] == X and mark[1] == X and mark[2] == X:
        return True
    if mark[3] == X and mark[4] == X and mark[5] == X:
        return True
    if mark[6] == X and mark[7] == X and mark[8] == X:
        return True
    if mark[0] == X and mark[4] == X and mark[8] == X:
        return True
    if mark[2] == X and mark[4] == X and mark[6] == X:
        return True
    if mark[0] == X and mark[3] == X and mark[6] == X:
        return True
    if mark[2] == X and mark[5] == X and mark[8] == X:
        return True
    if mark[1] == X and mark[4] == X and mark[7] == X:
        return True


def o_wins():
    if mark[0] == O and mark[1] == O and mark[2] == O:
        return True
    if mark[3] == O and mark[4] == O and mark[5] == O:
        return True
    if mark[6] == O and mark[7] == O and mark[8] == O:
        return True
    if mark[0] == O and mark[4] == O and mark[8] == O:
        return True
    if mark[2] == O and mark[4] == O and mark[6] == O:
        return True
    if mark[0] == O and mark[3] == O and mark[6] == O:
        return True
    if mark[2] == O and mark[5] == O and mark[8] == O:
        return True
    if mark[1] == O and mark[4] == O and mark[7] == O:
        return True


global player
player = X

def gra():
    global turn
    #arbitraz()
    while True:
       # turn = 0
        print("o_wins() == None=", o_wins() == None )
        print("x_wins() == None=", x_wins() == None)
        print("UNDERSCORE not in mark=",UNDERSCORE not in mark)
        print("turn <= 8=",turn >= 8)
        if all([(o_wins() is None), (x_wins() is None), (UNDERSCORE not in mark), (turn == 9)]):
            print(DRAW)
            exit()
        cord_input = input("Enter the coordinates:").split()
        coordinates = ''.join(cord_input)
        # sprawdz które pole zostało wybrane
        if coordinates.isnumeric() != True:
            print("You should enter numbers!")
            continue
        else:
            coordinates = int(coordinates)
        if coordinates in cell:
            index = int(cell.index(int(coordinates)))
        else:
            print("Coordinates should be from 1 to 3!")
            continue
        if mark[index] in [X, O]:
            print("This cell is occupied! Choose another one!")
            continue
        elif mark[index] == UNDERSCORE:

            if turn == 0 or turn % 2 == 0:
                mark[index] = X
                turn += 1
            elif turn == 1 or turn % 2 != 0:
                mark[index] = O
                turn += 1
            #print(turn)
            print_table_mark()
            arbitraz()
            break


gra()
