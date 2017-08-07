import unittest


class TestPlayer(unittest.TestCase):

	# why _makeOne() instead of setUp()?
	# to keep instance attributes consistent
	def setUp(self):
		from dragonball.player import Player
		self.player = Player('bob', 3, 1)

	def _makeOne(self):
		from dragonball.player import Player
		return Player('bob', 3, 1)


	# test_block_<enemy_action>
	#.........................................................................#
	def test_block_BLOCK(self):
		instance = self._makeOne()
		instance.block('BLOCK')

		expected = 3
		self.assertEquals(instance.lives, expected)

	def test_block_CHARGE(self):
		instance = self._makeOne()
		instance.block('CHARGE')

		expected = 3
		self.assertEquals(instance.lives, expected)

	def test_block_FIRE(self):
		instance = self._makeOne()
		instance.block('FIRE')

		expected = 3
		self.assertEquals(instance.lives, expected)

	def test_block_KAMEHAMEHA(self):
		instance = self._makeOne()
		instance.block('KAMEHAMEHA')

		expected = 2
		self.assertEquals(instance.lives, expected)


	# test_charge_<enemy_action>
	#.........................................................................#
	def test_charge_BLOCK(self):
		instance = self._makeOne()
		instance.charge('BLOCK')

		expected_lives = 3
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 2
		self.assertEquals(instance.charges, expected_charges)

	def test_charge_CHARGE(self):
		instance = self._makeOne()
		instance.charge('CHARGE')

		expected_lives = 3
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 2
		self.assertEquals(instance.charges, expected_charges)

	def test_charge_FIRE(self):
		instance = self._makeOne()
		instance.charge('FIRE')

		expected_lives = 2
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 2
		self.assertEquals(instance.charges, expected_charges)

	def test_charge_KAMEHAMEHA(self):
		instance = self._makeOne()
		instance.charge('KAMEHAMEHA')

		expected_lives = 0
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 2
		self.assertEquals(instance.charges, expected_charges)


	# test_fire_<enemy_action>
	#.........................................................................#
	def test_fire_BLOCK(self):
		instance = self._makeOne()
		instance.fire('BLOCK')

		expected_lives = 3
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 0
		self.assertEquals(instance.charges, expected_charges)

	def test_fire_CHARGE(self):
		instance = self._makeOne()
		instance.fire('CHARGE')

		expected_lives = 3
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 0
		self.assertEquals(instance.charges, expected_charges)

	def test_fire_FIRE(self):
		instance = self._makeOne()
		instance.fire('FIRE')

		expected_lives = 3
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 0
		self.assertEquals(instance.charges, expected_charges)

	def test_fire_KAMEHAMEHA(self):
		instance = self._makeOne()
		instance.fire('KAMEHAMEHA')

		expected_lives = 1
		self.assertEquals(instance.lives, expected_lives)
		expected_charges = 0
		self.assertEquals(instance.charges, expected_charges)
