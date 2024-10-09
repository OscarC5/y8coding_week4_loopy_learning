from os import system

from time import sleep
clear = lambda : system("clear")

x = 0x1F600
while True:
    j = 0
    for _ in range (10):
        for _ in range (10):
            print(chr(j+x), end="")
            j += 1
        print()
    sleep(0.00001)
    clear()
    x += 1