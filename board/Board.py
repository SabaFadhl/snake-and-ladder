from board import *
from services import *

game=SnakesAndLadders()

def splash():
    # clear(0)
    splashColor()
    
    clear(0)

    print('''
           --------------------------
          | SNAKE AND LADDER GAME    |
          | Devloped by Saba ❤      |
          | T-MAHER....              |
          | t-Amal ...               |
           ------------------------- 
            Loading . . .
          ''')
    clear(2)


def start():
    global player1
    global player2
    clear(0)
    while True:
        try:
            player1name=input("Enter player 1 name : ")
            if validation.validString(player1name,3,7):
                player1=Player(player1name)
                break
        except:
            print("Enter string !!!! ")
    
    while True:
        try:
            player2name=input("Enter player 2 name : ")
            if validation.validString(player2name,3,7):
                player2=Player(player2name)
                break
        except:
            print("Enter string !!!! ")
            
    clear(1)
    game.makeList(1,30,6)  
    game.drawBoard()
    
    while True:
        dice1=Dice()
        dice2=Dice()
        print("\n")
        
        score1=dice1.roll(player1.name)
        
        score2=dice2.roll(player2.name)
        
        player1.addScore(score1)
        player2.addScore(score2)
        sleep(2)
        
        # print("1,2",player1.score,player2.score)
        
        
        
        if player1.score==30:
            clear(1)
            print('''
                    ----------------------
                     %s ==========> Winner *_*
                    -----------------------
                  '''%player1.name)
            break
        elif player2.score==30:
            clear(1)
            print('''
                    ----------------------
                     %s ==========> Winner *_*
                    -----------------------
                  '''%player2.name)
            break
        
           
def end():
    clear(2)
    splashColor()
    clear(0)
    print('''
          * * *    *      *   *  *  *     
          *    *    *    *    *  
          * * *       *       *  *  *
          *    *      *       *
          * * *       *       *  *  *
           
           Devloped by Saba ❤    
           
          ''')
    
  
    clear(2)




