# player.py

class Player(object):

	def __init__(self, name):
	    self.name = name
	    self.lives = 3
        self.charges = 0
        
    def block(self, enemy_action):
        # enemy action interaction
        if enemy_action == 'kamehameha':
            self.lives -= 1

    def charge(self, enemy_action):
        # self action
        self.charges += 1
        
        # enemy action interaction
        if enemy_action == 'fire':
            self.lives -= 1 
        elif enemy_action == 'kamehameha':
            self.lives -= 3

    def fire(self, enemy_action):
        # self action
        self.charges -= 1
        
        # enemy action interaction
        if enemy_action == 'kamehameha':
            self.lives -= 2

    def kamehameha(self, enemy_action):
        # self action
        self.charges -= 3