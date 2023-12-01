,,,
Thanks to TheLPro for this script
Loading bar for the script, able to make loading time more apparent.
,,,
from termcolor import colored
from time import sleep
import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

    
class Bar:
        
    b = "█"
    d = "•"
    c = "light_green"
    s = random.randint(1, 5) / 100
    current = 0

    def bar(char):
        Bar.b = char
    def fill(char):
        Bar.d = char
    def color(color):
        Bar.c = color
    def speed(min, max, divider):
        Bar.speed = random.randint(min, max) / divider

    def update(percent, last):
        current = last
        for i in range(percent - last + 1):
            if current == 0 or current == 1:
                boxes = 0
                dots = 50
            else:
                boxes = round(current / 2)
                dots = round((100 - current) / 2)
            cls()
            print(colored(f"Loading {current + 1}% {Bar.b*boxes}{Bar.d*dots}", Bar.c))
            sleep(Bar.s)
            current += 1
            if current == 100:
                return True
Bar.update(100, 0)
