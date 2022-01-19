from os import system, name
from termcolor import colored
import os

from time import sleep

def clear(s):
    sleep(int(s))
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def playerName(name):
    return colored(name, 'cyan')
def snakenum(num):
    return colored(num, 'red')
def ladderNum(num):
    return colored(num, 'green')
def normalNum(num):
    return colored(num, 'white')

def snake():
    os.system('color e')
    sleep(1)
    os.system('color 7')
    
def ladder():
    os.system('color a')
    sleep(1)
    os.system('color 7')

def splashColor():
    os.system('color d')

# screen=Screen()
# screen.snake()
# print(len(ladderNum(3)))
# print(len("3"))