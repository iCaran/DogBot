import numpy as np
from leg import leg
from plotter import plotter


class updater:

    def __init__(self, angle_y_slider, ax, fig, legs):
        self.angle_y_slider = angle_y_slider
        self.ax = ax
        self.fig = fig
        self.legs = legs

    def update(self, val=None, event=None):
        print(val)
        print(event)

        angle_y = self.angle_y_slider.val
        # angle_y = val
        rad_y = np.radians(angle_y)
        R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

        angle_y2 = -self.angle_y_slider.val
        rad_y2 = np.radians(angle_y2)
        R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

        feet = []

        for l in range(len(self.legs)):
            if l % 2 == 0:
                feet.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(self.legs[l].args[1]))))
            else:
                feet.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.legs[l].args[1]))))

        plotter(self.ax).plot()

        for foot in range(len(feet)):
            new = leg(self.legs[foot].args[0], feet[foot], self.legs[foot].args[2])
            new.plot(self.ax)

        self.fig.canvas.draw_idle()
