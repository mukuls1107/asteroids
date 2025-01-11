import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot
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
    shotGroup = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shotGroup,drawable,updatable)
    
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
            
        for ast in asteroids:
            for bullet in shotGroup:
                if pygame.math.Vector2.distance_to(ast.position, bullet.position) < ast.radius or pygame.math.Vector2.distance_to(ast.position, bullet.position) < bullet.radius:
                    ast.split()
        
        for ast in asteroids:
            if ast.collision(pl):
                print("Collision Detected\nGame Over!")
                
                pause_game(screen)

def pause_game(screen):
    """
    Pauses the game, displays a blinking "Game Over" message, and waits for user action.
    """
    font = pygame.font.Font(None, 74)  # Font for the "Game Over" text
    text = font.render("Game Over!", True, (255, 0, 0))  # Red text
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    blink = True
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Add a keypress to reset or exit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'R' to restart
                    main()  # Restart the game
                elif event.key == pygame.K_q:  # Press 'Q' to quit
                    pygame.quit()
                    exit()

        # Clear the screen

        if blink:
            screen.blit(text, text_rect)
        else:
            # Draw a rectangle over the text to "erase" it
            pygame.draw.rect(screen, (0, 0, 0), text_rect)

        # Alternate the blinking effect
        blink = not blink
        pygame.display.flip()

        # Control the blinking speed
        clock.tick(2) 
if __name__ == "__main__":
    main()
