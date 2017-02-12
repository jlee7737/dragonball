# player.py

class Player(object):

	def __init__(self, name):
	    self.name = name
	    self.lives = 3
        self.charges = 0
        
    def block(self, enemy_action):
        # enemy action interaction
        if enemy_action == 'KAMEHAMEHA':
            self.lives -= 1
        
        return 'BLOCK'

    def charge(self, enemy_action):
        # self action
        self.charges += 1
        
        # enemy action interaction
        if enemy_action == 'FIRE':
            self.lives -= 1 
        elif enemy_action == 'KAMEHAMEHA':
            self.lives -= 3
            
        return 'CHARGE'

    def fire(self, enemy_action):
        # self action
        self.charges -= 1
        
        # enemy action interaction
        if enemy_action == 'KAMEHAMEHA':
            self.lives -= 2
            
        return 'FIRE'

    def kamehameha(self, enemy_action):
        # self action
        self.charges -= 3
        
        return 'KAMEHAMEHA'