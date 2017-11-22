import pygame
import utils

class Player():
	x = 0
	y = 0
	moveSpeed = 5
	gravitySpeed = 5

	jumpSpeed = 5
	jumpSpeedTracker = jumpSpeed
	jumpHeight = 70
	jumpHeightTracker = 0


	moveRight = False
	moveLeft = False
	jumping = False
	canJump = False

	screen = ""

	def __init__(self, screen):
		# Call pygame sprite init method
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(".\\assets\\player.png", ).convert_alpha() #load a sprite image
		self.rect = self.image.get_rect() # set collision rectangle		

	def updatePos(self):
		self.rect.x = self.x
		self.rect.y = self.y