import pygame
import random

class Asteroid:
    def __init__(self, center, scale=10, rotation=random.randrange(-10, 10)):
        self.center = center
        self.scale = scale
        self.angle = 0
        self.rotation = rotation
        self.dx = random.randrange(-10,10)
        self.dy = random.randrange(-10,10)
        self.points = [
            pygame.Vector2(0,-8).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,-7).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(4,-4).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,-2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,0).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(5,2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,5).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(1,5).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(0,3).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-2,3).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-4,1).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-4,-2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-1,-4).rotate(self.angle) * self.scale + self.center,
        ]
        self.rect = pygame.draw.polygon(SCREEN, WHITE, self.points, 1)
        
    def update(self):
        self.points = [
            pygame.Vector2(0,-8).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,-7).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(6,-4).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(5,-2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(6,0).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(5,2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(3,5).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(1,5).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(0,3).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-2,3).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-4,1).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-4,-2).rotate(self.angle) * self.scale + self.center,
            pygame.Vector2(-3,-6).rotate(self.angle) * self.scale + self.center,
        ]
    def draw(self):
        self.update()
        self.rect = pygame.draw.polygon(SCREEN, WHITE, self.points, 1)
    def move(self):
        self.angle += self.rotation / FPS
        self.center += pygame.Vector2(self.dx, self.dy) / FPS
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        if self.center.x < 0:
            self.center.x = SCREEN_WIDTH