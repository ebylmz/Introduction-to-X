import random
import re

class Board:
    def __init__(self, size, numBombs):
        self.size = size
        self.numBombs = numBombs
        self.board = self.makeNewBoard() # plant the bombs
        self.assignValuesToBoard()

        # initialize a set to keep track of which locations we've uncovered
        # we will save (row, column) tuples into this set
        self.dug = set() # if we dig at 0, 0 then self.dug = {(0,0)}

    
    def makeNewBoard(self):
        board = [[j for j in range(self.size)] for i in range(self.size)]

        # plant the bombs
        bombsPlanted = 0
        while bombsPlanted < self.numBombs:
            # select random location
            loc = random.randint(0, self.size**2 - 1) 
            r = loc // self.size    # row
            c = loc % self.size     # coloumn

            # be sure selected location is not planted bomb already
            if board[r][c] != '*':
                board[r][c] = '*'
                bombsPlanted += 1
        return board

    def assignValuesToBoard(self):
        for r in range(self.size):
            for c in range(self.size):
                # calculate the neighoring bombs number for empty cell
                if self.board[r][c] != "*":
                    self.board[r][c] = self.getNumNeighboringBombs(r, c)
    
    def getNumNeighboringBombs(self, row, col):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are.
        # * * *
        # * 8 *
        # * * *
        numNeighboringBombs = 0

        # make sure to not go out of bounds!
        for r in range(max(0, row - 1), min(row + 1, self.size - 1) + 1):
            for c in range(max(0, col - 1), min(col + 1, self.size - 1) + 1):
                # don't check our original location
                if (r != row or c != col) and (self.board[r][c] == '*'):
                    numNeighboringBombs += 1
        return numNeighboringBombs

    # return True if successful dig, False if bomb dug
    def dig(self, row, col):

        self.dug.add((row, col)) # keep track that we dug here

        # hit a bomb (game over)
        if self.board[row][col] == '*':
            return False

        # dig at location with neighboring bombs -> finish dig
        elif self.board[row][col] > 0:
            return True

        # dig at location with no neighboring bombs -> recursively dig neighbors!
        for r in range (max(0, row - 1), min(self.size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.size - 1, col + 1) + 1):
                if (r, c) not in self.dug:
                    self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(size = 10, numBombs = 10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!

    board = Board(size, numBombs)
    safe = True

    while len(board.dug) < board.size ** 2 - numBombs:
        print(board)

        # 0,0 or 0, 0 or 0,      0
        userInput = re.split(",(\\s)*", input("Where would you like to dig? Input as row, col: "))
        try:
            row, col = int(userInput[0]), int(userInput[-1])    # first and last input
            if 0 <= row and row < board.size and 0 <= col and col < board.size:
                safe = board.dig(row, col)
                if not safe:
                    # dug a bomb (game over rip)
                    break
            else:
                print("Invalid location. Try again.")
        except ValueError:
            print("Invalid location. Try again.")
    
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.size) for c in range(board.size)]
        print(board)

if __name__ == "__main__":
    play()