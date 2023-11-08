"""
Today is Monday, the first of November, 2021
6:24 PM
"""

from time import sleep
from os import system

class labyrinth:
	map_matrix =\
	[
			[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
			[1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
			[1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
			[1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
	]

	map_start = [0, 2]
	map_end = [9, 8]
	map_with_player = None

	def player_in_map(self, player):
		self.map_with_player = self.map_matrix
		self.map_with_player[player.position[0]][player.position[1]] = 2

	def formated_map_print(self):
		counter = 0
		while counter < len(self.map_with_player):
			print(map_with_player[counter], "\n")
			counter += 1

class player:
	player_position = [0, 2]

	def can_move_up(self, map):
		if map.map_matrix[self.player_position[0] - 1][self.player_position[1]] == 0:
			return True
		else:
			return False

	def can_move_down(self, map):
		if map.map_matrix[self.player_position[0] + 1][self.player_position[1]] == 0:
			return True
		else:
			return False

	def can_move_right(self, map):
		if map.map_matrix[self.player_position[0]][self.player_position[1] + 1] == 0:
			return True
		else:
			return False

	def can_move_left(self, map):
		if map.map_matrix[self.player_position[0]][self.player_position[1] - 1] == 0:
			return True
		else:
			return False

	def move_up(self, map):
		if map.map_matrix[self.player_position[0] - 1][self.player_position[1]] == 0:
			self.player_position[0] -= 1

	def move_down(self, map):
		if map.map_matrix[self.player_position[0] + 1][self.player_position[1]] == 0:
			self.player_position[0] += 1

	def move_right(self, map):
		if map.map_matrix[self.player_position[0]][self.player_position[1] + 1] == 0:
			self.player_position[1] += 1

	def move_left(self, map):
		if map.map_matrix[self.player_position[0]][self.player_position[1] - 1] == 0:
			self.player_position[1] -= 1

"""
Today is Monday, the first of November, 2021
6:27 PM
Matrix created and pausing for having dinner
6:46 PM
Starting logic part (i'ma suffer)
6:53 PM
First, I will make a basic movement algorithm
7:35 PM
I re-wrote all in classes. Now I have the labyrinth and player classes. This is 0.0
"""