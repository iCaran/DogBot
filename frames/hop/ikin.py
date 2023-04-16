import numpy as np
import math

a1 = 210.66798510366596
a2 = 200.0

t_a=[]
k_a=[]

def clean():
    global t_a, k_a

    t_a = []
    k_a = []

def export():
    global t_a, k_a

    print(t_a)
    print(k_a)

    #export_angles(t_a, k_a)
    return t_a, k_a

def get(b, ax, e, i, j):

    p1=b.get_heads()

    print([e[i][0][j], e[i][1][j], e[i][2][j]])
    print(p1[i])
    print()

    dif=np.array([e[i][0][j], e[i][1][j], e[i][2][j]])-np.array(p1[i])

    """print(dif)
    print()"""

    r=math.sqrt(dif[0]**2 + dif[1]**2 + dif[2]**2)
    kn, m = get_angle(r)

    th = get_tangle(dif, m)

    # print()
    t_a.append(th)
    k_a.append(kn)

    print("done")
    print()

def get_tangle(dif, m):
    vec1 = dif
    vec2 = np.array([-100, 0, 0])

    dot_product = np.dot(vec1, vec2)
    mag1 = np.linalg.norm(vec1)
    mag2 = np.linalg.norm(vec2)
    cos_theta = dot_product / (mag1 * mag2)
    theta = np.arccos(cos_theta)
    theta_deg = np.rad2deg(theta)

    #print("thigh angle:",theta_deg-m)

    return theta_deg-m

def get_angle(r):
    global a1, a2

    if a1 + a2 <= r or a1 + r <= a2 or a2 + r <= a1:
        # The side lengths don't form a valid triangle
        print("invalid")
    # else: print("valid")

    cos_B = (a1**2 + a2**2 - r**2) / (2*a1*a2)
    B = math.degrees(math.acos(cos_B))

    #print(B)

    A=a1
    B=a2
    C=r

    cos_A = (B ** 2 + C ** 2 - A ** 2) / (2 * B * C)
    cos_B = (A ** 2 + C ** 2 - B ** 2) / (2 * A * C)
    cos_C = (A ** 2 + B ** 2 - C ** 2) / (2 * A * B)

    A = math.degrees(math.acos(cos_A))
    B = math.degrees(math.acos(cos_B))
    C = math.degrees(math.acos(cos_C))

    # print("knee angle:", C)

    return C, B
