import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from dump import export


A = [[-230.14564298, -160.75, 779.40537747], [230.14564298, -160.75, 779.40537747], [-230.14564298, 160.75, 779.40537747], [230.14564298, 160.75, 779.40537747]]
B = [[-127.24033134, -160.75, 778.05231466], [333.05095462, -160.75, 778.05231466], [-127.24033134, 160.75, 778.05231466], [333.05095462, 160.75, 778.05231466]]

ends=[]

for i in range(4):
    center = ((A[i][0] + B[i][0]) / 2, (A[i][1] + B[i][1]) / 2, (A[i][2] + B[i][2]) / 2)
    print()
    print(center)

    distance = np.sqrt((B[i][0] - A[i][0])**2 + (B[i][1] - A[i][1])**2 + (B[i][2] - A[i][2])**2)
    radius = distance/2

    print(distance)
    print(radius)

    theta = np.linspace(0, np.pi, 60)

    x = center[0] - radius * np.cos(theta)
    y = [center[1]] + radius * np.zeros_like(theta)
    z = (center[2] - radius * np.sin(theta))

    # x=x[::-1]

    print(x)

    ends.append([x, y, z])

print(ends)

export(ends)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in ends:
    ax.plot(i[0], i[1], i[2])
    #ax.plot(i[0][-1], i[1][-1], i[2][-1], color='blue', linewidth=20)

    # Plot a large ball at the point
    ax.scatter(i[0][-1], i[1][-1], i[2][-1], s=100, color='red')

# Set the lower and upper limits of the x-axis
ax.set_xlim([-300, 400])

# Set the lower and upper limits of the y-axis
ax.set_ylim([-150, 150])

# Set the lower and upper limits of the z-axis
ax.set_zlim([900, 200])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()