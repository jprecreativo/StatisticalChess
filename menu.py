
class Menu:

    def ShowStartMenu(self):
        print("1.- Play as white")
        print("2.- Play as black")

        try: return int(input())
        except: return -1

    def AskForMove(self):
        print("Write your move")

        return input()
