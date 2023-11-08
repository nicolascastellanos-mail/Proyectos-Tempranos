"""
16/09/2021.11:52AM
"""

import pygame, sys

pygame.init()

class map(pygame.sprite.Sprite):
	speed_x = 0
	speed_y = 0
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("map.png")
		self.image.convert()
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()

class player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png")
		self.image.convert()
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()

pygame.display.set_caption("Intento de Mapa")
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
window.fill((255, 255, 255))

sprites = pygame.sprite.Group()

mainmap = map()
mainplayer = player()

sprites.add(mainmap)
sprites.add(mainplayer)

mainplayer.rect.x = 350
mainplayer.rect.y = 250

sprites.draw(window)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				mainmap.speed_y = 10
			if event.key == pygame.K_DOWN:
				mainmap.speed_y = -10
			if event.key == pygame.K_RIGHT:
				mainmap.speed_x = -10
			if event.key == pygame.K_LEFT:
				mainmap.speed_x = 10
			if event.key == pygame.K_w:
				mainmap.speed_y = -10
			if event.key == pygame.K_s:
				mainmap.speed_y = 10
			if event.key == pygame.K_d:
				mainmap.speed_x = 10
			if event.key == pygame.K_a:
				mainmap.speed_x = -10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				mainmap.speed_y = 0
			if event.key == pygame.K_DOWN:
				mainmap.speed_y = 0
			if event.key == pygame.K_RIGHT:
				mainmap.speed_x = 0
			if event.key == pygame.K_LEFT:
				mainmap.speed_x = 0
			if event.key == pygame.K_w:
				mainplayer.speed_y = 0
			if event.key == pygame.K_s:
				mainplayer.speed_y = 0
			if event.key == pygame.K_d:
				mainplayer.speed_x = 0
			if event.key == pygame.K_a:
				mainplayer.speed_x = 0

	mainmap.rect.x += mainmap.speed_x
	mainmap.rect.y += mainmap.speed_y

	window.fill((255, 255, 255))

	sprites.draw(window)

	pygame.display.flip()
	clock.tick(30)

"""
16/09/2021.12:39PM (pausa para almorzar, ya puedo mover el mapa o la cámara con las flechas y el jugador con wasd)
16/09/2021.12:39PM (continuando. Voy a implementar que la cámara siga al jugador y cierro el proyecto)
					para eso tendré que hacer que el jugador se quede estatico en el centro de la pantalla y el mapa sea el que se mueva
16/09/2021.01:39PM (objetivo alcanzado, cerrando proyecto)
"""