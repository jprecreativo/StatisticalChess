
import chess
import operator
from fractions import Fraction

class Move:
    __directory = "D:\Documentos\Ajedrez\Bases de datos\StatisticalChess\\"
    __lines = ""

    def openFile(self, name: str):
        file = open(self.__directory + name + ".txt", "r")
        self.__lines = file.readlines()

    def __candidateMoves(self, gameLine: str, turn: bool, numMove: int):
        candidateMovesFrequencies = {}
        candidateMovesWins = {}
        result = ""

        for line in self.__lines:
            candidateMove = line.partition(gameLine)[2].partition(" ")[0]

            if candidateMove != "":
                result = line.split()[-1]

                if candidateMove in candidateMovesFrequencies:
                    try:
                        if turn == chess.WHITE:
                            candidateMovesWins[candidateMove] += float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        else:
                            candidateMovesWins[candidateMove] += float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        candidateMovesFrequencies[candidateMove] += 1

                    except: pass

                else:
                    try:
                        if turn == chess.WHITE:
                            candidateMovesWins[candidateMove] = float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        else:
                            candidateMovesWins[candidateMove] = float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        candidateMovesFrequencies[candidateMove] = 1
                    
                    except: pass

        return candidateMovesFrequencies, candidateMovesWins

    def nextMove(self, gameLine: str, turn: bool, numMove: int):
        candidateMovesFrequencies, candidateMovesWins = self.__candidateMoves(gameLine, turn, numMove)
        candidateMoves = {}

        for key in candidateMovesFrequencies:
            candidateMoves[key] = candidateMovesFrequencies[key] * candidateMovesWins[key]

        try: return max(candidateMoves, key=candidateMoves.get)
        except: return ""
