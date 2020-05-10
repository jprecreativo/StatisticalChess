
import chess

class Game:
    __game = ""
    __board = chess.Board()
    __numMove = 1

    def getGame(self):
        return self.__game

    def getBoard(self):
        return self.__board

    def getNumMove(self):
        return self.__numMove

    def makeMove(self, move: str, isWhite: bool):
        if isWhite:
            self.__game += str(self.__numMove) + ". "
            self.__numMove += 1;

        self.__game += move + " "
        self.__board.push_san(move)
