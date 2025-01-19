import pygame
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
MAX_SPEED = 8
MISSLE_SPEED = 5
FPS = 60

class Missle:
    def __init__(self, spawn, velocity):
        self.center = spawn
        self.velocity = velocity
        self.dx = MISSLE_SPEED * self.velocity.x
        self.dy = MISSLE_SPEED * self.velocity.y
        self.cycle = 120
        self.rect = pygame.Rect(pygame.Vector2(0,0) + self.center, (1, 1))
    def move(self):
        self.center += pygame.Vector2(self.dx, self.dy)
        self.cycle -= 1
    def draw(self):
        self.rect = pygame.Rect(pygame.Vector2(-1,-1) + self.center, (2, 2))
        pygame.draw.rect(SCREEN, WHITE, self.rect)