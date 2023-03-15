import numpy as np


class leg:
    def __init__(self, knee=[], foot=[], knee_tail=[]):
        self.args = [knee, foot, knee_tail]
        self.knee_tail = np.array(knee_tail)
        self.knee = np.array(knee)
        self.foot = np.array(foot)
        self.knee_head = self.knee_tail + self.knee
        self.foot_tail = self.knee_head
        self.foot_head = self.foot_tail + self.foot

    def plot(self, ax):
        ax.quiver(self.knee_tail[0], self.knee_tail[1], self.knee_tail[2], [self.knee[0]], [self.knee[1]],
                  [self.knee[2]], arrow_length_ratio=0.1)
        ax.quiver(self.foot_tail[0], self.foot_tail[1], self.foot_tail[2], [self.foot[0]], [self.foot[1]],
                  [self.foot[2]], arrow_length_ratio=0.1)

    def plot_legs(self, legs, ax):
        l = []
        for i in range(len(legs)):
            l.append(leg(legs[i].args[0], legs[i].args[1], legs[i].args[2]))
            l[i].plot(ax)
