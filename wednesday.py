from os import system
from time import sleep
clear= lambda : system ("clear")
x = chr (23637)
for i in range(100) :
    print(" " * i, x)
    sleep(0.01)
    clear()