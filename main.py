import pygame
pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

class Player:
    def __init__(self):
        self.center = SCREEN_CENTER
        self.angle = 0
        self.rotation = 0.1
        self.points = [
            pygame.Vector2(self.center.x, self.center.y - 8), 
            pygame.Vector2(self.center.x - 4, self.center.y + 8), 
            pygame.Vector2(self.center.x + 4, self.center.y + 8)
            ]
        self.dx = 0.01
        self.dy = 0.01
    def update(self):
        self.points = [
            pygame.Vector2(0, -8).rotate(self.angle) + self.center, 
            pygame.Vector2(-4, 8).rotate(self.angle) + self.center, 
            pygame.Vector2(4, 8).rotate(self.angle) + self.center
            ]
    def draw(self):
        self.update()
        pygame.draw.polygon(SCREEN, WHITE, self.points, 1)

def draw(p1):
    SCREEN.fill(BLACK)
    p1.draw()
    pygame.display.update()

def move(p1):
    p1.center.y -= p1.dy
    p1.angle += p1.rotation

def collide():
    pass

def main():
    running = True
    p1 = Player()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        collide()
        move(p1)
        draw(p1)

if __name__ == "__main__":
    main()

