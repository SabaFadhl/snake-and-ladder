from board.cells import *
from services.Screen import *

class SnakesAndLadders(Cells):
      def __init__(self) :
          self.__snakes={17:4,19:7,21:9,27:1}
          self.__ladders={3:22,5:8,11:26,20:29}
          super().__init__
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
       
      def changePlayersPosition(self,p1,p2):
            # clear(2)
            
            # print ("befor",p1.score,p2.score)
            
            self.makeList(self._min,self._max,self._rowsNum)
            # print(p1.score,p2.score)
            if p1.score>30:
                p1.score=30
                
            if p2.score>30:
                p2.score=30
            
            
            scor1=self.checkScore(self.__snakes,"snake",p1)
            scor2=self.checkScore(self.__ladders,"ladder",p1)
            scor3=self.checkScore(self.__snakes,"snake",p2)
            scor4=self.checkScore(self.__ladders,"ladder",p2)
            # if scor1 and scor2 and scor3 and scor4
            clear(0) 
            
            if p1.score/6-1<0:
                
                # print(p1.score,"p1 1 ",self.myBoard[0][int(0 if p1.score%6-1<0 else p1.score%6-1)])
                self.myBoard[0][int(0 if p1.score%6<0 else p1.score%6-1)]=p1.name
            else :
                # print(p1.score,"p1 2 ",self.myBoard[int(p1.score/6-1)][int(0 if p1.score%6-1<0 else p1.score%6-1)])
                self.myBoard[int(p1.score/6)][int(0 if p1.score%6-1<0 else p1.score%6-1)]=p1.name
                
                
            if p2.score/6-1<0:
                # print(p2.score,"p2 1 ",self.myBoard[0][int(0 if p2.score%6-1<0 else p2.score%6-1)])
                self.myBoard[0][int(0 if p2.score%6<0 else p2.score%6-1)]=p2.name
                
            else :
                # print(p2.score,"p2 1 ",self.myBoard[int(p2.score/6-1)][int(0 if p2.score%6-1<0 else p2.score%6-1)])
                self.myBoard[int(p2.score/6)][int(0 if p2.score%6-1<0 else p2.score%6-1)]=p2.name
                
                
            
            # for row in self.myBoard:
            #     for i,item in range(1,6),row:
            #         if item==row[i]:
                        
                    
            # print ("after",p1.score,p2.score)
            
            
            # print("p1",p1.score)
            # print("p2",p2.score)
            
            clear(0)      
            self.drawBoard()
            print(p1.name," score is ",p1.score)
            print(p2.name," score is ",p2.score)
            
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
                        return p.score
          else :
             return False
                        
game=SnakesAndLadders()





