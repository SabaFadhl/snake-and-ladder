from board import *
from services import *

# Create object for game from SnakesAndLadders class
game=SnakesAndLadders()

#create splash function to show starting of game
def splash():
    '''
    splash take no args\n
    it show box of game informatio\n
    return no value\n

    '''
    clear(0) #clear screen
    splashColor() # colord font in screen 
    
    #print box info
    print('''
           --------------------------
          | SNAKE AND LADDER GAME    |
          | Devloped by Saba ❤      |
          | T-MAHER....              |
          | t-Amal ...               |
           ------------------------- 
            Loading . . .
          ''')
    
    #sleep(2) and clear screan 
    clear(2)
    
def start():
    '''
    start function  take no args\n
    it take players names and start game\n
    it lanch the game\n
    return no value\n

    '''
    # Global objects of players
    global player1
    global player2
    
    #clear screen
    clear()
    
    #loop to take player 1 andvalidation it
    while True:
        try:
            player1name=input("Enter player 1 name : ")
            if validation.validString(player1name,3,7):#vallidation
                player1=Player(player1name)
                break
        except:
            print("Enter string !!!! ")
            
    #loop to take player 2 andvalidation it
    while True:
        try:
            player2name=input("Enter player 2 name : ")
            if validation.validString(player2name,3,7):#vallidation
                player2=Player(player2name)
                break
        except:
            print("Enter string !!!! ")
    
    
    #sleep(2) and clear screan         
    clear(1)
    
    #create borad list
    game.makeList(1,30,6)  
    
    #drawing borad
    game.drawBoard()
    
    # Calling dice until one is winner
    while True:
        #create two Dices
        dice1=Dice()
        dice2=Dice()
        print("\n")
        
        #roll Dices and store values 
        score1=dice1.roll(player1.name)
        score2=dice2.roll(player2.name)
        
        #Add scrors to player's scores
        player1.addScore(score1)
        player2.addScore(score2)
        
        #wait 1 second 
        sleep(1)
        
        # print("1,2",player1.score,player2.score)
        
        
        #Check if player 1 win
        if player1.score==30:
            clear(1)
            print('''
                    ---------------------------
                     %s ==========> Winner *_*
                    ---------------------------
                  '''%player1.name)
            break
        #Check if player 2 win
        elif player2.score==30:
            clear(1)
            print('''
                    ---------------------------
                     %s ==========> Winner *_*
                    ---------------------------
                  '''%player2.name)
            break
        
        #Clalling Change player position
        game.changePlayersPosition(player1,player2)
    
           
def end():
    '''
    end function  take no args\n
    it sleep and clear screen and colored font and print \n
    it lanch the game\n
    return no value\n

    '''
    #sleep(2) and clear screan 
    clear(2)
    splashColor()
    #sleep(2) and clear screan 
    clear(0)
    
    print('''
          * * *    *      *   *  *  *     
          *    *    *    *    *  
          * * *       *       *  *  *
          *    *      *       *
          * * *       *       *  *  *
           
           Devloped by Saba ❤    
           
          ''')
    
    #sleep(2) and clear screan 
    clear(2)




