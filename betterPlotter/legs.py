import numpy as np

class legs:
    MAG = 200.0

    def __init__(self, ax, t_o, dims=None):
        self.ax = ax
        self.t_o = t_o
        self.tails = t_o.get_heads()
        self.args = [self.tails, dims]

    def plot(self):
        for i in range(len(self.args[1])):
            self.ax.quiver(self.args[0][i][0], self.args[0][i][1], self.args[0][i][2], self.args[1][i][0], self.args[1][i][1],
                           self.args[1][i][2], arrow_length_ratio=0.1)

    def update(self, dims=None):
        self.tails = self.t_o.get_heads()
        if dims:
            self.args = [self.tails, dims]
        else:
            self.args = [self.tails, self.args[1]]

    def get_heads(self):
        return self.tails+self.args[1]

    def angle_plot(self, angles):
        v=[]
        for i in range(len(angles)):
            theta=angles[i]
            x = legs.MAG * np.cos(np.radians(theta))
            y = 0
            z = legs.MAG * np.sin(np.radians(theta))
            v.append([x,y,z])
        v=np.array(v)
        self.args=[self.t_o.get_heads(), v]
        self.plot()