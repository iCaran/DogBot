import numpy as np

# straight af
# angles=[-64.41, 64.41, 90, -90]

# random 1
# angles = [55, -55, -45, 45]

# random 2
angles = [-45, 40, 65, -65]

# angles = [-30, 30, 45, -45]
def change(th, l, ang=None):

    global angles

    if ang is not None:
        angles=ang

    thighs = th.args[1]
    legs = l.args[1]

    angle_y = angles[0]
    angle_y2 = angles[1]
    leg_angle = angles[2]
    leg_angle2 = angles[3]

    rad_y = np.radians(angle_y)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    rad_y2 = np.radians(angle_y2)
    R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

    leg_rad = np.radians(leg_angle)
    leg_R = np.array([[np.cos(leg_rad), 0, np.sin(leg_rad)], [0, 1, 0], [-np.sin(leg_rad), 0, np.cos(leg_rad)]])

    leg_rad2 = np.radians(leg_angle2)
    leg_R2 = np.array([[np.cos(leg_rad2), 0, np.sin(leg_rad2)], [0, 1, 0], [-np.sin(leg_rad2), 0, np.cos(leg_rad2)]])

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
    l.update(v2)