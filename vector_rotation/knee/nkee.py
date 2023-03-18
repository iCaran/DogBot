import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Define the original 3D vector and the angle about the y-axis
knee=np.array([190, 0, 91])
foot=np.array([-200, 0, 0,])

knee_tail=np.array([-300.75, -160.75, 44])
knee_head=knee_tail+knee

foot_tail=knee_head
foot_head=foot_tail+foot

theta_y = 0

# Initialize Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

ax.set_xlim([-400, 0])
ax.set_ylim([-200, 200])
ax.set_zlim([400, 0])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Create the GUI slider for theta_y
axcolor = 'lightgoldenrodyellow'
axtheta_y = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider_y = Slider(axtheta_y, 'Theta Y', 0, 360, valinit=theta_y)

# Define the function to update the vector when the slider is moved
def update(val):
    global knee, knee_tail, foot_tail, foot, theta_y
    theta_y = slider_y.val
    theta_y_rad = np.radians(theta_y)
    rotation_matrix = np.array([[np.cos(theta_y_rad), 0, np.sin(theta_y_rad)],
                                [0, 1, 0],
                                [-np.sin(theta_y_rad), 0, np.cos(theta_y_rad)]])
    new_vector = np.dot(rotation_matrix, foot)
    ax.clear()
    ax.quiver(knee_tail[0], knee_tail[1], knee_tail[2], [knee[0]], [knee[1]], [knee[2]], arrow_length_ratio=0.1)
    ax.quiver(foot_tail[0], foot_tail[1], foot_tail[2], [new_vector[0]], [new_vector[1]], [new_vector[2]],arrow_length_ratio=0.1)
    ax.set_xlim([-400, 0])
    ax.set_ylim([-200, 200])
    ax.set_zlim([400, 0])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    fig.canvas.draw_idle()

# Bind the slider to the update function
slider_y.on_changed(update)

ax.quiver(knee_tail[0], knee_tail[1], knee_tail[2], [knee[0]], [knee[1]], [knee[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail[0], foot_tail[1], foot_tail[2], [foot[0]], [foot[1]], [foot[2]], arrow_length_ratio=0.1)

# Display the visualization
plt.show()