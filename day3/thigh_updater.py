import numpy as np
from graph import plotter
from base import body
from thigh import thighs
from leg import leg


class tu:

    def __init__(self, fig, slider, thighs, legs):
        self.slider = slider
        self.fig = fig
        self.thighs = thighs
        self.legs=legs

    def update(self, slider, ax, u, val=None):

        legs=u.legs

        angle_y = slider.val
        rad_y = np.radians(angle_y)
        R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

        angle_y2 = -val
        rad_y2 = np.radians(angle_y2)
        R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

        plotter(ax).plot()
        body.plot(ax)

        l=[]
        v = []
        t = []
        for i in range(len(self.thighs)):
            if i % 2 == 0:
                v.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(self.thighs[i].args[1]))))
            else:
                v.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.thighs[i].args[1]))))
            t.append(thighs(self.thighs[i].args[0], v[i]))
            t[i].plot(ax)
            l.append(leg(v[i],legs[i].args[1],t[i].args[0]))
            l[i].plot(ax)

        #self.thighs=t
        self.legs=l

        self.fig.canvas.draw_idle()
