import numpy as np
from graph import plotter

class thighs:

    MAG = 210.66798510366596

    def update(self, dims=None):
        self.thigh_tail = self.b.get_heads()
        if dims: self.args = [self.thigh_tail, dims]
        else: self.args = [self.thigh_tail, self.args[1]]
        self.tail = np.array(self.args[0])
        # self.thigh = np.array(self.args[1])

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

    def set_args(self):
        self.args[1]=[[], [], [], []]

    def pass_to_l(self, x, y, z):
        self.xyz= [x,y,z]

    def t3_a(self, frame, t, ax, fig, l):
        # print(frame)
        x = thighs.MAG * np.cos(np.radians(t[frame]))
        y = 0
        z = thighs.MAG * np.sin(np.radians(t[frame]))
        plotter(ax).plot()
        self.b.plot(ax)
        ax.quiver(self.args[0][3][0], self.args[0][3][1], self.args[0][3][2], x, y, z, arrow_length_ratio=0.1)
        # print(self.args[1])
        # self.args[1][3]=[x,y,z]
        self.pass_to_l(x,y,z)
        l.l3_ang(frame, ax, fig, self)
        # fig.canvas.draw_idle()