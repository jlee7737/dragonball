from player import Player
import time


class DragonBall(object):
    '''
    DragonBall class defines game to run dragonball game.
    '''

    game_over = 0
    round_count = 1


    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    def setup_game():
        """
        Set up DragonBall game with two Player instances 'p1' and 'p2'.
        
        Returns:
            DragonBall instance
        """
        print("Hello Saiyans, welcome to Earth!")
        p1_name = input("Saiyan1, what is your name? ")
        p2_name = input("Saiyan2, what is your name? ")
        p1 = Player(p1_name)
        p2 = Player(p2_name)

        dragonball = DragonBall(p1, p2)
        
        return dragonball


    def print_title(self):
        p1 = self.player1
        p2 = self.player2

        spacer = 46 - (len(p1.name) + len(p2.name))
        print ("==================================================")
        print (" "*int(spacer/2) + p1.name + " VS " + p2.name      )
        print ("                      ~ · ~                       ")
        print ("               LET THE FIGHT BEGIN!               ")
        print ("==================================================")
        print ("")
        time.sleep(1)


    def play_round(self):
        p1 = self.player1
        p2 = self.player2

        print ("                     ROUND " + str(DragonBall.round_count))
        print ("--------------------------------------------------")
        DragonBall.round_count += 1

        p1_action = p1.play_action()
        p2_action = p2.play_action()
        p1.action_dispatcher[p1_action](p2_action)
        p2.action_dispatcher[p2_action](p1_action)
        
        print ("                 ...fighting...                 \n")
        time.sleep(1)
        print ("ROUND STATS:")
        print (" {} - lives:{}, charges:{} ".format(p1.name, p1.lives, p1.charges))
        print (" {} - lives:{}, charges:{} ".format(p2.name, p2.lives, p2.charges))
        print ("\n")
        time.sleep(1)
        
        if p1.lives == 0 or p2.lives ==0:
            DragonBall.game_over = 1
            print ("                   GAME OVER!                     ")
            if p1.lives == 0:
                print ("{} wins!".format(p2.name))
            else:
                print ("{} wins!".format(p1.name))


    def start_game(self):
        self.print_title()
        while DragonBall.game_over != 1:
            self.play_round()
            


