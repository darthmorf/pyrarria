import pygame
import utils
from random import randint

class TileSurface():

	tileGroup = pygame.sprite.Group()

	tileGrid = []

	def __init__(self, mainSurface, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.surface = mainSurface.subsurface((x, y, width, height))

	def updatePos(self, x, y):
		self.x = self.x
		self.y = self.y

	def generateTiles(self):
		tiles = []
		x = 0
		y = 368

		for i in range(0, 99):
			row = []
			for j in range(0, 99):
				newTile = Dirt(x, y, self)
				newTile.rect.x = x
				newTile.rect.y = y
				row.append(newTile)
				x += 16
			x = 0
			y += 16
			tiles.append(row)

		self.tileGrid = tiles

	def drawTiles(self):
		for i in range(0, len(self.tileGrid)):
			for j in range(0, len(self.tileGrid[i])):
				self.tileGrid[i][j].update()




class Tile(pygame.sprite.Sprite):
	x = 0
	y = 0

	def __init__(self, sprite, x, y, surface):
		# Call pygame sprite init method
		super().__init__()
		self.image = pygame.image.load(sprite).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		
		self.x = x
		self.y = y
		self.parentSurface = surface

		self.parentSurface.tileGroup.add(self)

	def update(self):
		self.parentSurface.surface.blit(self.image, (self.x, self.y))			



class Dirt(Tile):
	def __init__(self, x, y, surface):
		spriteVariant = randint(1, 3)
		super().__init__(".\\assets\\dirt0" + str(spriteVariant) + ".png", x, y, surface)

class Air(Tile):
	def __init__(self, x, y, surface):
		super().__init__(".\\assets\\air.png", x, y, surface)