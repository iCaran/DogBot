import numpy as np
from leg import leg
from graph import plotter
from base import body


class updater:

    def __init__(self, angle_y_slider, ax, fig, legs):
        self.angle_y_slider = angle_y_slider
        self.ax = ax
        self.fig = fig
        #self.legs = t.legs
        self.legs=legs
        self.prev=0

    def update(self, t, var, val=None, event=None):

        legs=t.legs

        #angle_y = self.angle_y_slider.val
        angle_y = val-var
        rad_y = np.radians(angle_y)
        R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

        #angle_y2 = -self.angle_y_slider.val
        angle_y2=-(val-var)
        rad_y2 = np.radians(angle_y2)
        R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

        feet = []

        for l in range(len(legs)):
            if l % 2 == 0:
                feet.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(legs[l].args[1]))))
            else:
                feet.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(legs[l].args[1]))))

        plotter(self.ax).plot()
        body.plot(self.ax)

        new=[]

        for foot in range(len(feet)):
            new.append(leg(legs[foot].args[0], feet[foot], legs[foot].args[2]))
            new[foot].plot(self.ax)

        #t.legs=new
        self.legs=new
        #self.prev=angle_y

        self.fig.canvas.draw_idle()

    def get_var(self):
        return self.prev

