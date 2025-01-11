import circleshape
import pygame
from constants import SHOT_RADIUS
import random
from asteroid import Asteroid
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.math.Vector2(0,1)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position = self.position + self.velocity * dt