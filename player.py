import pygame
import utils

class Player():
	x = 0
	y = 0
	moveSpeed = 5

	moveRight = False
	moveLeft = False
	moveUp = False
	moveDown = False

	screen = ""

	def __init__(self, screen):
		# Call pygame sprite init method
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(".\\assets\\player.png", ).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		

	def update(self):
		self.screen.blit(self.image, (self.x, self.y))