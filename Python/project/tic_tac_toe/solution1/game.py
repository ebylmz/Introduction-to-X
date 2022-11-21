import time
import random  

class TicTacToe:
    def __init__(self, playerX, playerO):
        self.playerX = playerX
        self.playerO = playerO
        self.board = [' ' for _ in range(9)] # single list to represent 3x3 row

    def printBoard(self):
        rows = [self.board[i * 3: (i + 1) * 3] for i in range(3)]        
        for row in rows: 
            print('|' + " | ".join(row) + '|')

    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False
    
    def availableMoves(self):
        # with enumerate ['x', 'x', 'o'] --> [(0, 'x') , (1, 'x'), (2, 'o')] 
        # each tuple can be use in for loop 
        # single line with list comprehension
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def emptySquare(self):
        return ' ' in self.board        

    def numOfEmptySquares(self):
        return self.board.count(' ')

    def winner(self, square, letter):
        # winner if there is a 3 
        # check the row
        rowIndex = square // 3 # current row
        row = self.board[rowIndex * 3 : (rowIndex + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # check column
        colIndex = square % 3 # current coloumn
        col = [self.board[i * 3 + colIndex] for i in range(3)]
        if all(spot == letter for spot in col):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        # 0 1 2
        # 3 4 5
        # 6 7 8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        # if all of these fail 
        return False

    # returns the winner of of the fame or None for a tie
    def play(self):
        # define who start first 
        letter = random.choice(['x', 'o']) 

        # print square numbers
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        for row in [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]:
            print('|' + " | ".join(row) + '|')

        # iterate while the game still has empty squares
        while self.emptySquare():
            # get the move from appropriate player
            if letter == 'x':
                square = self.playerX.getMove(self) 
            else:
                square = self.playerO.getMove(self)

            if self.makeMove(square, letter):
                print(letter + " makes a move to square " + str(square))
                self.printBoard()

                # after valid movement check if current player win
                if self.winner(square, letter):
                    print(letter + " wins!")
                    return letter
                letter = 'o' if letter == 'x' else 'x'
            # tiny break
            print()
            time.sleep(.8)
        print("It's a tie!")
