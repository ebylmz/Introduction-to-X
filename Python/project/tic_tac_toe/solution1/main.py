from game import TicTacToe
from player import HumanPlayer, ComputerPlayer

if __name__ == '__main__':
    playerX = HumanPlayer('x')
    # playerX = ComputerPlayer('x')
    playerO = ComputerPlayer('o')
    game = TicTacToe(playerX, playerO)
    game.play()