# https://chat.openai.com/chat/ff8f378b-3e6a-4fc2-8fb4-998c9c1f15fa

import numpy as np
from graph import plotter
import time

#angles=[-30, 30, 45, -45]

starting_point = 1
ending_point = 224.2296679816934
num_divisions = 225

step = (ending_point - starting_point) / (num_divisions - 1)
a1 = [starting_point + step * i for i in range(num_divisions)]

s2 = (45 - starting_point) / (num_divisions - 1)
a2 = [starting_point + s2 * i for i in range(num_divisions)]

s3 = (30 - starting_point) / (num_divisions - 1)
a3 = [starting_point + s3 * i for i in range(num_divisions)]

def change(ax, fig, b, th, l, prev):

    """print(l.get_heads())
    old=l.get_heads()[0][2]"""

    if prev=="sit":
        print("standing...")
        for i in range(225):
            print(i)
            angle_y = -a3[i]
            angle_y2 = a3[i]
            leg_angle = a2[i]
            leg_angle2 = -a2[i]
            b.lift(a1[i])
            ang=[angle_y, angle_y2, leg_angle, leg_angle2]
            plot(ang, ax, th, l, b, fig)
    else:
        print("sitting...")
        for i in range(255):
            angle_y = a3[i]
            angle_y2 = -a3[i]
            leg_angle = -a2[i]
            leg_angle2 = a2[i]
            b.lift(-a1[i])
            ang = [angle_y, angle_y2, leg_angle, leg_angle2]
            plot(ang, ax, th, l, b, fig)

    """new = l.get_heads()[0][2]
    print(l.get_heads())"""

    #print(new-old)

    print("now %sing!" % ("sit" if prev=="stand" else "stand"))

def plot(ang, ax, th, l, b, fig):
    thighs = th.args[1]
    legs = l.args[1]

    rad_y = np.radians(ang[0])
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    rad_y2 = np.radians(ang[1])
    R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

    leg_rad = np.radians(ang[2])
    leg_R = np.array([[np.cos(leg_rad), 0, np.sin(leg_rad)], [0, 1, 0], [-np.sin(leg_rad), 0, np.cos(leg_rad)]])

    leg_rad2 = np.radians(ang[3])
    leg_R2 = np.array([[np.cos(leg_rad2), 0, np.sin(leg_rad2)], [0, 1, 0], [-np.sin(leg_rad2), 0, np.cos(leg_rad2)]])

    plotter(ax).plot()
    b.plot(ax)

    v = []
    v2 = []
    for i in range(len(thighs)):
        if i % 2 == 0:
            v.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(thighs[i]))))
        else:
            v.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(thighs[i]))))

    for i in range(len(legs)):
        if i % 2 == 0:
            v2.append(np.identity(3).dot((leg_R.dot(np.identity(3).dot(legs[i])))))
        else:
            v2.append(np.identity(3).dot((leg_R2.dot(np.identity(3).dot(legs[i])))))

    th.update(v)
    th.plot(ax)
    l.update(v2)
    l.plot()

    #fig.canvas.draw_idle()

    time.sleep(0.5)