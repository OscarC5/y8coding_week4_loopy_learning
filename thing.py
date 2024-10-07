from os import system

from time import sleep

x = 0x1F600
while True:
    j = 0
    for _ in range (10):
        for _ in range (10):
            print(chr(j+x), end="")
            j += 1
        print()
    sleep(0.01)
    system("cls")
    x += 1