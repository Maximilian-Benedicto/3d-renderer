import pygame
import sys
from camera import Camera
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

camera = Camera(position=(0, 0, 5))  # Start the camera 5 units back on the z-axis

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle camera movement (e.g., arrow keys to move the camera)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera.position[0] -= 0.1  # Move left
    if keys[pygame.K_RIGHT]:
        camera.position[0] += 0.1  # Move right
    if keys[pygame.K_UP]:
        camera.position[2] -= 0.1  # Move forward
    if keys[pygame.K_DOWN]:
        camera.position[2] += 0.1  # Move backward

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the cube relative to the camera
    rasterizer.render_object(cube, camera)

    # Update the display
    pygame.display.update()

pygame.quit()

sys.exit()

