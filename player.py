import pygame

class Player():
	x = 0
	y = 0

	oldX = 0
	oldY = 0
	
	moveSpeed = 5
	gravitySpeed = 5

	jumpSpeed = 5
	jumpSpeedTracker = jumpSpeed
	jumpHeight = 70
	jumpHeightTracker = 0

	height = 0

	moveRight = False
	moveLeft = False
	jumping = False
	canJump = False

	def __init__(self, surface, x, y):
		# Call pygame sprite init method
		super().__init__()
		self.surface = surface
		self.image = pygame.image.load("./assets/player.png", ).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		
		self.x = x
		self.y = y
		self.height = self.rect.height

	def updatePos(self):
		self.rect.x = self.x
		self.rect.y = self.y