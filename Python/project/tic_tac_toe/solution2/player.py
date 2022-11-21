import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        # get a random valid spot for next move
        return random.choice(game.availableMoves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        validSquare = False
        mov = None

        while not validSquare:
            square = input(self.letter + "'s turn. Input move(0-8): ")
            try:
                # check input type by casting (raises exception ValueError)
                mov = int(square)
                if mov not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print("Invalid square. Try again")
        return mov


