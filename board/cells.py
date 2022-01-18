from services.Player import *
from services.Screen import *
class Cells:
      #function to create list of rows
      def makeList(self,min,max,rowsNum):
           #initialize variables
           self.myBoard =list() 
           self.row =list() 
           self.__rowsNum =rowsNum
           self.__min=min
           self.__max=max
           
           for cell in range( self.__min,self.__max+1):
                  self.row.append(cell)
                  if cell%self.__rowsNum==0:
                        self.myBoard.append(self.row)
                        self.row=list()
           return self.myBoard 
     
      def drawBoard(self):
            # _____   _____   _____   _____   _____   _____
          for row in self.myBoard:
            s=('''            
                  |     | |     | |     | |     | |     | |     |
                  | %02s  | | %02s  | | %02s  | |  %02s | |  %02s | |  %02s | 
                  |_____| |_____| |_____| |_____| |_____| |_____|
                  '''%(row[0],row[1],row[2],row[3],row[4],row[5]))
            print(s,end="")

      def changePlayersPosition(self,p1=Player(""),p2=Player("")):
      #     print(self.myBoard)
          self.myBoard[int(p1.score/6)][int(p1.score%6-1)]="p1"
          self.myBoard[int(p2.score/6)][int(p2.score%6-1)]="p2"
          
          for row in self.myBoard:
                for cell in row:
                      if str(cell)==str(p1.score):
                            cell=p1.name
          Screen.clear(1)      
          self.drawBoard()
      #     print(self.myBoard)
            

cells=Cells()
# cells.makeList(1,31,6)
# cells.drawBoard()





