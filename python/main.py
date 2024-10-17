import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FOV, NEAR, FAR
from geometry import Cube
from rasterizer import Rasterizer

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Rasterizer")

# Create a rasterizer instance and a 3D object (cube)
rasterizer = Rasterizer(screen, FOV, NEAR, FAR)
cube = Cube()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the cube
    rasterizer.render_object(cube)

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()

