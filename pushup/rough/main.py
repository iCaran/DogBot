import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from matplotlib.widgets import Button
from posture import change

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

def update():
    global ax, fig, b, thigh_obj, leg_obj, prev, switch
    change(ax, fig, b, thigh_obj, leg_obj, prev)
    switch=(switch+1)%2
    prev = states[switch]
    button.label.set_text(states[(switch+1)%2])

# Connect the button to the click event handler
button.on_clicked(lambda val: update())

plt.show()
