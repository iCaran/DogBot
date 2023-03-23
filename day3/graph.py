class plotter:

    def __init__(self, ax):
        self.ax = ax
        self.x = [-400, 400]
        self.y = [-200, 200]
        self.z = [800,0]

    def plot(self):
        self.ax.clear()
        self.ax.set_xlim(self.x)
        self.ax.set_ylim(self.y)
        self.ax.set_zlim(self.z)
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
