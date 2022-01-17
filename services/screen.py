from os import system, name
from time import sleep

class Screen:
    def clear(s):
        sleep(int(s))
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')




screen=Screen()