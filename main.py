import pygame, player
from constants import *
 
pygame.init()

ck = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pl = player.Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pl.draw(screen)
        pygame.display.flip()
        delt = ck.tick(60)
        dt = delt / 1000
        pl.update(dt)
        
if __name__ == "__main__":
    main()
