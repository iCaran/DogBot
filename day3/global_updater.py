import numpy as np
from leg import leg
from graph import plotter
from base import body
from thigh import thighs
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class slider_all:

    def update_legs(self):

        #angle_y = self.angle_y_slider.val
        angle_y = self.feet_slider.val-self.prev
        rad_y = np.radians(angle_y)
        R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

        #angle_y2 = -self.angle_y_slider.val
        angle_y2=self.prev-self.feet_slider.val
        rad_y2 = np.radians(angle_y2)
        R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

        feet = []

        for l in range(len(self.legs)):
            if l % 2 == 0:
                feet.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(self.legs[l].args[1]))))
            else:
                feet.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.legs[l].args[1]))))

        plotter(self.ax).plot()
        body.plot(self.ax)

        new=[]

        for foot in range(len(feet)):
            new.append(leg(self.legs[foot].args[0], feet[foot], self.legs[foot].args[2]))
            new[foot].plot(self.ax)

        #t.legs=new
        self.legs=new
        #self.prev=angle_y

        self.fig.canvas.draw_idle()


    def update_thighs(self):

        angle_y = self.thighs_slider.val
        rad_y = np.radians(angle_y)
        R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

        angle_y2 = -self.thighs_slider.val
        rad_y2 = np.radians(angle_y2)
        R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

        plotter(self.ax).plot()
        body.plot(self.ax)

        l=[]
        v = []
        t = []
        for i in range(len(self.thighs)):
            if i % 2 == 0:
                v.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(self.thighs[i].args[1]))))
            else:
                v.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.thighs[i].args[1]))))
            t.append(thighs(self.thighs[i].args[0], v[i]))
            t[i].plot(self.ax)
            l.append(leg(v[i],self.legs[i].args[1],t[i].args[0]))
            l[i].plot(self.ax)

        self.thighs=t
        self.legs=l
        self.prev=self.feet_slider.val

        self.fig.canvas.draw_idle()

    def create_slider(self):
        axcolor = 'lightgoldenrodyellow'
        t_y = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
        self.thighs_slider = Slider(t_y, 'hip', -65, 25, valinit=0)

        f_y = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
        self.feet_slider = Slider(f_y, 'knee', 0, 90, valinit=0)

    def __init__(self, fig, thighs, legs, ax):
        self.create_slider()
        self.fig = fig
        self.thighs = thighs
        self.legs = legs
        self.ax = ax
        self.prev=self.feet_slider.val