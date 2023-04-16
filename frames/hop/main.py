import matplotlib.pyplot as plt
from ikin import get, export, clean
from path_frames import get_points
from base import body
from graph import plotter
from thigh import thighs
from legs import legs
from path_frames import export_angles

fig = plt.figure()
ax = plt.axes(projection="3d")

plotter(ax).plot()

b = body()
b.plot(ax)

th=thighs(b)
lg = legs(ax, th)

ends = get_points()

"""print([ends[0][0][0], ends[0][1][0], ends[0][2][0]])
print(b.get_heads()[0])
print()"""

t_a=[]
k_a=[]

c=0

for i in range(len(ends)):
    for j in range(len(ends[i][0])):
        c+=1
        if c==58 or c==59 or c==60 or c==178 or c==179 or c==180: continue
        print(c)
        get(b, ax, ends, i, j)
    t1, k1 = export()
    clean()
    t_a.append(t1)
    k_a.append(k1)

print()
print(t_a)
print(k_a)

print(len(t_a[0]))
print(len(k_a[0]))

export_angles(t_a, k_a)

plt.show()
