from os import system
from time import sleep
clear = lambda : system("clear")

# clear()
# sleep(0.5)
# print("""🫥Oscar's
#       """)
# sleep(1)
# print("""         😵Horror
#       """)
# sleep(1)
# print("""                 😄Emoji
#       """)
# sleep(1)
# print("""                        🎉Hilarity
#       """)                                        
# sleep(1)
clear()
a = """

"""
b = a*5
print("customize your monster!")
print(a*2)
name = input("insert name here:   ")
print("pick a monster")
sleep (0.5)
print("""
      zombie🧟‍♂️
      skeleton💀
      vampire🧛‍♂️
      ghost👻
      """)
sleep(0.5)
monstername= input("tipe the name of one of the monsters above!(whitout emoji)")
if monstername == "zombie":
    monster = "🧟‍♂️"
elif monstername == "skeleton":
    monster = "💀"
elif monstername == "vampire":
    monster = "🧛‍♂️"
elif monstername == "ghost":
    monster = "👻"
else:
    print("sorry, that is not a monster. your monster is now a ghost")
    monster = "👻"
    monstername = "ghost"
clear()
print("There was one a dude named",name,)
sleep(1.5)
print(name,"decided to go for a walk")

for i in range(100):
      clear()
      print(b)
      print(' ' * i + "😐")    
      sleep(0.1)