from os import system, name
from time import sleep

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

mycells =list()
row=list()
for cell in range(1,31):
      row.append(cell)
      if cell%6==0:
            mycells.append(row)
            row=list()
            
squre=[]
def cell(cells):
      for row in cells:
        s=('''
           _____   _____   _____   _____   _____   _____
          |     | |     | |     | |     | |     | |     |
          | %02d  | | %02d  | | %02d  | |  %02d | |  %02d | |  %02d | 
          |_____| |_____| |_____| |_____| |_____| |_____|
        '''%(row[0],row[1],row[2],row[3],row[4],row[5]))
        print(s,end="")


cell(mycells)
sleep(1)
screen_clear()
print(mycells)