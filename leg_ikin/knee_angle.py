import numpy as np
import math

a1 = 210.66798510366596
a2 = 200.0

p1=[]
p2=[]

def get(b, t, l, ax):
    global p1, p2

    p1=b.get_heads()
    p2=l.get_heads()

    """a1 = t.thigh_tail[0][2] - t.get_heads()[0][2]
    print(a1)

    a2 = l.get_heads()[0][2] - t.get_heads()[0][2]
    print(a2)

    print(p1[0])
    print(p2[0])"""

    """print(t.args[1][0])
    print(math.sqrt(t.args[1][0][0]**2 + t.args[1][0][1]**2 + t.args[1][0][2]**2))"""

    """print(l.args[1][0])
    print(math.sqrt(l.args[1][0][0]**2 + l.args[1][0][1]**2 + l.args[1][0][2]**2))"""

    dif=np.array(p2[0])-np.array(p1[0])
    #print(dif)

    r=math.sqrt(dif[0]**2 + dif[1]**2 + dif[2]**2)
    #print(r)
    m = get_angle(r)

    r = ax.quiver(p1[0][0], p1[0][1], p1[0][2], dif[0], dif[1], dif[2])
    b = ax.quiver(p1[0][0], p1[0][1], p1[0][2], 100, 0, 0)

    get_tangle(dif, m)


def get_tangle(dif, m):
    vec1 = dif
    vec2 = np.array([100, 0, 0])

    dot_product = np.dot(vec1, vec2)
    mag1 = np.linalg.norm(vec1)
    mag2 = np.linalg.norm(vec2)
    cos_theta = dot_product / (mag1 * mag2)
    theta = np.arccos(cos_theta)
    theta_deg = np.rad2deg(theta)

    print("thigh angle:",theta_deg-m)


def get_angle(r):
    global a1, a2

    if a1 + a2 <= r or a1 + r <= a2 or a2 + r <= a1:
        # The side lengths don't form a valid triangle
        print("invalid")
    # else: print("valid")

    cos_B = (a1**2 + a2**2 - r**2) / (2*a1*a2)
    B = math.degrees(math.acos(cos_B))
    """print(cos_B)
    print(B)

    print()"""

    A=a1
    B=a2
    C=r

    cos_A = (B ** 2 + C ** 2 - A ** 2) / (2 * B * C)
    cos_B = (A ** 2 + C ** 2 - B ** 2) / (2 * A * C)
    cos_C = (A ** 2 + B ** 2 - C ** 2) / (2 * A * B)

    A = math.degrees(math.acos(cos_A))
    B = math.degrees(math.acos(cos_B))
    C = math.degrees(math.acos(cos_C))

    """print("Angle A:", A)
    print("Angle B:", B)
    print("Angle C:", C)"""

    print("knee angle:", C)

    # print(A+B+C)

    return B
