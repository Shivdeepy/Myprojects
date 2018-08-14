import time
import sys

class Game(object):
    print("\nWelcome to Quiz Game \n")
    y = "WARNING! This Game is Full of Risk. Continue on your Own Risk"
    
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
    delay_print(y)
		
print("\nTo Continue press 1 and to get out press 0 ")
x = input("> ")

class Game1(object):
    print("Welcome Game 1.:This will tell you without asking any data from you.\n")
    y = "\t\tThink any number in your mind."
    Game.delay_print(y)
    input()
    x = "\t\tThink same number for your friend. And add them. "
    Game.delay_print(x)
    input()
    a = "\t\tEnter any number from my side and add it to the sum above."
    Game.delay_print(a)
    z = int(input("\t\t"))
    b = "\t\tGive half to GOD. And minus your friends share."
    Game.delay_print(b)
    input()
    print("You have left with ",z/2)
    
