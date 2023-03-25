import numpy as np
from graph import plotter

angles = [-30, 30, 45, -45]
sum=0

def change(frame, ax, fig, b, th, l, prev, frame_count):
    thighs = th.args[1]
    legs = l.args[1]
    global sum

    if prev == "sit":
        if (sum==angles[0] or (sum==0 and frame>0.9*frame_count)):
            sum=0
            return
        print("standing...")
        angle_y = angles[0] * 1 / frame_count
        angle_y2 = angles[1] * 1 / frame_count
        leg_angle = angles[2] * 1 / frame_count
        leg_angle2 = angles[3] * 1 / frame_count
        b.lift(224.2296679816934 * 1 / frame_count)
        ang = [angle_y, angle_y2, leg_angle, leg_angle2, b]
        print(ang)
        sum+=angle_y
    else:
        if (sum==angles[0] or (sum==0 and frame>0.9*frame_count)):
            sum=0
            return
        print("sitting...")
        angle_y = -angles[0] * 1 / frame_count
        angle_y2 = -angles[1] * 1 / frame_count
        leg_angle = -angles[2] * 1 / frame_count
        leg_angle2 = -angles[3] * 1 / frame_count
        b.lift(-224.2296679816934 * 1 / frame_count)
        ang = [angle_y, angle_y2, leg_angle, leg_angle2, b]
        print(ang)
        sum -= angle_y

    rad_y = np.radians(angle_y)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    rad_y2 = np.radians(angle_y2)
    R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

    leg_rad = np.radians(leg_angle)
    leg_R = np.array([[np.cos(leg_rad), 0, np.sin(leg_rad)], [0, 1, 0], [-np.sin(leg_rad), 0, np.cos(leg_rad)]])

    leg_rad2 = np.radians(leg_angle2)
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

    print("now %sing!" % ("sit" if prev == "stand" else "stand"))
    print(frame)

    fig.canvas.draw_idle()

    return [ax, fig, b, th, l]


#fig = plt.figure
