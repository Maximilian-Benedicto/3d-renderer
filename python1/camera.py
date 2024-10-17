import numpy as np

class Camera:
    def __init__(self, position=(0, 0, 0), look_at=(0, 0, -1), up=(0, 1, 0)):
        self.position = np.array(position)
        self.look_at = np.array(look_at)
        self.up = np.array(up)
    
    def get_view_matrix(self):
        """ 
        Get the view matrix that transforms world coordinates to camera space. 
        We'll use a simple translation for now (no rotation).
        """
        # Negative translation to simulate camera movement
        translate = np.eye(4)
        translate[0:3, 3] = -self.position
        return translate
