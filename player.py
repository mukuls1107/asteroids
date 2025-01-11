import circleshape, pygame
import constants
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.x = x
        self.y= y
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,color=(255,255,255), points=self.triangle(), width=2)
        
    def rotate(self,dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # ? 
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
        
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet_velocity = forward * constants.PLAYER_SHOOT_SPEED
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = bullet_velocity