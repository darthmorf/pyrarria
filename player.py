import pygame

class Sprite(pygame.sprite.Sprite):
	def __init__(self, bgColor, width, height, asset):
		# Call pygame sprite init method
		super().__init__()

		# Pass in the color of the sprite, and its x and y position, width and height.
        # Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(bgColor)
		self.image.set_colorkey(bgColor)
        
		#self.image = pygame.image.load(asset).convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()