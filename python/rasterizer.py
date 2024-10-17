from geometry import project_vertex, draw_triangle, apply_view_transform
from zbuffer import ZBuffer

class Rasterizer:
    def __init__(self, screen, fov, near, far):
        self.screen = screen
        self.fov = fov
        self.near = near
        self.far = far
        self.zbuffer = ZBuffer(screen.get_width(), screen.get_height())

    def render_object(self, object3d, camera):
        # Clear the Z-buffer before rendering
        self.zbuffer.clear()

        # Get the camera's view matrix
        view_matrix = camera.get_view_matrix()

        for face in object3d.faces:
            # Transform the 3D vertices relative to the camera
            v1 = apply_view_transform(object3d.vertices[face[0]], view_matrix)
            v2 = apply_view_transform(object3d.vertices[face[1]], view_matrix)
            v3 = apply_view_transform(object3d.vertices[face[2]], view_matrix)

            # Project the transformed vertices onto the screen
            v1_2d = project_vertex(v1, self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)
            v2_2d = project_vertex(v2, self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)
            v3_2d = project_vertex(v3, self.screen.get_width(), self.screen.get_height(), self.fov, self.near, self.far)

            # Draw the triangle
            draw_triangle(self.screen, v1_2d, v2_2d, v3_2d, (255, 0, 0), self.zbuffer)
