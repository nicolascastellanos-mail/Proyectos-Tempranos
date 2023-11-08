"""
Today is Monday, the first of November, 2021
6:24 PM
"""

from time import sleep
from os import system
from random import randint

def coordinate(coords):
	return [coords[1], coords[0]]

class labyrinth:
	map_matrix =\
	[
			["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
			["N", "O", "O", " ", "O", "O", "O", "O", " ", " ", "O", "O", "O", "N"],
			["N", "O", "O", " ", "O", " ", " ", " ", " ", "O", "O", "O", "O", "N"],
			["N", "O", "O", " ", "O", " ", "O", "O", "O", "O", "O", "O", "O", "N"],
			["N", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "N"],
			["N", "O", "O", "O", "O", " ", "O", "O", " ", " ", " ", "O", "O", "N"],
			["N", "O", "O", "O", "O", " ", "O", "O", " ", "O", " ", "O", "O", "N"],
			["N", "O", "O", "O", "O", " ", "O", "O", " ", "O", " ", "O", "O", "N"],
			["N", "O", "O", "O", "O", " ", " ", " ", " ", "O", " ", "O", "O", "N"],
			["N", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", "O", "N"],
			["N", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", "O", "O", "N"],
			["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"]
	]

	solution_number = 0
	map_start = None
	map_end = None
	map_with_player = None

	def __init__(self):
		self.map_start = coordinate([3, 1])
		self.map_end = coordinate([11, 10])
		self.map_with_player = self.map_matrix

	def player_in_map(self, player):
		self.map_with_player = self.map_matrix
		self.map_with_player[player.player_position[0]][player.player_position[1]] = "P"

	def formated_map_print(self):
		counter = 0
		while counter < len(self.map_with_player):
			print(self.map_with_player[counter], "\n")
			counter += 1

class player:
	player_position = None

	def __init__(self, labyrinth_map):
		self.player_position = labyrinth_map.map_start

	def can_move_up(self, labyrinth_map):
		if labyrinth_map.map_with_player[self.player_position[0] - 1][self.player_position[1]] not in ["O", "N", str(my_labyrinth.solution_number)]:
			return True
		else:
			return False

	def can_move_down(self, labyrinth_map):
		if labyrinth_map.map_with_player[self.player_position[0] + 1][self.player_position[1]] not in ["O", "N", str(my_labyrinth.solution_number)]:
			return True
		else:
			return False

	def can_move_right(self, labyrinth_map):
		if labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1] + 1] not in ["O", "N", str(my_labyrinth.solution_number)]:
			return True
		else:
			return False

	def can_move_left(self, labyrinth_map):
		if labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1] - 1] not in ["O", "N", str(my_labyrinth.solution_number)]:
			return True
		else:
			return False

	def move_up(self, labyrinth_map):
		labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1]] = str(my_labyrinth.solution_number)
		self.player_position[0] -= 1

	def move_down(self, labyrinth_map):
		labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1]] = str(my_labyrinth.solution_number)
		self.player_position[0] += 1

	def move_right(self, labyrinth_map):
		labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1]] = str(my_labyrinth.solution_number)
		self.player_position[1] += 1

	def move_left(self, labyrinth_map):
		labyrinth_map.map_with_player[self.player_position[0]][self.player_position[1]] = str(my_labyrinth.solution_number)
		self.player_position[1] -= 1

	def where_can_move(self, labyrinth_map, solution_list):
		if self.player_position == labyrinth_map.map_end:
			solution_list.append(labyrinth_map.map_with_player)
			solution_list.append("FINISHED")
			return False

		valid_movements = {"up": False, "down": False, "right": False, "left": False}
		movement_names = list(valid_movements.keys())
		choosed_movement = movement_names[randint(0, len(movement_names) - 1)]

		if self.can_move_up(labyrinth_map):
			valid_movements["up"] = True
		
		if self.can_move_down(labyrinth_map):
			valid_movements["down"] = True
		
		if self.can_move_right(labyrinth_map):
			valid_movements["right"] = True
		
		if self.can_move_left(labyrinth_map):
			valid_movements["left"] = True

		if valid_movements["up"] == True or valid_movements["down"] == True or valid_movements["right"] == True or valid_movements["left"] == True:
			while valid_movements[choosed_movement] != True:
				choosed_movement = movement_names[randint(0, len(movement_names) - 1)]
		else:
			solution_list.append(labyrinth_map.map_with_player)
			my_labyrinth.solution_number += 1
			player_position = my_labyrinth.map_start
			return False

		if choosed_movement == "up":
			self.move_up(labyrinth_map)
		elif choosed_movement == "down":
			self.move_down(labyrinth_map)
		elif choosed_movement == "right":
			self.move_right(labyrinth_map)
		elif choosed_movement == "left":
			self.move_left(labyrinth_map)

my_labyrinth = labyrinth()
my_player = player(my_labyrinth)
solutions = []

my_labyrinth.player_in_map(my_player)
my_labyrinth.formated_map_print()

while "FINISHED" not in solutions:
	system("cls")

	my_labyrinth.player_in_map(my_player)
	my_labyrinth.formated_map_print()
	my_player.where_can_move(my_labyrinth, solutions)

input()

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
7:38 PM
Starting new version
8:18 PM
The player goes throught a single-road labyrinth. This is 0.1
Today is Tuesday, the second of November, 2021
6:30 PM
Starting new version
7:40 PM
The player chooses a random way. This is 0.2
Today is Saturday, the sixth of November, 2021
3:25 PM
Starting new version
3:46 PM
The player tries going by different ways. This is 0.3
"""
