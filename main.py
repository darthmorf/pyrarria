import pygame
import utils
import player
import tiles

pygame.init()

# -------- Global Variables -----------

# --- Colours ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BGCOLOUR = (153, 255, 255)

# -------- Initialize Game -----------

# Open main game window
size = (1280, 720)
mainScreen = pygame.display.set_mode(size)
pygame.display.set_caption("Pyrarria")

#initialize player
player = player.Player(mainScreen)

#generate tiles
tileGrid = tiles.GenerateTiles(mainScreen)

running = True
 
# Clock is used to control how fast the screen updates
clock = pygame.time.Clock()

#draw stuff for the first tim
mainScreen.fill(BGCOLOUR)
player.update()
tiles.DrawTiles(tileGrid)
pygame.display.flip()

# -------- Main Program Loop -----------
while running:
    
    # --- Main event loop ---
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              running = False # Flag that we are done so we exit the game loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: player.moveRight = True
            if event.key == pygame.K_a: player.moveLeft = True
            if event.key == pygame.K_w: player.moveUp = True
            if event.key == pygame.K_s: player.moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: player.moveRight = False
            if event.key == pygame.K_a: player.moveLeft = False
            if event.key == pygame.K_w: player.moveUp = False
            if event.key == pygame.K_s: player.moveDown = False
 
    # --- Game logic ---
    drawList = []
    drawList.append(player.update())
    mainScreen.fill(BGCOLOUR)
    
    if player.moveRight: player.x += player.moveSpeed
    if player.moveLeft:  player.x -= player.moveSpeed
    if player.moveUp:    player.y -= player.moveSpeed
    if player.moveDown:  player.y += player.moveSpeed

    drawList.append(player.update())
    

    # --- Drawing Logic ---    

    # Update screen
    pygame.display.update(drawList)
     
    # Set Framerate to 60fps
    clock.tick(60)


#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
