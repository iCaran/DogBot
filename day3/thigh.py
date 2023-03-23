import numpy as np

class thighs:
    def __init__(self, thigh_tail, thigh_dim,):
        self.args=[thigh_tail, thigh_dim]
        self.tail = np.array(thigh_tail)
        self.thigh = np.array(thigh_dim)

    def plot(self, ax):
        ax.quiver(self.tail[0], self.tail[1], self.tail[2], self.thigh[0], self.thigh[1], self.thigh[2], arrow_length_ratio=0.05)