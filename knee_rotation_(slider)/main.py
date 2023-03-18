import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.3)

ax.set_xlim([-400, 400])
ax.set_ylim([-200, 200])
ax.set_zlim([400, 0])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

axcolor = 'lightgoldenrodyellow'
ax_y = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
angle_y_slider = Slider(ax_y, 'Y', 0, 90, valinit=0)

# 1
knee1 = np.array([190, 0, 91])
foot1 = np.array([-200, 0, 0])

knee_tail1 = np.array([-300.75, -160.75, 44])
knee_head1 = knee_tail1 + knee1

foot_tail1 = knee_head1
foot_head1 = foot_tail1 + foot1

# 2
knee2 = np.array([-190, 0, 91])
foot2 = np.array([200, 0, 0])

knee_tail2 = np.array([300.75, -160.75, 44])
knee_head2 = knee_tail2 + knee2

foot_tail2 = knee_head2
foot_head2 = foot_tail2 + foot2

# 3
knee3 = np.array([190, 0, 91])
foot3 = np.array([-200, 0, 0])

knee_tail3 = np.array([-300.75, 160.75, 44])
knee_head3 = knee_tail3 + knee3

foot_tail3 = knee_head3
foot_head3 = foot_tail3 + foot3

# 4
knee4 = np.array([-190, 0, 91])
foot4 = np.array([200, 0, 0, ])

knee_tail4 = np.array([300.75, 160.75, 44])
knee_head4 = knee_tail4 + knee4

foot_tail4 = knee_head4
foot_head4 = foot_tail4 + foot4


def update(val):
    angle_y = angle_y_slider.val
    rad_y = np.radians(angle_y)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    angle_y2 = -angle_y_slider.val
    rad_y2 = np.radians(angle_y2)
    R_y2 = np.array([[np.cos(rad_y2), 0, np.sin(rad_y2)], [0, 1, 0], [-np.sin(rad_y2), 0, np.cos(rad_y2)]])

    vec_new1 = np.identity(3).dot(R_y.dot(np.identity(3).dot(foot1)))
    vec_new3 = np.identity(3).dot(R_y.dot(np.identity(3).dot(foot3)))

    vec_new2 = np.identity(3).dot(R_y2.dot(np.identity(3).dot(foot2)))
    vec_new4 = np.identity(3).dot(R_y2.dot(np.identity(3).dot(foot4)))
    # line.set_data([0, vec_new[0]], [0, vec_new[1]])
    # line.set_3d_properties([0, vec_new[2]])
    ax.clear()
    ax.set_xlim([-400, 400])
    ax.set_ylim([-200, 200])
    ax.set_zlim([400, 0])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    ax.quiver(knee_tail1[0], knee_tail1[1], knee_tail1[2], [knee1[0]], [knee1[1]], [knee1[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail1[0], foot_tail1[1], foot_tail1[2], [vec_new1[0]], [vec_new1[1]], [vec_new1[2]],
              arrow_length_ratio=0.1)

    ax.quiver(knee_tail3[0], knee_tail3[1], knee_tail3[2], [knee3[0]], [knee3[1]], [knee3[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail3[0], foot_tail3[1], foot_tail3[2], [vec_new3[0]], [vec_new3[1]], [vec_new3[2]],
              arrow_length_ratio=0.1)

    ax.quiver(knee_tail2[0], knee_tail2[1], knee_tail2[2], [knee2[0]], [knee2[1]], [knee2[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail2[0], foot_tail2[1], foot_tail2[2], [vec_new2[0]], [vec_new2[1]], [vec_new2[2]],
              arrow_length_ratio=0.1)

    ax.quiver(knee_tail4[0], knee_tail4[1], knee_tail4[2], [knee4[0]], [knee4[1]], [knee4[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail4[0], foot_tail4[1], foot_tail4[2], [vec_new4[0]], [vec_new4[1]], [vec_new4[2]],
              arrow_length_ratio=0.1)

    # fig.canvas.draw_idle()


angle_y_slider.on_changed(update)

# knee&foot
ax.quiver(knee_tail1[0], knee_tail1[1], knee_tail1[2], [knee1[0]], [knee1[1]], [knee1[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail1[0], foot_tail1[1], foot_tail1[2], [foot1[0]], [foot1[1]], [foot1[2]], arrow_length_ratio=0.1)

ax.quiver(knee_tail2[0], knee_tail2[1], knee_tail2[2], [knee2[0]], [knee2[1]], [knee2[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail2[0], foot_tail2[1], foot_tail2[2], [foot2[0]], [foot2[1]], [foot2[2]], arrow_length_ratio=0.1)

ax.quiver(knee_tail3[0], knee_tail3[1], knee_tail3[2], [knee3[0]], [knee3[1]], [knee3[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail3[0], foot_tail3[1], foot_tail3[2], [foot3[0]], [foot3[1]], [foot3[2]], arrow_length_ratio=0.1)

ax.quiver(knee_tail4[0], knee_tail4[1], knee_tail4[2], [knee4[0]], [knee4[1]], [knee4[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail4[0], foot_tail4[1], foot_tail4[2], [foot4[0]], [foot4[1]], [foot4[2]], arrow_length_ratio=0.1)

plt.show()
