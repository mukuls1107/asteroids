import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

pygame.init()

ck = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Abe Niche Dekh!")

# Sprite groups

# Associate asteroid containers with groups
def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    astField  =pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    
    # Create player object
    pl = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    updatable.add(pl)
    drawable.add(pl)
    
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw and update all sprites
        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()

        # Update all sprites
        delt = ck.tick(60)
        dt = delt / 1000
        for up in updatable:
            up.update(dt)

if __name__ == "__main__":
    main()
