from geometry import project_vertex, draw_triangle
from zbuffer import ZBuffer

class Rasterizer:
    def __init__(self, screen, fov, near, far):
        self.screen = screen
        self.fov = fov
        self.near = near
        self.far = far
        self.zbuffer = ZBuffer(screen.get_width(), screen.get_height())

    def render_object(self, object3d):
        # Clear the Z-buffer before rendering
        self.zbuffer.clear()

        for face in object3d.faces:
            # Project vertices
            v1 = project_vertex(object3d.vertices[face[0]], self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)
            v2 = project_vertex(object3d.vertices[face[1]], self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)
            v3 = project_vertex(object3d.vertices[face[2]], self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)

            # Rasterize the triangle
            draw_triangle(self.screen, v1, v2, v3, (255, 0, 0), self.zbuffer)
