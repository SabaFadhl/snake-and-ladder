from services.Validation import *

class Player():
    
    # self.__score=0
    # def __init__(self):
    #     pass 
    
    def __init__(self,name) :
        self.__score=0
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if  validation.validString(name,3,10):
            self.__name=name
            
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,score):
        # new=score+self.__score
        # print(score)
        # print(self.__score)
        # self.score=new
        # if new>100:
        #     self.__score=100
        # else:
        self.__score+=score
        
    def addScore(self,score):
        self.__score+=score         
     
        
            
    def __del__(self):
        del self
        
        
    
player=Player("saba")
player.score=6
# player.addScore(4)
print(player.score)
