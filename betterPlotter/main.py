import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs

fig = plt.figure()
ax = plt.axes(projection="3d")

plotter(ax).plot()

b = body()
b.plot(ax)

# thigh_dims = [[190, 0, 91], [-190, 0, 91], [190, 0, 91], [-190, 0, 91]]
# thigh_obj = thighs(b, thigh_dims)

thigh_theta = 30
angles = [thigh_theta, 180-thigh_theta, thigh_theta, 180-thigh_theta]
thigh_obj = thighs(b)
thigh_obj.angle_plot(angles, ax)

# leg_dims = [[-200, 0, 0], [200, 0, 0], [-200, 0, 0], [200, 0, 0]]
# leg_obj = legs(ax, thigh_obj, leg_dims)

leg_theta = 30 - thigh_theta
ang = [180-leg_theta, leg_theta, 180-leg_theta, leg_theta]
leg_obj = legs(ax, thigh_obj)
leg_obj.angle_plot(ang)

thigh_obj.plot(ax)
leg_obj.plot()

plt.show()