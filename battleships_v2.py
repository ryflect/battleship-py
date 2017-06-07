# Imports
from random import randint
import string


# Board Creation
class Board(object):
    b = []

    def __init__(self, row):
        self.row = row

    def create_board(self):
        b = [['O' for i in range(self.row)] for j in range(self.row)]
        return b

    def check_tile(self, x, y, ch, board):
        if board[x][y] == ch:
            return True
        else:
            return False

    def place_battleship(self, board):
        b_ship = False
        while not b_ship:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            b_ori = randint(0, 1)
            if b_ori == 0:
                if y+3 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x, y+1, 'O', board) and self.check_tile(x, y+2, 'O', board) and self.check_tile(x, y+3, 'O', board):
                    board[x][y] = 'B'
                    board[x][y+1] = 'B'
                    board[x][y+2] = 'B'
                    board[x][y+3] = 'B'
                    b_ship = True
            elif b_ori == 1:
                if x+3 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x+1, y, 'O', board) and self.check_tile(x+2, y, 'O', board) and self.check_tile(x+3, y, 'O', board):
                    board[x][y] = 'B'
                    board[x+1][y] = 'B'
                    board[x+2][y] = 'B'
                    board[x+3][y] = 'B'
                    b_ship = True

    def place_carrier(self, board):
        c_ship = False
        while not c_ship:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            c_ori = randint(0, 1)
            if c_ori == 0:
                if y+4 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x, y+1, 'O', board) and self.check_tile(x, y+2, 'O', board) and self.check_tile(x, y+3, 'O', board) and self.check_tile(x, y+4, 'O', board):
                    board[x][y] = 'C'
                    board[x][y+1] = 'C'
                    board[x][y+2] = 'C'
                    board[x][y+3] = 'C'
                    board[x][y+4] = 'C'
                    c_ship = True
            elif c_ori == 1:
                if x+4 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x+1, y, 'O', board) and self.check_tile(x+2, y, 'O', board) and self.check_tile(x+3, y, 'O', board) and self.check_tile(x+4, y, 'O', board):
                    board[x][y] = 'C'
                    board[x+1][y] = 'C'
                    board[x+2][y] = 'C'
                    board[x+3][y] = 'C'
                    board[x+4][y] = 'C'
                    c_ship = True

    def place_submarine(self, board):
        s_ship = False
        while not s_ship:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            s_ori = randint(0, 1)
            if s_ori == 0:
                if y+2 >= self.row:
                    pass
                elif self.check_tile(x,y, 'O', board) and self.check_tile(x, y+1, 'O', board) and self.check_tile(x, y+2, 'O', board):
                    board[x][y] = 'S'
                    board[x][y+1] = 'S'
                    board[x][y+2] = 'S'
                    s_ship = True
            elif s_ori == 1:
                if x+2 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x+1, y, 'O', board) and self.check_tile(x+2, y, 'O', board):
                    board[x][y] = 'S'
                    board[x+1][y] = 'S'
                    board[x+2][y] = 'S'
                    s_ship = True

    def place_destroyer(self,board):
        d_ship = False
        while not d_ship:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            d_ori = randint(0, 1)
            if d_ori == 0:
                if y+1 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x, y+1, 'O', board):
                    board[x][y] = 'D'
                    board[x][y+1] = 'D'
                    d_ship = True
            elif d_ori == 1:
                if x+1 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x+1, y, 'O', board):
                    board[x][y] = 'D'
                    board[x+1][y] = 'D'
                    d_ship = True

    def place_cruiser(self, board):
        k_ship = False
        while not k_ship:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            k_ori = randint(0, 1)
            if k_ori == 0:
                if y+2 >= self.row:
                    pass
                elif self.check_tile(x,y, 'O', board) and self.check_tile(x, y+1, 'O', board) and self.check_tile(x, y+2, 'O', board):
                    board[x][y] = 'K'
                    board[x][y+1] = 'K'
                    board[x][y+2] = 'K'
                    k_ship = True
            elif k_ori == 1:
                if x+2 >= self.row:
                    pass
                elif self.check_tile(x, y, 'O', board) and self.check_tile(x+1, y, 'O', board) and self.check_tile(x+2, y, 'O', board):
                    board[x][y] = 'K'
                    board[x+1][y] = 'K'
                    board[x+2][y] = 'K'
                    k_ship = True


# Printing the board
def print_board(rows):
    num = 0
    letters = list(string.ascii_uppercase)
    print num,
    num += 1
    for i in rows:
        print num,
        num += 1
    print ' '
    num = 0
    for row in rows:
        print letters[num],
        print ' '.join(row)
        num += 1


# Conversion from letter list to num list
def convert_letter_to_num(letter):
    le = list(string.ascii_uppercase)
    for w in range(len(le)):
        if letter == le[w]:
            return w

# Main Program
rows = 10
ships = 5
guesses = 30
a = Board(rows)
battle = a.create_board()
a.place_carrier(battle)
a.place_battleship(battle)
a.place_submarine(battle)
a.place_cruiser(battle)
a.place_destroyer(battle)

print 'Welcome to Battleships!'

c_count = 5
b_count = 4
s_count = 3
k_count = 3
d_count = 2
while guesses:
    g = raw_input('Enter the target: ')
    x = convert_letter_to_num(g[0])
    y = int(g[1:])-1
    if battle[x][y] == 'B':
        print 'Battleship Hit!'
        battle[x][y] = '!'
        b_count -= 1
    elif battle[x][y] == 'C':
        print 'Carrier Hit!'
        battle[x][y] = '!'
        c_count -= 1
    elif battle[x][y] == 'D':
        print 'Destroyer Hit!'
        battle[x][y] = '!'
        d_count -= 1
    elif battle[x][y] == 'K':
        print 'Cruiser Hit!'
        battle[x][y] = '!'
        k_count -= 1
    elif battle[x][y] == 'S':
        print 'Submarine Hit!'
        battle[x][y] = '!'
        s_count -= 1
    else:
        print 'Miss'
    guesses -= 1

print_board(battle)
total = c_count + d_count + k_count + s_count + b_count
if total == 0:
    print 'You win!'
else:
    print 'You lose.'
