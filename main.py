
from game import Game as GameClass
from move import Move as MoveClass

if __name__ == "__main__":
    firstMoves = ["a3","a4","b3","b4","c3","c4","d3","d4","e3","e4","f3","f4","g3","g4","h3","h4","Na3","Nc3","Nf3","Nh3"]
    firstMove = "a3"
    game = GameClass()
    move = MoveClass()

    game.makeMove(firstMove, True)
    move.openFile(firstMove)

    print(move.nextMove(game.getGame(), -1))

    game.makeMove("d5", False)

    print(move.nextMove(game.getGame(), game.getNumMove()))

    game.makeMove("Nf3", True)

    print(move.nextMove(game.getGame(), -1))

    game.makeMove("Nf6", False)

    print(move.nextMove(game.getGame(), game.getNumMove()))
