
class File:
    __directory = "D:\Documentos\Ajedrez\Bases de datos\StatisticalChess\\"
    __file = None

    def openFile(self, name: str):
        self.__file = open(self.__directory + name + ".txt", "r+")
        
        return (self.__file.readlines())

    def writeGameLine(self, gameLine: str):
        self.__file.write("\n" + gameLine)
        self.__file.close()
