import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from stand import change
from knee_angle import get

fig = plt.figure()
ax = plt.axes(projection="3d")

plotter(ax).plot()

b = body()

thigh_dims = [[190, 0, 91], [-190, 0, 91], [190, 0, 91], [-190, 0, 91]]
thigh_obj = thighs(b, thigh_dims)

leg_dims = [[-200, 0, 0], [200, 0, 0], [-200, 0, 0], [200, 0, 0]]
leg_obj = legs(ax, thigh_obj, leg_dims)

change(thigh_obj, leg_obj)

thigh_obj.plot(ax)
leg_obj.plot()

get(b, thigh_obj, leg_obj, ax)

plt.show()