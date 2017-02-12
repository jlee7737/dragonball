# player.py
import getpass

class Player(object):
    '''
    Player class defines dragonball game player.
    '''
    
    action_dict = {'b': 'BLOCK',
                   'c': 'CHARGE',
                   'f': 'FIRE',
                   'k': 'KAMEHAMEHA'}

    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.charges = 0
        self.action_dispatcher = {'BLOCK': self.block, 
                                  'CHARGE': self.charge,
                                  'FIRE': self.fire,
                                  'KAMEHAMEHA': self.kamehameha}
        
    def play_action(self):
        '''
        Player chooses action based on action_dict and current player stats.
        
        Action choice input with getpass for hiding action choices
        during player turns.
        '''
        valid_action = 0
        while valid_action == 0:
            self.show_available_actions()
            
            action_choice = getpass.getpass(" " + self.name + ", what's your move? ")
            
            valid_action = self.validate_action(action_choice)
            
        return Player.action_dict[action_choice]
    
    def show_available_actions(self):
        '''
        Prints out player's currently available valid actions depending on 
        player current stats.
        '''
        print (" {}'s available moves:".format(self.name))
        print ("  b: BLOCK")
        print ("  c: CHARGE")
        if self.charges >= 1:
            print ("  f: FIRE")
            if self.charges >= 3:
                print ("  k: KAMEHAMEHA")
    
    def validate_action(self, action_choice):
        '''
        Validates player's action depending on current stats.
        
        Function takes in player's action choice from options in action_dict.
        
        Returns 1 if action is valid, 0 if invalid.
        '''
        if action_choice in ['b', 'c']:
            return 1
        elif action_choice == 'f':
            if self.charges >= 1:
                return 1
            else:
                return 0
        elif action_choice == 'k':
            if self.charges >= 3:
                return 1
            else:
                return 0
        else:
            print (" * Invalid choice! Choose again...")
            return 0
    
    def block(self, enemy_action):
        # action result
        # no changes

        # enemy action result
        if enemy_action == 'KAMEHAMEHA':
            self.lives -= 1

    def charge(self, enemy_action):
        # action result
        self.charges += 1
        
        # enemy action result
        if enemy_action == 'FIRE':
            self.lives -= 1 
        elif enemy_action == 'KAMEHAMEHA':
            self.lives -= 3

    def fire(self, enemy_action):
        # action result
        self.charges -= 1
        
        # enemy action result
        if enemy_action == 'KAMEHAMEHA':
            self.lives -= 2

    def kamehameha(self, enemy_action):
        # action result
        self.charges -= 3
        
        # enemy action result
        # no changes
