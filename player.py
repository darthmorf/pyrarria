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
        
		# Fetch the rectangle object that has the dimensions of the image.
		#self.rect = self.image.get_rect()

	def update(self):
		self.screen.blit(utils.get_image('.\\assets\\player.png'), (self.x, self.y))