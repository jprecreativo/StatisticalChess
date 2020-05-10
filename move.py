
import operator
from fractions import Fraction

class Move:
    __directory = "D:\Documentos\Ajedrez\Bases de datos\StatisticalChess\\"
    __lines = ""

    def openFile(self, name: str):
        file = open(self.__directory + name + ".txt", "r")
        self.__lines = file.readlines()

    def __candidateMoves(self, game: str, numMove: int):
        candidateMovesFrequencies = {}
        candidateMovesWins = {}
        result = ""
        
        if numMove != -1:   # Black to play.
            game += str(numMove) + ". "

        for line in self.__lines:
            candidateMove = line.partition(game)[2].partition(" ")[0]

            if candidateMove != "":
                result = line.split()[-1]

                if candidateMove in candidateMovesFrequencies:
                    try:
                        if numMove != -1:   # Black to play.
                            candidateMovesWins[candidateMove] += float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        else:   # White to play.
                            candidateMovesWins[candidateMove] += float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        candidateMovesFrequencies[candidateMove] += 1

                    except: pass

                else:
                    try:
                        if numMove != -1:   # Black to play.
                            candidateMovesWins[candidateMove] = float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        else:   # White to play.
                            candidateMovesWins[candidateMove] = float(Fraction(result.partition("-")[2].partition("\n")[0]))

                        candidateMovesFrequencies[candidateMove] = 1
                    
                    except: pass

        return candidateMovesFrequencies, candidateMovesWins

    def nextMove(self, game: str, numMove: int):
        candidateMovesFrequencies, candidateMovesWins = self.__candidateMoves(game, numMove)
        candidateMoves = {}

        for key in candidateMovesFrequencies:
            candidateMoves[key] = candidateMovesFrequencies[key] * candidateMovesWins[key]

        try:
            return max(candidateMoves, key=candidateMoves.get)
        
        except: return ""
