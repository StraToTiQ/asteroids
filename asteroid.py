import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            f_vector = self.velocity.rotate(angle)
            s_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            f_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            s_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            f_asteroid.velocity = f_vector * 1.2
            s_asteroid.velocity = s_vector * 1.2
            self.kill()
            return