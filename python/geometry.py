import pygame
import numpy as np

class Cube:
    def __init__(self):
        self.vertices = [
            [-1, -1, -1], [-1, -1,  1], [-1,  1, -1], [-1,  1,  1],
            [1, -1, -1], [1, -1,  1], [1,  1, -1], [1,  1,  1]
        ]
        self.faces = [
            (0, 1, 2), (1, 3, 2), (4, 5, 6), (5, 7, 6),  # Front and back
            (0, 1, 4), (1, 5, 4), (2, 3, 6), (3, 7, 6),  # Sides
            (0, 2, 4), (2, 6, 4), (1, 3, 5), (3, 7, 5)   # Top and bottom
        ]

def project_vertex(vertex, screen_width, screen_height, fov, near, far):
    """ Project a 3D vertex to 2D screen space using perspective projection. """
    x, y, z = vertex
    f = 1 / np.tan(np.radians(fov) / 2)
    projected_x = x * f / z
    projected_y = y * f / z
    screen_x = int((projected_x + 1) * screen_width / 2)
    screen_y = int((1 - projected_y) * screen_height / 2)
    return screen_x, screen_y

def draw_triangle(screen, v1, v2, v3, color, zbuffer):
    """ Draw a triangle on the screen. Update the Z-buffer. """
    pygame.draw.polygon(screen, color, [v1, v2, v3])
