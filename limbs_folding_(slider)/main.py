import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from base import body
from graph import plotter
from thigh import thighs
from thigh_updater import tu

from leg import leg
from updater import updater

fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.2)

plotter(ax).plot()

axcolor = 'lightgoldenrodyellow'
t_y = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
thighs_slider = Slider(t_y, 'hip', -65, 25, valinit=0)

f_y = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
feet_slider = Slider(f_y, 'knee', 0, 90, valinit=0)

body.plot(ax)

# thighs
t1 = thighs([-300.75, -160.75, 44], [190, 0, 91])
t2 = thighs([300.75, -160.75, 44], [-190, 0, 91])
t3 = thighs([-300.75, 160.75, 44], [190, 0, 91])
t4 = thighs([300.75, 160.75, 44], [-190, 0, 91])

# legs
l1 = leg([190, 0, 91], [-200, 0, 0], [-300.75, -160.75, 44])
l2 = leg([-190, 0, 91], [200, 0, 0], [300.75, -160.75, 44])
l3 = leg([190, 0, 91], [-200, 0, 0], [-300.75, 160.75, 44])
l4 = leg([-190, 0, 91], [200, 0, 0], [300.75, 160.75, 44])

legs=[l1,l2,l3,l4]

thighs = [t1, t2, t3, t4]

u = updater(feet_slider, ax, fig, legs)
t = tu(fig, thighs_slider, thighs, legs)

t.slider.on_changed(lambda val: t.update(t.slider, ax, u, feet_slider.val, val))
feet_slider.on_changed(lambda val: u.update(t, u.get_var(), val))

t1.plot(ax)
t2.plot(ax)
t3.plot(ax)
t4.plot(ax)

leg().plot_legs(legs, ax)

plt.show()
