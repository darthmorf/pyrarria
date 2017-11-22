import pygame
import utils
from random import randint

tiles = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
	x = 0
	y = 0
	enabled = True

	screen = ""

	def __init__(self, screen, sprite, x, y):
		# Call pygame sprite init method
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(sprite).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		
		self.x = x
		self.y = y

		tiles.add(self)


	def update(self):
		self.screen.blit(self.image, (self.x, self.y))


class Dirt(Tile):
	def __init__(self, screen, x, y):
		spriteVariant = randint(1, 3)
		super().__init__(screen, ".\\assets\\dirt0" + str(spriteVariant) + ".png", x, y)

class Air(Tile):
	def __init__(self, screen, x, y):
		super().__init__(screen, ".\\assets\\air.png", x, y)
	

def generateTiles(screen):
	tiles = []
	x = 0
	y = 256

	for i in range(0, 99):
		row = []
		for j in range(0, 99):
			newTile = Dirt(screen, x, y)
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