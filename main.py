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

