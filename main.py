import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # Add Player to both groups

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Instantiate Player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill screen with black
        dt = clock.tick(60)/1000 # Pause until 1/60th of a second has passed

        updatable.update(dt)     # Update all updatable objects
        for obj in drawable:
            obj.draw(screen)     # Draw all drawable objects

        pygame.display.flip()    # Refresh the screen

if __name__ == "__main__":
    main()