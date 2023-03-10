import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

fig = plt.figure()
ax = plt.axes(projection="3d")

vec = np.array([0, 0, 100])

ax.set_xlim([-150, 150])
ax.set_ylim([-150, 150])
ax.set_zlim([0, 150])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

axcolor = 'lightgoldenrodyellow'
ax_y = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
angle_y_slider = Slider(ax_y, 'Y', 0, 90.0, valinit=0.0)

def update(val):
    angle_z = angle_y_slider.val
    rad_y = np.radians(angle_z)
    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)], [0, 1, 0], [-np.sin(rad_y), 0, np.cos(rad_y)]])

    vec_new = np.identity(3).dot(R_y.dot(np.identity(3).dot(vec)))
    #line.set_data([0, vec_new[0]], [0, vec_new[1]])
    #line.set_3d_properties([0, vec_new[2]])
    ax.clear()
    ax.set_xlim([-150, 150])
    ax.set_ylim([-150, 150])
    ax.set_zlim([0, 150])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.quiver(0, 0, 0, vec_new[0], vec_new[1], vec_new[2], arrow_length_ratio=0.1)

    fig.canvas.draw_idle()

angle_y_slider.on_changed(update)

#line, = ax.plot([0, vec[0]], [0, vec[1]], [0, vec[2]])
ax.quiver(0,0,0,vec[0],vec[1],vec[2], arrow_length_ratio=0.1)

plt.show()