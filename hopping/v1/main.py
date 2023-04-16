import matplotlib.pyplot as plt
from load import get_points
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
#import time
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(projection="3d")

plotter(ax).plot()

b = body()
b.plot(ax)

th=thighs(b)
lg = legs(ax, th)

t, k = get_points()

print(t)
print(k)

print(t[0]==t[1])

print()
print(t[1])
print(k[1])

thigh_obj = thighs(b)
leg_obj = legs(ax, thigh_obj)

"""for i in range(57):
    thigh_obj.angle_plot([t[0][i], t[1][i], t[2][i], t[3][i]], ax)
    leg_obj.angle_plot([k[0][i], k[1][i], k[2][i], k[3][i]])

    thigh_obj.plot(ax)
    leg_obj.plot()"""

def change(frame):
    i=frame
    thigh_obj.angle_plot([t[1][i], t[1][i], t[1][i], t[1][i]], ax)
    leg_obj.angle_plot([k[1][i], k[1][i], k[1][i], k[1][i]])

    plotter(ax).plot()
    b.plot(ax)
    thigh_obj.plot(ax)
    leg_obj.plot()

ani = FuncAnimation(fig, change, frames=60, fargs=(), repeat=False)
ani.save('animation.mp4', fps=60)

"""change = hop_on

def init():
    pass

ani = FuncAnimation(fig, change, frames=60, fargs=(ax, fig, b, th, lg, t_a, k_a), interval=16, init_func=init, repeat=False)
#ani.save('animation.mp4', fps=60)"""

plt.show()
