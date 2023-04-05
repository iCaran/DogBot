import numpy as np

class thighs:

    MAG = 210.66798510366596

    def update(self, dims=None):
        self.thigh_tail = self.b.get_heads()
        if dims: self.args = [self.thigh_tail, dims]
        else: self.args = [self.thigh_tail, self.args[1]]
        self.tail = np.array(self.args[0])
        self.thigh = np.array(self.args[1])

    def __init__(self, b, thigh_dims=None):
        self.b=b
        self.args = [b.get_heads(), thigh_dims]
        self.update()
        if thigh_dims is not None: self.thigh_dims=thigh_dims

    def plot(self, ax):
        #print(self.thigh_tail[0][0])
        for i in range(len(self.args[0])):
            ax.quiver(self.args[0][i][0], self.args[0][i][1], self.args[0][i][2], self.args[1][i][0], self.args[1][i][1], self.args[1][i][2], arrow_length_ratio=0.1)

    def get_heads(self):
        return self.args[0]+self.args[1]

    def angle_plot(self, angles, ax):
        v=[]
        for i in range(len(angles)):
            theta=angles[i]
            x = thighs.MAG * np.cos(np.radians(theta))
            y = 0
            z = thighs.MAG * np.sin(np.radians(theta))
            v.append([x,y,z])
        v=np.array(v)
        self.args=[self.b.get_heads(), v]
        self.plot(ax)