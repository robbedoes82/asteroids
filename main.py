# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # denk dat dit voor de creatie van player moet komen als player in juiste container moet komen
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #hoeft niet in class zelf gedeclareerd te worden
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = ((updatable))
    Shot.containers = (shots, updatable, drawable) #belangrijk om ook tot container "shots" te behoren, anders kan je er niet over itereren
    
    player = Player(x, y)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

         # limit the framerate to 60 FPS (clock.tick(60))
         # dt = aantal seconden dat gepasseerd is sinds laatste tick
        dt = clock.tick(60)/1000
       


if __name__ == "__main__":
    main()
