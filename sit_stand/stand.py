import numpy as np
from graph import plotter

def stand(ax, fig, b, th, l):
    thighs=th.args[1]
    legs=l.args[1]

    print("standing...")

    angle_y = -30
    rad_y = np.radians(angle_y)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    angle_y2 = 30
    rad_y2 = np.radians(angle_y2)
    R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

    leg_angle = 45
    leg_rad = np.radians(leg_angle)
    leg_R = np.array([[np.cos(leg_rad), 0, np.sin(leg_rad)], [0, 1, 0], [-np.sin(leg_rad), 0, np.cos(leg_rad)]])

    # angle_y2 = -self.angle_y_slider.val
    leg_angle2 = -45
    leg_rad2 = np.radians(leg_angle2)
    leg_R2 = np.array([[np.cos(leg_rad2), 0, np.sin(leg_rad2)], [0, 1, 0], [-np.sin(leg_rad2), 0, np.cos(leg_rad2)]])

    plotter(ax).plot()
    b.plot(ax)

    v = []
    v2=[]
    for i in range(len(thighs)):
        if i % 2 == 0:
            v.append(np.identity(3).dot(R_y.dot(np.identity(3).dot(thighs[i]))))
        else:
            v.append(np.identity(3).dot(R_y2.dot(np.identity(3).dot(thighs[i]))))

    for i in range(len(legs)):
        if i%2==0:
            v2.append(np.identity(3).dot((leg_R.dot(np.identity(3).dot(legs[i])))))
        else:
            v2.append(np.identity(3).dot((leg_R2.dot(np.identity(3).dot(legs[i])))))

    th.update(v)
    th.plot(ax)
    l.update(v2)
    l.plot()

    print("now standing!")

    fig.canvas.draw_idle()