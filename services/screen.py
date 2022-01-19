from os import system, name
from termcolor import colored
import os

from time import sleep

def clear(s=0):
    '''
        clear take s => number  \n
        it clear screen with sleep (s) \n
        return no args \n
    '''
    sleep(int(s))
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def playerName(name):
    '''
        playerName take name => string  \n
        it change color of font \n
        return colored string \n
    '''
    return colored(name, 'cyan')

def snakenum(num):
    '''
        snakenum take num => int  \n
        it change color of font of num\n
        return colored string \n
    '''
    return colored(num, 'red')

def ladderNum(num):
    '''
        ladderNum take num => int  \n
        it change color of font of num\n
        return colored string \n
    '''
    return colored(num, 'green')

def normalNum(num):
    '''
        ladderNum take num => int  \n
        it change color of font of num\n
        return colored string \n
    '''
    return colored(num, 'white')

def snake():
    '''
        snake take no args  \n
        it change color of font of screen and return to white\n
        return no args\n
    '''
    os.system('color e')
    sleep(1)
    os.system('color 7')
    
def ladder():
    '''
        ladder take no args  \n
        it change color of font of screen and return to white\n
        return no args\n
    '''
    os.system('color a')
    sleep(1)
    os.system('color 7')

def splashColor():
    '''
        splashColor take no args  \n
        it change color of font of screen and return to white\n
        return no args\n
    '''
    os.system('color d')

# screen=Screen()
# screen.snake()
# print(len(ladderNum(3)))
# print(len("3"))