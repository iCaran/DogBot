import matplotlib.pyplot as plt
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from matplotlib.widgets import Button
from stand import stand
from sit import sit

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

# Create the button
button_ax = plt.axes([0.7, 0.05, 0.2, 0.075])
button = Button(button_ax, "stand")

button_ay = plt.axes([0.1, 0.05, 0.2, 0.075])
but = Button(button_ay, "sit")

# Connect the button to the click event handler
button.on_clicked(lambda val: stand(ax, fig, b, thigh_obj, leg_obj))
but.on_clicked(lambda val: sit(ax, fig, b, thigh_obj, leg_obj))

plt.show()
