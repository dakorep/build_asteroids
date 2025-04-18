from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = v1 * 1.2
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2.velocity = v2 * 1.2