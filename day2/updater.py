import numpy as np


# from leg import leg

class updater:

    def __init__(self, angle_y_slider, ax, fig, legs):
        self.angle_y_slider = angle_y_slider
        self.ax = ax
        self.fig = fig
        self.l1 = legs[0]
        self.l2 = legs[1]
        self.l3 = legs[2]
        self.l4 = legs[3]

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

        vec_new1 = np.identity(3).dot(R_y.dot(np.identity(3).dot(self.l1.foot)))
        vec_new3 = np.identity(3).dot(R_y.dot(np.identity(3).dot(self.l3.foot)))

        vec_new2 = np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.l2.foot)))
        vec_new4 = np.identity(3).dot(R_y2.dot(np.identity(3).dot(self.l4.foot)))
        # line.set_data([0, vec_new[0]], [0, vec_new[1]])
        # line.set_3d_properties([0, vec_new[2]])
        self.ax.clear()
        self.ax.set_xlim([-400, 400])
        self.ax.set_ylim([-200, 200])
        self.ax.set_zlim([400, 0])
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')

        self.ax.quiver(self.l1.knee_tail[0], self.l1.knee_tail[1], self.l1.knee_tail[2], [self.l1.knee[0]],
                       [self.l1.knee[1]], [self.l1.knee[2]], arrow_length_ratio=0.1)
        self.ax.quiver(self.l1.foot_tail[0], self.l1.foot_tail[1], self.l1.foot_tail[2], [vec_new1[0]], [vec_new1[1]],
                       [vec_new1[2]], arrow_length_ratio=0.1)

        self.ax.quiver(self.l2.knee_tail[0], self.l2.knee_tail[1], self.l2.knee_tail[2], [self.l2.knee[0]],
                       [self.l2.knee[1]], [self.l2.knee[2]], arrow_length_ratio=0.1)
        self.ax.quiver(self.l2.foot_tail[0], self.l2.foot_tail[1], self.l2.foot_tail[2], [vec_new2[0]], [vec_new2[1]],
                       [vec_new2[2]], arrow_length_ratio=0.1)

        self.ax.quiver(self.l3.knee_tail[0], self.l3.knee_tail[1], self.l3.knee_tail[2], [self.l3.knee[0]],
                       [self.l3.knee[1]], [self.l3.knee[2]], arrow_length_ratio=0.1)
        self.ax.quiver(self.l3.foot_tail[0], self.l3.foot_tail[1], self.l3.foot_tail[2], [vec_new3[0]], [vec_new3[1]],
                       [vec_new3[2]], arrow_length_ratio=0.1)

        self.ax.quiver(self.l4.knee_tail[0], self.l4.knee_tail[1], self.l4.knee_tail[2], [self.l4.knee[0]],
                       [self.l4.knee[1]], [self.l4.knee[2]], arrow_length_ratio=0.1)
        self.ax.quiver(self.l4.foot_tail[0], self.l4.foot_tail[1], self.l4.foot_tail[2], [vec_new4[0]], [vec_new4[1]],
                       [vec_new4[2]], arrow_length_ratio=0.1)

        self.fig.canvas.draw_idle()
