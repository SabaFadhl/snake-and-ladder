from services.Player import *
from services.Screen import *
class Cells:
      def __init__(self):
         self.myBoard =list() 
         self.row =list()    
      #function to create list of rows
      def makeList(self,min,max,rowsNum):
           #initialize variables
           self.myBoard =list() 
           self.row =list() 
           self._rowsNum =rowsNum
           self._min=min
           self._max=max
           
           for cell in range( self._min,self._max+1):
                  self.row.append(cell)
                  if cell%self._rowsNum==0:
                        self.myBoard.append(self.row)
                        self.row=list()
           return self.myBoard 
     
      def drawBoard(self):
            # _____   _____   _____   _____   _____   _____
          for row in self.myBoard:
                
            # if self.myBoard[1]==row:
            #    s=('''            
            #                   |     | |     | |     | |     | |     | |     |
            #                   |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s} | |  {:2s} | |  {:2s} |
            #                   |_____| |_____| |_____| |_____| |_____| |_____|
            #                   '''.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),))
            # elif self.myBoard[0]==row:
            #        s=('''            
            #                   |     | |     | |     | |     | |     | |     |
            #                   |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  |
            #                   |_____| |_____| |_____| |_____| |_____| |_____|
            #                   '''.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),))
            # else:
            #       s=('''            
            #                   |     | |     | |     | |     | |     | |     |
            #                   |  {:2s} | |  {:2s} | |  {:2s} | |  {:2s} | |  {:2s} | |  {:2s} |
            #                   |_____| |_____| |_____| |_____| |_____| |_____|
            s=('''            
                  
                     {:2s}    {:2s}    {:2s}    {:2s}    {:2s}    {:2s}
                  
                  '''.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),))
                                     
                       
            
            
            # s=('''            
            #       |     | |     | |     | |     | |     | |     |
            #       |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  | |  {:2s}  |
            #       |_____| |_____| |_____| |_____| |_____| |_____|
            #       '''.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),))
            # s=('''            
            #        |              | |              | |              | |              | |              | |              |
            #       ''')
            # s+=" |{0:^5}| |{1:^5}| |{2:^5}| |{3:^5} |{4:^5}| |{5:^5}|".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]))   
            # s+=('''|______________| |______________| |______________| |______________| |______________| |______________| 
            #       ''')
            print(s,end="")

      def changePlayersPosition(self,p1=Player(""),p2=Player("")):
          clear(0)
          self.makeList(self._min,self._max,self._rowsNum)
          self.myBoard[int(p1.score/6)][int(p1.score%6-1)]="p1"
          self.myBoard[int(p2.score/6)][int(p2.score%6-1)]="p2"
          
          clear(0)      
          self.drawBoard()
      

cells=Cells()
# cells.makeList(1,31,6)
# cells.drawBoard()





