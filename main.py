
from menu import Menu as MenuClass
from game import Game as GameClass

if __name__ == "__main__":
    startedGame = False
    
    while True:
        if not startedGame:
            while True:
                option = MenuClass.ShowStartMenu(MenuClass)

                if option in [1,2]:
                    break

            startedGame = True
            humanTurn = True
            nextMove = ""

            if option == 1:   # Human begins the game.
                nextMove = MenuClass.AskForMove(MenuClass)
                humanTurn = False

            gameObject = GameClass(nextMove)

        else:
            if humanTurn:
                nextMove = MenuClass.AskForMove(MenuClass)
                humanTurn = False

            else:
                nextMove = ""
                humanTurn = True

            startedGame = not (gameObject.makeMove(nextMove))
