import keyboard
from random import randint

class Dice:
    '''
            Dice class to mange Dice of Game\n
    '''
    def __init__(self) :
        '''
            constractor take no args\n
            it initialise min and max\n
            return no value\n

         '''
        self.__min=int(1)
        self.__max=int(6)
        
    @property
    def min(self):
        return self.__min
    
    @min.setter
    def min(self,min):
        self.__min=min
    @property
    def max(self):
        return self.__max
    
    @max.setter
    def max(self,min):
        self.__max=max
                
    def roll(self,name):
        '''
            roll take name => name of player \n
            it roll up random dice \n
            return no=>number \n
        '''
        print("%s press any key to roll : "%name)
        # keyboard.read_key()
        input()
        #Generate random number beteen[min,max]
        no = randint(self.min,self.max)
        #draw Dices
        if no == 1:
            print(" _____")
            print("|     |")
            print("|  0  |")
            print("|     |")
            print("|_____|")
        elif no == 2:
            print(" _____")
            print("|     |")
            print("| 0 0 |")
            print("|     |")
            print("|_____|")
        elif no == 3:
            print(" _____")
            print("|  0  |")
            print("|  0  |")
            print("|  0  |")
            print("|_____|")
        elif no == 4:
            print(" _____")
            print("| 0 0 |")
            print("|     |")
            print("| 0 0 |")
            print("|_____|")
        elif no == 5:
            print(" _____")
            print("| 0 0 |")
            print("|  0  |")
            print("| 0 0 |")
            print("|_____|")
        elif no == 6:
            print(" _____")
            print("| 0 0 |")
            print("| 0 0 |")
            print("| 0 0 |")
            print("|_____|")
       
        # keyboard.remove_all_hotkeys
        return no





# a=dice.roll()  
# print(a) 
