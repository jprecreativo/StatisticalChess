
class Move:
    __directory = "D:\Documentos\Ajedrez\Bases de datos\StatisticalChess\\"
    __lines = ""

    def openFile(self, name: str):
        file = open(self.__directory + name + ".txt", "r")
        self.__lines = file.readlines()

    def __candidateMoves(self, game: str, numMove: int):
        cadidateMoves = []
        
        if numMove != -1:
            game += " " + numMove + ". " 

        for line in self.__lines:
            candidateMove = line.partition(game)[2].partition(" ")[0]

            if candidateMove != "":
                cadidateMoves.append(candidateMove)

        return cadidateMoves

    def nextMove(self, game: str, numMove: int):
        cadidateMoves = self.__candidateMoves(game, numMove)

        try:
            return max(set(cadidateMoves), key=cadidateMoves.count)
        
        except:
            return ""