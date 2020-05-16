
from move import Move as MoveClass
import random
import chess

class Game:
    __moveObject = MoveClass()
    __firstMoves = ["a3","a4","b3","b4","c3","c4","d3","d4","e3","e4","f3","f4","g3","g4","h3","h4","Na3","Nc3","Nf3","Nh3"]
    __gameLine = ""
    __board = chess.Board()
    __numMove = 1
    __theoreticalNovelty = False

    def __init__(self, firstMove: str):
        if firstMove == "":
            firstMove = random.choice(self.__firstMoves)
        
        self.__moveObject.openFile(firstMove)
        self.makeMove(firstMove)

    def makeMove(self, nextMove: str):
        if self.__board.turn == chess.WHITE:
            self.__gameLine += str(self.__numMove) + ". "
            self.__numMove += 1;

        if not self.__theoreticalNovelty and nextMove == "":   # Computer to play.
            nextMove = self.__moveObject.nextMove(self.__gameLine, self.__board.turn, self.__numMove)

            if nextMove == "":   # Computer does not know how to play.
                self.__theoreticalNovelty = True

        if self.__theoreticalNovelty:
            nextMove = self.__board.san(random.choice(list(self.__board.legal_moves)))

        self.__gameLine += nextMove + " "
        self.__board.push_san(nextMove)

        print(self.__gameLine)
