from services.Player import *
from services.Screen import *
class Cells:
      '''
            Cells class to mange cells of board\n
           
      '''
      def __init__(self):
         '''
            constractor take no args\n
            it initialise cells list\n
            return no value\n

         '''
         self.myBoard =list() 
         self.row =list()    
      #function to create list of rows
      def makeList(self,min,max,rowsNum):
           '''
                  makeList take min => start number of cells and max => end number of cells \n
                  it build cells board list\n
                  return cells list\n
           '''
           #initialize variables
           self.myBoard =list() 
           self.row =list() 
           self._rowsNum =rowsNum
           self._min=min
           self._max=max
           # loops throw rows in cells and create it
           for cell in range( self._min,self._max+1):
                  self.row.append(cell)
                  if cell%self._rowsNum==0:
                        self.myBoard.append(self.row)
                        self.row=list()
           return self.myBoard 
     
      def drawBoard(self):
          '''
                  makedrawBoard take no Args \n
                  it draw  board using cell list\n
                  return cells list\n
           '''
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
                  '''.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5])))
                                     
                       
            
            
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
            
          print("\n")

      def changePlayersPosition(self,p1,p2):
            #abstract method will implemets in child
            pass
game=Cells()
# cells.makeList(1,31,6)
# cells.drawBoard()





