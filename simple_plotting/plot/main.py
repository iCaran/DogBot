import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.set_xlim([-400, 400])
ax.set_ylim([-200, 200])
ax.set_zlim([150,0])

#body
ax.quiver(-249.75, -126.25, 44, 499.5, 0, 0, arrow_length_ratio=0)
ax.quiver(249.75, -126.25, 44, 0, 252.5, 0, arrow_length_ratio=0)
ax.quiver(249.75, 126.25, 44, -499.5, 0, 0, arrow_length_ratio=0)
ax.quiver(-249.75, 126.25, 44, 0, -252.5, 0, arrow_length_ratio=0)

#shoulder
ax.quiver(-249.75, -126.25, 44, -51, 0, 0, arrow_length_ratio=0)
ax.quiver(-300.75, -126.25, 44, 0, -34.5, 0, arrow_length_ratio=0)

ax.quiver(249.75, -126.25, 44, 51, 0, 0, arrow_length_ratio=0)
ax.quiver(300.75, -126.25, 44, 0, -34.5, 0, arrow_length_ratio=0)

ax.quiver(-249.75, 126.25, 44, -51, 0, 0, arrow_length_ratio=0)
ax.quiver(-300.75, 126.25, 44, 0, 34.5, 0, arrow_length_ratio=0)

ax.quiver(249.75, 126.25, 44, 51, 0, 0, arrow_length_ratio=0)
ax.quiver(300.75, 126.25, 44, 0, 34.5, 0, arrow_length_ratio=0)

#thigh
ax.quiver(-300.75, -160.75, 44, 190, 0, 91, arrow_length_ratio=0)
ax.quiver(300.75, -160.75, 44, -190, 0, 91, arrow_length_ratio=0)
ax.quiver(-300.75, 160.75, 44, 190, 0, 91, arrow_length_ratio=0)
ax.quiver(300.75, 160.75, 44, -190, 0, 91, arrow_length_ratio=0)

#foot
ax.quiver(-110.75, -160.75, 135, -200, 0, 0, arrow_length_ratio=0)
ax.quiver(-110.75, 160.75, 135, -200, 0, 0, arrow_length_ratio=0)
ax.quiver(110.75, -160.75, 135, 200, 0, 0, arrow_length_ratio=0)
ax.quiver(110.75, 160.75, 135, 200, 0, 0, arrow_length_ratio=0)

plt.show()