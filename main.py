import pygame
import Classes.Player as Player
import Classes.Asteroid as Asteroid
import random
pygame.init()

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

def draw(p1, asteroids):
    SCREEN.fill(BLACK)
    p1.draw()
    for asteroid in asteroids:
        asteroid.draw()
    for missle in p1.missles:
        missle.draw()
    pygame.display.update()

def move(p1, asteroids):
    mouse_move = pygame.mouse.get_rel()
    if mouse_move[0] > 0:
        p1.angle += p1.rotation / FPS
    elif mouse_move[0] < 0:
        p1.angle -= p1.rotation / FPS
    button = pygame.mouse.get_pressed()
    if button[0]:
        p1.thrust()
        p1.move()
    else:
        p1.friction()
        p1.move()
    for asteroid in asteroids:
        asteroid.move()
    for missle in p1.missles:
        missle.move()
        if missle.cycle == 0:
            p1.missles.remove(missle)

def collide(p1, asteroids):
    p1.collide(asteroids)
    for asteroid in asteroids:
        for missle in p1.missles:
            if missle.rect.colliderect(asteroid.rect):
                p1.missles.remove(missle)
                if asteroid.scale == 10:
                    for i in range(3):
                        asteroids.append(Asteroid(pygame.Vector2(random.randrange(-100, 100), random.randrange(-100, 100)) + asteroid.center, 5, asteroid.rotation*2))
                if asteroid.scale == 5:
                    for i in range(3):
                        asteroids.append(Asteroid(pygame.Vector2(random.randrange(-100, 100), random.randrange(-100, 100)) + asteroid.center, 1, asteroid.rotation*2))
                asteroids.remove(asteroid)

def main():
    running = True
    clock = pygame.time.Clock()
    p1 = Player()
    asteroids = [] 
    for i in range(6):
        asteroids.append(Asteroid(pygame.Vector2(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT))))
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
                p1.fire()
        move(p1, asteroids)
        collide(p1, asteroids)
        draw(p1, asteroids)

if __name__ == "__main__":
    main()

