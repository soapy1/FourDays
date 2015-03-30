'''
A game! (using python 3)
'''
from Person import Person
from Map import Map

title = '''
______              _         _   _            _ _  __     
|  _  \            (_)       | | | |          | (_)/ _|    
| | | |__ _ _   _   _ _ __   | |_| |__   ___  | |_| |_ ___ 
| | | / _` | | | | | | '_ \  | __| '_ \ / _ \ | | |  _/ _ \\
| |/ / (_| | |_| | | | | | | | |_| | | |  __/ | | | ||  __/
|___/ \__,_|\__, | |_|_| |_|  \__|_| |_|\___| |_|_|_| \___|
             __/ |                                         
            |___/                                          
'''

def intro():
    print(title) 
    money = 10
    health = 10
    player = Person(health, money)
    gender = input("are you a \n - boy [b] \n - girl [g] \n")
    if (gender == "b" or gender == "g"):
        if gender == "b":
            player.set_gender("boy")
        else:
            player.set_gender("girl")
    else:
        player.set_gender(None)
    name = input("what is your name: ")
    player.name = name
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

def story_intro(p):
    print("\n")
    print('Happy birthday to {0}, happy birthday to {0}'.format(p.get_name()))
    print('You are finally 10 years old!')
    input('')
    print('Father: {0}, you are no longer a little {1}. You need to get a job to help support the family'.format(p.get_name(), p.get_gender()))
    print('Mother: Ever since your older brother lost his arm at the factory the family has been suffering.')
    print('You: Yes father, I\'ll start working at the factory tomorrow')
    r = input ("\nready? ")

def main():
    m = Map()
    m.genMap()
    current_pos = m.mappola
    
    player = intro()
    story_intro(player)
    print_stats(player)
    game = True
    while game == True:
        if (player.money >= 20):
            print('it was a long and hard road but you escaped poverty.')
            print('YOU WIN')
            break
        if (player.health <= 0 or player.money <= 0):
            print ('\nGAME OVER'.format(player.health, player.money))
            break

        if (current_pos == {}):
            game = False
            print_stats(player)
            break
        
        if (current_pos['cond'] == "done"):
            m.genMap()
            current_pos = m.mappola
        elif (current_pos['cond'] == "challenge"):
            print("CHALLENGE: type {0} {1} time".format(current_pos['word'], current_pos['times']))
            if challenge(current_pos['word'], current_pos['times']):
                player.money += 1
                print("good job")
            else:
                player.health -= 1
                print("you fail")
            current_pos = current_pos['next']
        else: 
            print('\n' + current_pos['cond'])
            for i in current_pos['act']:
                print("  [{0}] {1}".format(i['opt'], i['val']))

            opt = input("\nwhat do you do? ").lower()

            if opt == "q":
                game = False
            elif opt == "stats":
                print_stats(player)
            elif opt == 'debug':
                print(current_pos)
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
                    player.money += 1
                else:
                    print("you fail")
                    player.health -= 1
            else:
                print(("you said {0}").format(opt))

if __name__ == "__main__":
    main()
