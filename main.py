import pygame, player
from constants import *
 
pygame.init()


ck = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Abe Niche Dekh!")
    

updatable = pygame.sprite.Group()
drawable  = pygame.sprite.Group()


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pl = player.Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        drawable.add(pl)
        updatable.add(pl)
        screen.fill((0,0,0))
        # pl.draw(screen)
        for dr in drawable:
            dr.draw(screen)
        
        pygame.display.flip()
        delt = ck.tick(60)
        dt = delt / 1000
        # pl.update(dt)
        for up in updatable:
            up.update(dt)
        
if __name__ == "__main__":
    main()
