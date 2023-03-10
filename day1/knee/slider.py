import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Define the original 3D vector and the angle about the y-axis
vector = np.array([1, 2, 3])
theta_y = 0

# Initialize Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Create the GUI slider for theta_y
axcolor = 'lightgoldenrodyellow'
axtheta_y = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider_y = Slider(axtheta_y, 'Theta Y', 0, 360, valinit=theta_y)

# Define the function to update the vector when the slider is moved
def update(val):
    global vector, theta_y
    theta_y = slider_y.val
    theta_y_rad = np.radians(theta_y)
    rotation_matrix = np.array([[np.cos(theta_y_rad), 0, np.sin(theta_y_rad)],
                                [0, 1, 0],
                                [-np.sin(theta_y_rad), 0, np.cos(theta_y_rad)]])
    new_vector = np.dot(rotation_matrix, vector)
    ax.clear()
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='r')
    ax.quiver(0, 0, 0, new_vector[0], new_vector[1], new_vector[2], color='b')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.canvas.draw_idle()

# Bind the slider to the update function
slider_y.on_changed(update)

# Display the visualization
plt.show()
