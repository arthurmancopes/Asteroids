from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt  # Move in a straight line

    def split(self):
        self.kill()  # Remove this asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Don't split if too small

        angle = random.uniform(20, 50)  # Generate a random angle between 20 and 50 degrees
        velocity_1 = self.velocity.rotate(angle) * 1.2
        velocity_2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS  # Compute new radius

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity_1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity_2

        # Add new asteroids to all relevant groups
        if hasattr(self, "containers"):
            for group in self.containers:
                group.add(asteroid1)
                group.add(asteroid2)
