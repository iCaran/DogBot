import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from leg import leg
from plotter import plotter
from updater import updater

fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.3)

plotter(ax).plot()

axcolor = 'lightgoldenrodyellow'
ax_y = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
angle_y_slider = Slider(ax_y, 'Y', 0, 90, valinit=0)

l1 = leg([190, 0, 91], [-200, 0, 0], [-300.75, -160.75, 44])
l2 = leg([-190, 0, 91], [200, 0, 0], [300.75, -160.75, 44])
l3 = leg([190, 0, 91], [-200, 0, 0], [-300.75, 160.75, 44])
l4 = leg([-190, 0, 91], [200, 0, 0], [300.75, 160.75, 44])

legs = [l1, l2, l3, l4]

u = updater(angle_y_slider, ax, fig, legs)

# https://chat.openai.com/chat/b072d1ec-9daa-425b-af79-60c906b773c0
angle_y_slider.on_changed(lambda val: u.update(val))
# angle_y_slider.on_changed(lambda event: u.update(event))
# angle_y_slider.on_changed(lambda val, event: u.update(val, event))
# angle_y_slider.on_changed(lambda tup: u.update(tup[0], tup[1]))

leg().plot_legs(legs, ax)

plt.show()
