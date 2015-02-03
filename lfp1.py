'''
A game! (using python 3)
'''
from Person import Person

game_path = {
    'cond':'You need to wake up to get to work',
     'act': [
        {
            'opt':1, 
            'val': 'wake up at 7am', 
            'pre':[], 
            'next': 
                {
                    'cond': 'you need to get to work',
                    'act': [
                        {
                            'opt':1,
                            'val':'walk',
                            'pre':[],
                            'next':{}
                        },
                        {
                            'opt':2,
                            'val':'run',
                            'pre':[],
                            'next':{}
                        }
                    ]
                }
        },
        {
            'opt':2, 
            'val': 'wake up at 6am', 
            'pre':[], 
            'next': 
                {
                    'cond': 'you need to get to work',
                    'act': [
                        {
                            'opt':1,
                            'val':'walk',
                            'pre':[],
                            'next':{}
                        },
                        {
                            'opt':2,
                            'val':'run',
                            'pre':[],
                            'next':{}
                        }
                    ]
                }
        }
    ]
}

def intro():
    money = 10
    health = 10
    player = Person(health, money)
    gender = input("are you a \n - boy [b] \n - girl [g] \n")
    if (gender == "b" or gender == "g"):
        player.set_gender(gender)
    else:
        player.set_gener(None)
    factory = input("\nare you in a: \n - shoe factory [s] \n - electronics factory [e] \n - clothing factory [c] \n")
    if (factory == "s" or factory == "e" or factory == "c"):
        player.set_factory(factory)
    else:
        player.set_factory(None)
    return player


def intro2():
    return Person(10,10)

def challenge(word, num):
    user_words = 0
    while (user_words < num):
        val = input("type '{0}' then enter ".format(word));
        if (val == word):
            user_words += 1
        else:
            return False
    return True

def print_stats(p):
    print("\nYOU:")
    print(" - have {0} dollars".format(p.get_money()))
    print(" - have {0} health\n".format(p.get_health()))


def main():

    current_pos = game_path
    player = intro2()
    print_stats(player)
    game = True
    while game == True:
        print('\n' + current_pos['cond'])
        for i in current_pos['act']:
            print(" - [{0}] {1}".format(i['opt'], i['val']))


        opt = input("\nwhat do you do? ").lower()

        if opt == "quit":
            game = False
        elif opt in ['1','2','3','4','5']:
            for i in current_pos['act']:
                if (int(opt) == i['opt']):
                    current_pos = i['next']
        elif opt == "work":
            if challenge('work', 10):
                print("good job for today")
            else:
                print("you fail")
        else:
            print(("you said {0}").format(opt))

if __name__ == "__main__":
    main()
