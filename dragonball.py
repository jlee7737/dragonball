# dragonball.py

from player import Player
import time

# game setup
game_over = 0
round_counter = 1
p1_name = input("Hello Saiyan1, welcome to Earth, what is your name? ")
p2_name = input("Hello Saiyan2, welcome to Earth, what is your name? ")
p1 = Player(p1_name)
p2 = Player(p2_name)

def print_title(p1_name, p2_name):
    spacer = 46 - (len(p1_name) + len(p2_name))
    print ("==================================================")
    print (" "*int(spacer/2) + p1_name + " VS " + p2_name      )
    print ("                      ~ · ~                       ")
    print ("              LET THE BATTLE BEGIN!               ")
    print ("==================================================")
    time.sleep(1)

def print_round():
    global round_counter
    print ("ROUND " + str(round_counter) + "!")
    print ("------------------------------")
    round_counter += 1
# game setup ends

# game starts
print_title(p1.name, p2.name)
while game_over != 1:
    #new round starts
    print_round()
    p1_action = p1.play_action()
    p2_action = p2.play_action()
    
    p1.action_dispatcher[p1_action](p2_action)
    p2.action_dispatcher[p2_action](p1_action)
    
    print ("...fighting...")
    time.sleep(2)
    print ("")
    print ("END OF ROUND STATS:")
    print ("{} - lives:{}, charges:{} ".format(p1.name, p1.lives, p1.charges))
    print ("{} - lives:{}, charges:{} ".format(p2.name, p2.lives, p2.charges))
    print ("------------------------------")
    print ("")
    time.sleep(2)
    
    if p1.lives == 0:
        game_over = 1
        print ("GAME OVER! {} wins".format(p2.name))
    elif p2.lives == 0:
        game_over = 1
        print ("GAME OVER! {} wins".format(p1.name))
# game ends





class DragonBall(object):
    '''
    DragonBall class defines game to run dragonball game.
    '''

    def __init__(self):
        return 1

    def start_game():
        return 1