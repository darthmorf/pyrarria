import pygame
import utils
from random import randint

tiles = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
	x = 0
	y = 0
	enabled = True

	def __init__(self, sprite, x, y, surface):
		# Call pygame sprite init method
		super().__init__()
		self.image = pygame.image.load(sprite).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		
		self.x = x
		self.y = y
		self.surface = surface

		tiles.add(self)

	def updatePos(self, x = self.x, y = self.y):
		self.rect.x = x
		self.rect.y = y


class Dirt(Tile):
	def __init__(self, x, y, surface):
		spriteVariant = randint(1, 3)
		super().__init__(".\\assets\\dirt0" + str(spriteVariant) + ".png", x, y, surface)

class Air(Tile):
	def __init__(self, x, y, surface):
		super().__init__(".\\assets\\air.png", x, y, surface)
	

def generateTiles(surface):
	tiles = []
	x = 0
	y = 368

	for i in range(0, 99):
		row = []
		for j in range(0, 99):
			newTile = Dirt(x, y, surface)
			newTile.rect.x = x
			newTile.rect.y = y
			row.append(newTile)
			x += 16
		x = 0
		y += 16
		tiles.append(row)

	return tiles


def drawTiles(tileArray):
	for i in range(0, len(tileArray)):
		for j in range(0, len(tileArray[i])):
			tileArray[i][j].update()