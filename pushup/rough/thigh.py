import numpy as np

class thighs:

    def update(self, dims=None):
        self.thigh_tail = self.b.get_heads()
        if dims: self.args = [self.thigh_tail, dims]
        else: self.args = [self.thigh_tail, self.args[1]]
        self.tail = np.array(self.args[0])
        self.thigh = np.array(self.args[1])

    def __init__(self, b, thigh_dims,):
        self.b=b
        self.args = [b.get_heads(), thigh_dims]
        self.update()

    def plot(self, ax):
        #print(self.thigh_tail[0][0])
        for i in range(4):
            ax.quiver(self.thigh_tail[i][0], self.thigh_tail[i][1], self.thigh_tail[i][2], self.args[1][i][0], self.args[1][i][1], self.args[1][i][2], arrow_length_ratio=0.1)

    def get_heads(self):
        return self.tail+self.thigh