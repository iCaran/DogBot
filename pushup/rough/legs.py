class legs:
    def __init__(self, ax, t_o, dims):
        self.ax = ax
        self.t_o = t_o
        self.tails = t_o.get_heads()
        self.args = [self.tails, dims]

    def plot(self):
        for i in range(4):
            self.ax.quiver(self.tails[i][0], self.tails[i][1], self.tails[i][2], self.args[1][i][0], self.args[1][i][1],
                           self.args[1][i][2], arrow_length_ratio=0.1)

    def update(self, dims=None):
        self.tails = self.t_o.get_heads()
        if dims:
            self.args = [self.tails, dims]
        else:
            self.args = [self.tails, self.args[1]]

    def get_heads(self):
        return self.tails+self.args[1]