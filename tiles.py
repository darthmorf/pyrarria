import pygame
import utils

class Tile():
	x = 0
	y = 250
	enabled = True

	screen = ""

	def __init__(self, screen, sprite):
		# Call pygame sprite init method
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(sprite).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		

	def update(self):
		self.screen.blit(self.image, (self.x, self.y))


class Dirt(Tile):

	def __init__(self, screen):
		super().__init__(screen, ".\\assets\\dirt01.png")
		