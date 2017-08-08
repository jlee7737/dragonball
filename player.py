from getpass import getpass


class Player(object):
    '''
    Player class defines dragonball game player.
    '''
    
    action_dict = {
        'b': 'BLOCK',
        'c': 'CHARGE',
        'f': 'FIRE',
        'k': 'KAMEHAMEHA',
        }

    
    def __init__(self, name, lives, charges):
        self.name = name
        self.lives = lives
        self.charges = charges
        self.action_dispatcher = {
            'b': self.block, 
            'c': self.charge,
            'f': self.fire,
            'k': self.kamehameha,
            }


    def show_available_actions(self):
        '''
        Prints out player's currently available valid actions based on 
        player instance's current stats.
        '''

        print (" {}'s available moves:".format(self.name))
        print ("  b: BLOCK")
        print ("  c: CHARGE")
        if self.charges >= 1:
            print ("  f: FIRE")
        if self.charges >= 3:
            print ("  k: KAMEHAMEHA")


    def play_action(self):
        '''
        Player chooses action input based on action_dict and player 
        instance's current stats.

        Returns:
            action (Str): string value returned from action_dict key:value
        '''

        action_is_valid = False
        while action_is_valid == False:
            self.show_available_actions()
            
            # uses 'getpass' to hide input during player's turn
            action_input = getpass(" " + self.name + ", what's your move? \n")
            
            action_is_valid = self.validate_input(action_input)
            
        return action_input


    def validate_input(self, action_input):
        '''
        Validates player's action input depending on player instance's 
        current stats.
        
        Args:
            action_input (Str): player's action input choice that maps 
                to Player object attribute action_dict 
        Returns:
            result (Bool): If action is valid for player, return True,
                otherwise, return False.
        '''
        result = False
        action_input = action_input.lower()

        if action_input in ['b', 'c']:
            result = True
        elif action_input == 'f':
            if self.charges >= 1:
                result = True
        elif action_input == 'k':
            if self.charges >= 3:
                result = True
        else:
            print ("* Invalid choice! Choose again...")

        return result


    def block(self, enemy_action):
        """
        Player's BLOCK action.
        """

        # action result

        # enemy action result
        if enemy_action == 'k':
            self.lives -= 1


    def charge(self, enemy_action):
        """
        Player's CHARGE action.
        """

        # action result
        self.charges += 1
        
        # enemy action result
        if enemy_action == 'f':
            self.lives -= 1 
        elif enemy_action == 'k':
            self.lives -= 3


    def fire(self, enemy_action):
        """
        Player's FIRE action.
        """

        # action result
        self.charges -= 1
        
        # enemy action result
        if enemy_action == 'k':
            self.lives -= 2


    def kamehameha(self, enemy_action):
        """
        Player's KAMEHAMEHA action.
        """

        # action result
        self.charges -= 3
        
        # enemy action result