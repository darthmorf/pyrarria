import pygame
import utils

class Tile():
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

	def update(self):
		self.screen.blit(self.image, (self.x, self.y))


class Dirt(Tile):

	def __init__(self, screen, x, y):
		super().__init__(screen, ".\\assets\\dirt01.png", x, y)
		



def GenerateTiles(screen):
	tiles = []
	x = 0
	y = 256

	for i in range(0, 50):
		row = []
		for j in range(0, 50):
			newTile = Dirt(screen, x, y)
			row.append(newTile)
			x += 16
		x = 0
		y += 16
		tiles.append(row)

	return tiles

def DrawTiles(tileArray):
	for i in range(0, len(tileArray)):
		for j in range(0, len(tileArray[i])):
			tileArray[i][j].update()