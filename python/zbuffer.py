import numpy as np

class ZBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = np.full((width, height), np.inf)

    def clear(self):
        """ Clear the Z-buffer by resetting it to infinity. """
        self.buffer.fill(np.inf)

    def update(self, x, y, z):
        """ Update the Z-buffer if the current point is closer. """
        if z < self.buffer[x, y]:
            self.buffer[x, y] = z
            return True
        return False
