import pygame
from geometry import Vector2, Vector3, Edge

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Light Toggle")

# Create a 2D array to keep track of the pixel states
pixels = [[0 for _ in range(WINDOW_WIDTH)] for _ in range(WINDOW_HEIGHT)]

def draw_pixels():
    """Draws the pixels on the screen based on their state."""
    for y in range(WINDOW_HEIGHT):
        for x in range(WINDOW_WIDTH):
            if pixels[y][x] == 1:  # If the pixel is lit
                screen.set_at((x, y), WHITE)  # Set pixel to white
            else:
                screen.set_at((x, y), BLACK)  # Set pixel to black

def main():
    running = True
    while running:

        # Draw the pixels
        draw_pixels()
        
        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

def draw_edge(edge):
    pygame.draw.line()
