from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # single list to represent 3x3 row
        self.currentWinner = None # keep track of winner

    def printBoard(self):
        # commands explain the things that happen under the hood

        # rows = [[]]
        # for i in range(3):
        #     for j in range(3):
        #         rows[i].append(self.board[i * 3 + j])

        # rows = [self.board[i * 3 : (i + 1) * 3] for i in range(3)]
                 
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('|' + ' | '.join(row)  + '|')

    @staticmethod
    def printBoardNums(): #! since it's static method no parameter as self exist 
        # 0 | 1 | 2 etc (tells us whawt number corresponds to what box)
        # numberBoard = [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]

        for row in [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]:
            print('|' + ' | '.join(row) + '|') 

    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these
        # first let's check the row
        rowIndex = square // 3
        row = self.board[rowIndex * 3 : (rowIndex + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # check column
        colIndex = square % 3
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

    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # after move check if there is a winner
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False

    def availableMoves(self):
        # with enumerate ['x', 'x', 'o'] --> [(0, 'x') , (1, 'x'), (2, 'o')]
        # we use each tuple in for loop 
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

        # single line with list comprehension
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def isGameOver(self):
        return ' ' not in self.board

    def numOfEmptySquares(self):
        return self.board.count(' ')


# returns the winner of of the fame or None for a tie
def play(game, playerX, playerO, printGame = True):
    if printGame: 
        TicTacToe().printBoardNums()
    
    letter = 'x'  # starting letter

    # iterate while the game still has empty squares
    while not game.isGameOver():
        # get the move from appropriate player
        square = playerX.getMove(game) if letter == 'x' else playerO.getMove(game)

        if game.makeMove(square, letter):
            if printGame:
                print(letter + f" makes a move to square {square}")
                game.printBoard()
                print() # empty line            
            
            # check if game game is over
            if game.currentWinner:
                if printGame:
                    print(letter + " wins!")
                return letter # winner

            letter = 'o' if letter == 'x' else 'x'
        # tiny break
        time.sleep(.8)
    if printGame:
        print("It's a tie!")

if __name__ == '__main__':
    playerX = HumanPlayer('X')
    playerY = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, playerX, playerY, printGame = True)