import pygame
import Missle

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
MAX_SPEED = 8
MISSLE_SPEED = 5
FPS = 60

class Player:
    def __init__(self):
        self.center = SCREEN_CENTER
        self.angle = 0
        self.rotation = 180
        self.thrusting = False
        self.missles = []
        self.points = [
            pygame.Vector2(0, -8).rotate(self.angle) + self.center, 
            pygame.Vector2(-4, 8).rotate(self.angle) + self.center, 
            pygame.Vector2(4, 8).rotate(self.angle) + self.center
            ]
        self.flame_points = [
            pygame.Vector2(-2, 8).rotate(self.angle) + self.center,
            pygame.Vector2(2, 8).rotate(self.angle) + self.center,
            pygame.Vector2(0, 10).rotate(self.angle) + self.center
        ]
        self.velocity = pygame.Vector2(0,0)
        self.dx = 0
        self.dy = 0
        self.rect = pygame.draw.polygon(SCREEN, WHITE, self.points, 1)
    def update(self):
        self.points = [
            pygame.Vector2(0, -8).rotate(self.angle) + self.center, 
            pygame.Vector2(-4, 8).rotate(self.angle) + self.center, 
            pygame.Vector2(4, 8).rotate(self.angle) + self.center 
            ]
        self.flame_points = [
            pygame.Vector2(-2, 8).rotate(self.angle) + self.center,
            pygame.Vector2(2, 8).rotate(self.angle) + self.center,
            pygame.Vector2(0, 12).rotate(self.angle) + self.center
        ]
        self.exploding = False
    def draw(self):
        self.update()
        if self.exploding:
            pygame.draw.circle(SCREEN, WHITE, self.center, self.rect.width)
        else:
            self.rect = pygame.draw.polygon(SCREEN, WHITE, self.points, 1)
            if self.thrusting:
                pygame.draw.polygon(SCREEN, WHITE, self.flame_points, 1)
    def thrust(self):
        self.velocity = pygame.Vector2(0,-1).rotate(self.angle)
        self.dy = self.dy + .1 * self.velocity.y if self.dy <= MAX_SPEED else MAX_SPEED * self.velocity.y
        self.dx = self.dx + .1 * self.velocity.x if self.dx <= MAX_SPEED else MAX_SPEED * self.velocity.x
        self.thrusting = True
    def friction(self):
        self.dy *= 0.99
        self.dx *= 0.99
        self.thrusting = False
    def move(self):
        self.center.x += self.dx
        self.center.y += self.dy
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        if self.center.x < 0:
            self.center.x = SCREEN_WIDTH
    def collide(self, colliders):
        for collider in colliders:
            if self.rect.colliderect(collider.rect):
                self.exploding = True
    def fire(self):
        if len(self.missles) <= 4:
            missle_velocity = pygame.Vector2(0,-1).rotate(self.angle)
            missle = Missle(pygame.Vector2(0, -8).rotate(self.angle) + self.center, missle_velocity)
            self.missles.append(missle)