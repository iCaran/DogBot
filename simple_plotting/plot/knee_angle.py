import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.set_xlim([-400, 400])
ax.set_ylim([-200, 200])
ax.set_zlim([0, 150])

# angle between knee and foot
'''
# k
k1_tail=np.array([-370.75, -160.75, 135])
k1_head=np.array([121, 34.5, -91])

# f
f1_tail=np.array([-249.75, -126.25, 44])
f1_head=np.array([-51, -34, 0])

# vectors

v1=k1_head-k1_tail
v2=f1_head-f1_tail

# Find the angle between the two vectors
cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
theta = np.arccos(cos_theta)

# Print the angle between the two vectors in degrees
print("The angle between vec1 and vec2 is:", np.degrees(theta), "degrees")

q = ax.quiver(f1_tail[0], f1_tail[1], f1_tail[2], [f1_head[0]], [f1_head[1]], [f1_head[2]], arrow_length_ratio=0.1)
q = ax.quiver(k1_tail[0], k1_tail[1], k1_tail[2], [k1_head[0]], [k1_head[1]], [k1_head[2]], arrow_length_ratio=0.1)
q = ax.quiver(0, 0, 0, [v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], arrow_length_ratio=0.1)
'''

knee=np.array([121, 34.5, -91])
foot=np.array([-51, -34, 0])

knee_tail=np.array([-370.75, -160.75, 135])
knee_head=knee_tail+knee

foot_tail=knee_head
foot_head=foot_tail+foot

#knee&foot
ax.quiver(knee_tail[0], knee_tail[1], knee_tail[2], [knee[0]], [knee[1]], [knee[2]], arrow_length_ratio=0.1)
ax.quiver(foot_tail[0], foot_tail[1], foot_tail[2], [foot[0]], [foot[1]], [foot[2]], arrow_length_ratio=0.1)

# Find the angle between the two vectors
#cos_theta = np.dot(knee, foot) / (np.linalg.norm(knee) * np.linalg.norm(foot))
cos_theta = np.dot(-foot, -knee) / (np.linalg.norm(-foot) * np.linalg.norm(knee))
theta = np.degrees(np.arccos(cos_theta))

# Print the angle between the two vectors in degrees
print("\nThe angle between vec1 and vec2 is:", 180-(np.degrees(theta)%360), "degrees")

plt.show()