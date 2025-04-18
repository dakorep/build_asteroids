# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Groups Initializations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #adding every instance of Player to updatable & drawable group
    Asteroid.containers = (asteroids, updatable, drawable) #adding every instance of Player to asteroids, updatable & drawable group
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    aster_field = AsteroidField()
    #print(Player.containers)
    print(updatable)
    print(drawable)
    print(asteroids)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for obj in asteroids:
            if obj.check_collision(player1):
                print("Game Over")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        #print(dt)

if __name__ == "__main__":
    main()              