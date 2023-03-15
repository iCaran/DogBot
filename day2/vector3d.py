import numpy as np


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def vec(self):
        return np.array([self.x, self.y, self.z])

    def magnitude(self):
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        self.z /= mag

    def plot(self, ax, color='b', start=(0, 0, 0)):
        ax.quiver(start[0], start[1], start[2], self.x, self.y, self.z, color=color)
