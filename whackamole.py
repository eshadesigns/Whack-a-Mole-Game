import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 512))
#grid = [[" " for i in range(20)] for j in range(16)]
def drawGrid():
    for i in range(1,20):
        pygame.draw.line(screen, (0,0,0), (0,i*32), (640, i*32))
    for i in range(1,20):
        pygame.draw.line(screen, (0,0,0), (i*32,0),(i*32,512))
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        #screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        xpos = 0
        ypos = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = event.pos
                    xpos = random.randint(0, 19) * 32
                    ypos = random.randint(0, 15) * 32
                    #screen.blit(mole_image, mole_image.get_rect(topleft=(xpos, ypos)))
            screen.fill("light green")
            drawGrid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(xpos,ypos)))
            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

