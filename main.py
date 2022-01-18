from services import *
from board  import *

board=game.makeList(1,30,6)
game.drawBoard()
player1=Player("saba1")
player2=Player("saba2")

player1.score=17
player2.score=2

# # print(player1.score)
# player2=Player("ddd")
game.changePlayersPosition(player1,player2)
# player1.score=3
# game.changePlayersPosition()

# # Screen.clear(0)
# dice.roll()
