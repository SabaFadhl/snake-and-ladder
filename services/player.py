from select import select


class Player():
    def __init__(self,name) :
        self.score=0
        self.name=name
    def addScore(self,score):
        self.score+=score
    def changeName(self,name):
        self.name=name
    def clear(self):
        self.score=0
        self.name=""
        
        
    
player=Player("saba")
player.addScore(6)
player.addScore(4)
print(player.score)
