"""
16/09/2021 at 1:42 PM

Starting project
This project is meaned to be a copy of Geometry Dash with the intention of making practice of
creating maps with objects and that they can move
"""

import pygame, sys

pygame.init()

class background(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("image/background.png")
		self.image.convert()
		self.rect = self.image.get_rect()

class ground(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("image/ground.png")
		self.image.convert()
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()

class spike(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("image/spike.png")
		self.image.convert()
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()

class player(pygame.sprite.Sprite):
	jumping = False
	falling = False
	x_speed = 0
	y_speed = 0
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("image/player.png")
		self.image.convert()
		self.rect = self.image.get_rect()
	def jump(self):
		self.jumping = True
		self.y_speed = -25
	def fall(self):
		self.falling = True
		self.y_speed = 10
	def stop(self):
		self.y_speed = 0

clock = pygame.time.Clock()

icon = pygame.image.load("image/icon.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("Geometry Dash")
window = pygame.display.set_mode((800, 600))

background_speed = -10
ground_speed = -20

map_backgrounds = pygame.sprite.Group()
map_grounds = pygame.sprite.Group()
objects = pygame.sprite.Group()
players = pygame.sprite.Group()

for i in range(0, 100):
	map_background = background()
	map_backgrounds.add(map_background)
	map_background.rect.x = 0 + (800 * i)
	map_background.rect.y = 0

for i in range(0, 100):
	map_ground = ground()
	map_grounds.add(map_ground)
	map_ground.rect.x = 0 + (800 * i)
	map_ground.rect.y = 0

main_player = player()

players.add(main_player)
main_player.rect.x = 200
main_player.rect.y = 350

for i in range(0, 2):
	new_spike = spike()
	objects.add(new_spike)
	new_spike.rect.x = 1000 + (50 * i)
	new_spike.rect.y = 350

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if (main_player.jumping == False) and (main_player.falling == False):
					main_player.jump()

	lose = pygame.sprite.spritecollide(main_player, objects, False)

	if lose:
		background_speed = 0
		ground_speed = 0

	for current_background in map_backgrounds:
		current_background.rect.x += background_speed

	for current_ground in map_grounds:
		current_ground.rect.x += ground_speed
	
	for current_object in objects:
		current_object.rect.x += ground_speed

	main_player.rect.y += main_player.y_speed

	if (main_player.jumping == True) and (main_player.rect.y) == 250:
		main_player.fall()
		main_player.jumping = False
	elif (main_player.falling == True) and (main_player.rect.y) == 350:
		main_player.stop()
		main_player.falling = False

	map_backgrounds.draw(window)
	map_grounds.draw(window)
	objects.draw(window)
	players.draw(window)

	pygame.display.flip()
	clock.tick(60)

"""
16/09/2021 at 3:57 PM

Finishing Project
But this can be a unoptimized form of making maps (and a hard one)
"""