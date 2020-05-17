
from file import File as FileClass
from move import Move as MoveClass
import random
import chess

class Game:
    __fileObject = FileClass()
    __moveObject = None
    __firstMoves = ["a3","a4","b3","b4","c3","c4","d3","d4","e3","e4","f3","f4","g3","g4","h3","h4","Na3","Nc3","Nf3","Nh3"]
    __gameLine = ""
    __board = chess.Board()
    __theoreticalNovelty = False

    def __init__(self, firstMove: str):
        if firstMove == "":
            firstMove = random.choice(self.__firstMoves)
        
        self.__moveObject = MoveClass(self.__fileObject.openFile(firstMove))
        self.makeMove(firstMove)

    def __isGameOver(self, checkResult=False):
        if self.__board.is_game_over():
            if checkResult:
                self.__gameLine += self.__board.result()

            self.__moveObject.writeGameLine(self.__gameLine)

        print(self.__gameLine)

        return (self.__board.is_game_over())

    def __executeMove(self, nextMove: str):
        self.__gameLine += nextMove + " "
        self.__board.push_san(nextMove)

    def __humanMove(self, nextMove: str):
        self.__executeMove(nextMove)
        
        return (self.__isGameOver(checkResult=True))
        
    def __computerMove(self):
        if not self.__theoreticalNovelty:
            nextMove = self.__moveObject.nextMove(self.__gameLine, self.__board.turn, self.__board.fullmove_number)

            if nextMove == "":   # Computer does not know how to play.
                self.__theoreticalNovelty = True

        if self.__theoreticalNovelty:   # Computer claim draw or play a random move.
            if self.__board.can_claim_draw():
                self.__gameLine += self.__board.result(claim_draw=True)
                
                return self.__isGameOver()

            else:
                legalMoves = list(self.__board.legal_moves)
                nextMove = self.__board.san(random.choice(legalMoves))

                self.__executeMove(nextMove)

        return (self.__isGameOver())

    def resetGame(self):
        __gameLine = ""
        __board = chess.Board()
        __theoreticalNovelty = False

    def makeMove(self, nextMove: str):
        if self.__board.turn == chess.WHITE:
            self.__gameLine += str(self.__board.fullmove_number) + ". "

        if nextMove == "":
            return self.__computerMove()

        return self.__humanMove(nextMove)
