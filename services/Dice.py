import keyboard
from random import randint

class Dice:
    def __init__(self) :
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
                
    def roll(self):
        
        print("press any key to roll :")
        keyboard.read_key()
        
        no = randint(self.min,self.max)
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
            
        return no




dice=Dice()
# a=dice.roll()  
# print(a) 
