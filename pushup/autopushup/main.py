import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from posture2 import change
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.2)

plotter(ax).plot()

b = body()
b.plot(ax)

thigh_dims = [[190, 0, 91], [-190, 0, 91], [190, 0, 91], [-190, 0, 91]]
thigh_obj = thighs(b, thigh_dims)
thigh_obj.plot(ax)
leg_dims = [[-200, 0, 0], [200, 0, 0], [-200, 0, 0], [200, 0, 0]]
leg_obj = legs(ax, thigh_obj, leg_dims)
leg_obj.plot()

plt.show()

states=["sit","stand"]
switch=0
prev=states[switch]
frame_count = 60

ani = FuncAnimation(fig, change, frames=frame_count, fargs=(ax, fig, b, thigh_obj, leg_obj, prev, frame_count), repeat=False, cache_frame_data=True)
ani.save('animation.mp4', fps=60)

plt.show()

switch = (switch + 1) % 2
prev = states[switch]

ani = FuncAnimation(fig, change, frames=frame_count, fargs=(ax, fig, b, thigh_obj, leg_obj, prev, frame_count), repeat=False, cache_frame_data=True)
ani.save('animation2.mp4', fps=60)

plt.show()
