import numpy as np

class body:

    def __init__(self):
        self.body_tails=[[-249.75, -126.25, 44],[249.75, -126.25, 44],[249.75, 126.25, 44],[-249.75, 126.25, 44]]
        self.shoulder_tails1=[[-249.75, -126.25, 44],[249.75, -126.25, 44],[-249.75, 126.25, 44],[249.75, 126.25, 44]]
        self.shoulder_tails2=[[-300.75, -126.25, 44],[300.75, -126.25, 44],[-300.75, 126.25, 44],[300.75, 126.25, 44]]

        self.body_dims=[[499.5, 0, 0],[0, 252.5, 0],[-499.5, 0, 0],[0, -252.5, 0]]
        self.shoulder_dims1=[[-51, 0, 0],[51, 0, 0],[-51, 0, 0],[51, 0, 0]]
        self.shoulder_dims2=[[0, -34.5, 0],[0, -34.5, 0],[0, 34.5, 0],[0, 34.5, 0]]

    def plot(self,ax):
        for i in range(len(self.body_tails)):
            ax.quiver(self.body_tails[i][0],self.body_tails[i][1],self.body_tails[i][2],self.body_dims[i][0],self.body_dims[i][1],self.body_dims[i][2], arrow_length_ratio=0)
            ax.quiver(self.shoulder_tails1[i][0],self.shoulder_tails1[i][1],self.shoulder_tails1[i][2],self.shoulder_dims1[i][0],self.shoulder_dims1[i][1],self.shoulder_dims1[i][2], arrow_length_ratio=0)
            ax.quiver(self.shoulder_tails2[i][0],self.shoulder_tails2[i][1],self.shoulder_tails2[i][2],self.shoulder_dims2[i][0],self.shoulder_dims2[i][1],self.shoulder_dims2[i][2], arrow_length_ratio=0)

    def get_heads(self):
        self.heads = np.array(self.shoulder_tails2)+np.array(self.shoulder_dims2)
        return self.heads