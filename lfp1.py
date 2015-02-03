'''
A game! (using python 3)
'''
from Person import Person

def intro():
    money = 10
    health = 10
    player = Person(health, money)
    gender = input("are you a \n - boy [b] \n - girl [g] \n")
    if (gender == "b" or gender == "g"):
        player.set_gender(gender)
    else:
        player.gener = "unknown"
    factory = input("\nare you in a: \n - shoe factory [s] \n - electronics factory [e] \n - clothing factory [c] \n")
    if (factory == "s" or factory == "e" or factory == "c"):
        player.factory(factory)
    else:
        player.factory = "unknown"
    return player

def main():
    player = intro()
    game = True
    while game == True:
        opt = input("\nwhat do you do? ").lower()
        if opt == "quit":
            game = False
        else:
            print(("you said {0}").format(opt))

if __name__ == "__main__":
    main()
