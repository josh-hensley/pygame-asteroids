import pygame
pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
MAX_SPEED = .1

class Player:
    def __init__(self):
        self.center = SCREEN_CENTER
        self.angle = 0
        self.rotation = 1
        self.points = [
            pygame.Vector2(0, -8).rotate(self.angle) + self.center, 
            pygame.Vector2(-4, 8).rotate(self.angle) + self.center, 
            pygame.Vector2(4, 8).rotate(self.angle) + self.center
            ]
        self.velocity = pygame.Vector2(0,0)
        self.dx = 0
        self.dy = 0
    def update(self):
        self.points = [
            pygame.Vector2(0, -8).rotate(self.angle) + self.center, 
            pygame.Vector2(-4, 8).rotate(self.angle) + self.center, 
            pygame.Vector2(4, 8).rotate(self.angle) + self.center 
            ]
    def draw(self):
        self.update()
        pygame.draw.polygon(SCREEN, WHITE, self.points, 1)
    def thrust(self):
        self.velocity = pygame.Vector2(0,-1).rotate(self.angle)
        self.dy = self.dy + 0.00001 * self.velocity.y if self.dy <= MAX_SPEED else MAX_SPEED * self.velocity.y
        self.dx = self.dx + 0.00001 * self.velocity.x if self.dx <= MAX_SPEED else MAX_SPEED * self.velocity.x
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

def draw(p1):
    SCREEN.fill(BLACK)
    p1.draw()
    pygame.display.update()

def move(p1):
    mouse_move = pygame.mouse.get_rel()
    if mouse_move[0] > 0:
        p1.angle += p1.rotation
    elif mouse_move[0] < 0:
        p1.angle -= p1.rotation
    button = pygame.mouse.get_pressed()
    if button[0] == True:
        p1.thrust()
    p1.move()

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

