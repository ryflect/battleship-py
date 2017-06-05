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

    def place_ship(self, board, ships):
        ships_placed = 0
        while ships_placed != ships:
            x = randint(0, self.row - 1)
            y = randint(0, self.row - 1)
            if board[x][y] != 'X':
                board[x][y] = 'X'
                ships_placed += 1


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
rows = 7
ships = 5
guesses = 10
a = Board(rows)
battle = a.create_board()
a.place_ship(battle, ships)
print 'Welcome to Battleship!'

while guesses:
    g = raw_input('Enter the target: ')
    x = convert_letter_to_num(g[0])
    y = int(g[1])-1
    if battle[x][y] == 'X':
        print 'Hit!'
        battle[x][y] = '!'
        ships -= 1
    else:
        print 'Miss'
    guesses -= 1

print_board(battle)
if ships == 0:
    print 'You win!'
else:
    print 'You lose.'

