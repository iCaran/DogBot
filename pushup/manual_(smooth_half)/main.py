import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from matplotlib.widgets import Button
from posture import change
from matplotlib.animation import FuncAnimation

def button_clicked(event):
    print("standing")


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

states=["sit","stand"]
switch=0
prev=states[switch]

# Create the button
button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
button = Button(button_ax, states[1])

ani = None

animation_running = False

def update():
    global ax, fig, b, thigh_obj, leg_obj, prev, switch, animation_running, ani
    frame_count = 60
    ani = FuncAnimation(fig, change, frames=frame_count, fargs=(ax, fig, b, thigh_obj, leg_obj, prev, frame_count), repeat=False, cache_frame_data=True)
    plt.show()
    switch = (switch + 1) % 2
    prev = states[switch]
    button.label.set_text(states[(switch + 1) % 2])
    ani.save('animation2.mp4', fps=60)

# Connect the button to the click event handler
button.on_clicked(lambda val: update())

plt.show()
