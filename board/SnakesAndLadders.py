from board.cells import *
from services.Screen import *

class SnakesAndLadders(Cells):
      def __init__(self) :
          self.__snakes={17:4,19:7,21:9,27:1}
          self.__ladders={3:22,5:8,11:26,20:29}
        #   self.colorize()
          
     #function to create list of rows
      def makeList(self,min,max,rowsNum):
           #initialize variables
           self.myBoard =list() 
           self.row =list() 
           self._rowsNum =rowsNum
           self._min=min
           self._max=max
           
           for cell in range( self._min,self._max+1):
                  if cell in self.__ladders.keys():
                      self.row.append(ladderNum(num=cell))
                  elif cell in self.__snakes.keys():
                      self.row.append(snakenum(num=cell))
                  else :
                      self.row.append(normalNum(num=cell))
                          
                  if cell%self._rowsNum==0:
                        self.myBoard.append(self.row)
                        self.row=list()
           return self.myBoard 
       
      def changePlayersPosition(self,p1=Player(""),p2=Player("")):
            clear(0)
            self.makeList(self._min,self._max,self._rowsNum)
            # print ("befor",p1.score,p2.score)
            
            self.checkScore(self.__snakes,"snake",p1)
            self.checkScore(self.__ladders,"ladder",p1)
            self.checkScore(self.__snakes,"snake",p2)
            self.checkScore(self.__ladders,"ladder",p2)
            
            self.myBoard[int(p1.score/6-1)][int(p1.score%6-1)]="p1"
            self.myBoard[int(p2.score/6-1)][int(p2.score%6-1)]="p2"
            
            # print ("after",p1.score,p2.score)
            
            
            # print("p1",p1.score)
            # print("p2",p2.score)
            
            clear(0)      
            self.drawBoard()
      def checkScore(self,dict,type,p=Player("")):
          if p.score in dict.keys():
                for key,value in dict.items():
                    if p.score.__eq__(key):
                        p.score=value
                        if type.__eq__("snake"):
                            print('''
                                    ---------------------------
                                      %s Snake -_- to %s    
                                    ---------------------------
                                    '''%(p.name,p.score))
                            snake()
                            clear(2)
                        elif type.__eq__("ladder"):
                            print('''
                            ---------------------------
                                %s Ladder ^_^ to %s     
                            ---------------------------
                            '''%(p.name,p.score))
                            ladder()
                            clear(2)
                        
game=SnakesAndLadders()





