from services import *
from board  import *
from os import system, name

board=cells.makeList(1,31,6)
cells.drawBoard()
player1=Player("saba1")

player1.score=3
print(player1.score)
player2=Player("ddd")
cells.changePlayersPosition(player1)
# Screen.clear(0)
