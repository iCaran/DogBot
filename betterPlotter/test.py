import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# define the starting point of the vector
start = [5, 5, 5]

# define the vector's magnitude
magnitude = 5

# define the rotation angle in degrees
theta = -30

# calculate the vector's components
x = magnitude * np.cos(np.radians(theta))
y = 0
z = magnitude * np.sin(np.radians(theta))

# plot the vector
ax.quiver(start[0], start[1], start[2], x, y, z, color='b')

# set the plot limits and labels
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# show the plot
plt.show()
