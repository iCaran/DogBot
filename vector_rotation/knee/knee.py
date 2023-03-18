import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.3)

ax.set_xlim([-400, 0])
ax.set_ylim([-200, 200])
ax.set_zlim([400, 0])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

axcolor = 'lightgoldenrodyellow'
ax_y = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
angle_y_slider = Slider(ax_y, 'Y', 0, 90, valinit=0)

knee=np.array([190, 0, 91])
foot=np.array([-200, 0, 0,])

knee_tail=np.array([-300.75, -160.75, 44])
knee_head=knee_tail+knee

foot_tail=knee_head
foot_head=foot_tail+foot

def update(val):
    angle_z = angle_y_slider.val
    rad_y = np.radians(angle_z)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    vec_new = np.identity(3).dot(R_y.dot(np.identity(3).dot(foot)))
    #line.set_data([0, vec_new[0]], [0, vec_new[1]])
    #line.set_3d_properties([0, vec_new[2]])
    ax.clear()
    ax.set_xlim([-400, 0])
    ax.set_ylim([-200, 200])
    ax.set_zlim([400, 0])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.quiver(knee_tail[0], knee_tail[1], knee_tail[2], [knee[0]], [knee[1]], [knee[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail[0], foot_tail[1], foot_tail[2], [vec_new[0]], [vec_new[1]], [vec_new[2]], arrow_length_ratio=0.1)

    fig.canvas.draw_idle()

angle_y_slider.on_changed(update)

#knee&foot
ax.quiver(knee_tail[0], knee_tail[1], knee_tail[2], [knee[0]], [knee[1]], [knee[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail[0], foot_tail[1], foot_tail[2], [foot[0]], [foot[1]], [foot[2]], arrow_length_ratio=0.1)

plt.show()
