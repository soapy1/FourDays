'''
A game! (using python 3)
'''
from Person import Person
from Map import Map

game_path = {
    'cond':'You need to wake up to get to work',
    'act': [
        {
            'opt':1, 
            'outcome': None,
            'val': 'wake up at 7am', 
            'pre':[], 
            'next': 
                {
                    'cond': 'you need to get to work',
                    'act': [{
                            'opt':1,
                            'outcome': 'Manager is mad. You get beat.', 
                            'val':'walk',
                            'pre':[],
                            'next':{
                                'cond': 'challenge',
                                'word': 'sorry',
                                'times': 10,
                                'next': 
                                    {
                                        'cond': 'You start to work',
                                        'act': [
                                            {
                                                'opt':1,
                                                'outcome': None,
                                                'val':'walk',
                                                'pre':[],
                                                'next':{
                                                    'cond': '',
                                                    'act': []
                                                }
                                            },
                                            {
                                                'opt':2,
                                                'outcome': None,
                                                'val':'run',
                                                'pre':[],
                                                'next':{
                                                    'cond': '',
                                                    'act': []
                                                }
                                            }
                                        ]
                                    }
                            }
                        },
                        {
                            'opt':2,
                            'outcome': None,
                            'val':'run',
                            'pre':[],
                            'next':{
                                'cond': '',
                                'act': []
                            }
                        }
                    ]
                }
        },
        {
            'opt':2, 
            'outcome': None,
            'val': 'wake up at 6am', 
            'pre':[], 
            'next': 
                {
                    'cond': 'you need to get to work',
                    'act': [
                        {
                            'opt':1,
                            'outcome': None,
                            'val':'walk',
                            'pre':[],
                            'next':{
                                'cond': '',
                                'act': []
                            }
                        },
                        {
                            'opt':2,
                            'outcome': None,
                            'val':'run',
                            'pre':[],
                            'next':{
                                'cond': '',
                                'act': []
                            }
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

def story_intro():
    print("\n")
    print("It's a scoldering hot day!\n ")

def main():
    m = Map()
    m.genMap()
    current_pos = m.mappola
    
#    story_intro()
    player = intro2()
    print_stats(player)
    game = True
    while game == True:
        if (current_pos == {}):
            game = False
            print_stats(player)
            break
        
        if (current_pos['cond'] == "challenge"):
            print("CHALLENGE: type {0} {1} time".format(current_pos['word'], current_pos['times']))
            if challenge(current_pos['word'], current_pos['times']):
                print("good job")
            else:
                print("you fail")
            current_pos = current_pos['next']
        else: 
            print('\n' + current_pos['cond'])
            for i in current_pos['act']:
                print(" - [{0}] {1}".format(i['opt'], i['val']))

            opt = input("\nwhat do you do? ").lower()

            if opt == "q":
                game = False
            elif opt == "stats":
                print_stats(player)
            elif opt == 'debug':
                for i in current_pos['act']:
                    print(i['outcome'])
            elif opt in ['1','2','3','4','5']:
                for i in current_pos['act']:
                    if (int(opt) == i['opt']):
                        player.health += i['health']
                        player.money += i['money']
                        if (i['outcome']):
                            print('\n' + i['outcome'] + '\n')
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
