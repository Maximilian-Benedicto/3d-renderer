class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
    
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


    def __repr__(self):
        return f"Edge({self.v1}, {self.v2})"
    
