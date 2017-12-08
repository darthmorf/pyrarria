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
screenSize = (1280, 720)
mainSurface = pygame.display.set_mode(screenSize)
tileSurface = tiles.TileSurface(mainSurface, 0, 0, screenSize[0], screenSize[1])
pygame.display.set_caption("Pyrarria")

#initialize player
player = player.Player(mainSurface, screenSize[0]/2, screenSize[1]/2)

#generate tiles
tileSurface.generateTiles()

running = True
 
# Clock is used to control how fast the surface updates
clock = pygame.time.Clock()

#draw stuff for the first time
mainSurface.fill(BGCOLOUR)
mainSurface.blit(player.image, (player.x, player.y))
tileSurface.drawTiles()
pygame.display.flip()

# -------- Main Program Loop -----------
while running:
    
    # --- Main event loop ---
    for event in pygame.event.get(): 
    
        if event.type == pygame.QUIT: # If user clicked close
              running = False # Flag that we are done so we exit the game loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: player.moveRight = True
            if event.key == pygame.K_a: player.moveLeft = True
            if event.key == pygame.K_SPACE and player.canJump == True: player.jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: player.moveRight = False
            if event.key == pygame.K_a: player.moveLeft = False
            #if event.key == pygame.K_SPACE: player.jumping = False
 
    # --- Game logic ---
    #clear the draw list
    drawList = []

    #draw bg over player position
    drawList.append(mainSurface.fill(BGCOLOUR, player.rect))

    # gravity effects
    if player.jumping == False:
        player.y += player.gravitySpeed       
        player.updatePos()

    #If colliding with tiles, sit on top rather than clip within
    collidingTiles = pygame.sprite.spritecollide(player, tileSurface.tileGroup, False)
    if len(collidingTiles) > 0:
        player.y = collidingTiles[0].y - player.rect.height
        player.updatePos()
        player.canJump = True
    else:
        player.canJump = False
        
    #movement logic
    if player.jumping == True:
        player.y -= player.jumpSpeedTracker
        player.jumpHeightTracker += player.jumpSpeedTracker  
        player.updatePos()
        #slow down towards top of jump
        if player.jumpHeightTracker > player.jumpHeight / 2:
            player.jumpSpeedTracker = player.jumpSpeedTracker * 0.9          
        #stop jumping if at apex
        if player.jumpHeightTracker > player.jumpHeight:
            player.jumping = False
            player.jumpHeightTracker = 0
            player.jumpSpeedTracker = player.jumpSpeed

    #horizontal movement
    if player.moveRight: player.x += player.moveSpeed
    if player.moveLeft: player.x -= player.moveSpeed
    player.updatePos()

    # --- Drawing Logic ---    

    #draw player
    drawList.append(mainSurface.blit(player.image, (640, 360)))

    #update tile surface
    drawList.append(mainSurface.blit(tileSurface.surface.convert(), (player.x + 640, player.y + 360)))

    # Update main surface
    pygame.display.update(drawList)
     
    # Set Framerate to 60fps
    clock.tick(60)


#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
