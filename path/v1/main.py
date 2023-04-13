import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from dump import export

A = (230.14564298, 160.75, 779.40537747)
B = (333.05095462, 160.75, 778.05231466)

center = ((A[0] + B[0])/2, (A[1] + B[1])/2, (A[2] + B[2])/2)
print(center)

distance = np.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
radius = distance/2

print(distance)
print(radius)

theta = np.linspace(0, np.pi, 60)

x = center[0] + radius*np.cos(theta)
y = [center[1]] + radius*np.zeros_like(theta)
z = center[2] + radius*np.sin(theta)

export([x,y,z])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
