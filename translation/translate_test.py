import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

#defining points
#points = np.array([[249.75,126.25,44], [300.75,160.75,44], [110.75,160.75,135], [310.75, 160.75, 135], 
#                  [-249.75,126.25,44], [-300.75,160.75,44], [-110.75,160.75,135],[-310.75, 160.75, 135],
#                 [-249.75,-126.25,44], [-300.75,-160.75,44], [-110.75,-160.75,135], [-310.75,-160.75, 135],
#                [249.75,-126.25,44], [300.75,-160.75,44], [110.75,-160.75,135], [310.75, -160.75, 135]])

#plotting the graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#plotting the slider
axcolor = 'lightgoldenrodyellow'
axx = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
axy = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
axz = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)

#defining the slider
sx = Slider(axx, 'X', -300, 300, valinit=0)
sy = Slider(axy, 'Y', -300, 300, valinit=0)
sz = Slider(axz, 'Z', 1, 50, valinit=0)


def update_x(val):
        x = sx.val
        ax.clear()
        #upper base
        points = np.array([[249.75,126.25,44], [-249.75,126.25,44], [-249.75,-126.25,44], [249.75,-126.25,44]])
        #taking each 2 points
        for i in range(0, len(points)-1):

                vector = points[i+1] - points[i]
                ax.quiver(points[i][0] + x, points[i][1], points[i][2], vector[0], vector[1], vector[2], color='red', arrow_length_ratio=0.01)

        vector1= points[len(points)-1] - points[0]
        ax.quiver(points[0][0] + x, points[0][1], points[0][2], vector1[0], vector1[1], vector1[2], color='red', arrow_length_ratio=0.01)

        #extended point
        pointsextended =  np.array([[300.75,126.25,44], [-300.75,126.25,44], [-300.75, -126.25, 44], [300.75, -126.25, 44]])

        for i in range(0, len(points)-1):

                vector2 = pointsextended[i] - points[i]
                ax.quiver(points[i][0] + x, points[i][1], points[i][2], vector2[0], vector2[1], vector2[2], color='blue', arrow_length_ratio=0.01)

        vector3= pointsextended[len(pointsextended)-1] - points[len(points)-1]
        ax.quiver(points[len(points)-1][0] + x, points[len(points)-1][1], points[len(points)-1][2], vector3[0], vector3[1], vector3[2], color='blue', arrow_length_ratio=0.01)

        #joining between extended point and knee
        point = np.array([[300.75,160.75,44],[-300.75,160.75,44],[-300.75,-160.75,44],[300.75,-160.75,44]])

        for i in range(0,len(point)-1):
                vect = point[i] - pointsextended[i]
                ax.quiver(pointsextended[i][0] + x,pointsextended[i][1],pointsextended[i][2],vect[0],vect[1],vect[2], color='blue', arrow_length_ratio=0.01)

        vect1 = point[len(point)-1] - pointsextended[len(pointsextended)-1]
        ax.quiver(pointsextended[len(pointsextended)-1][0] + x,pointsextended[len(pointsextended)-1][1],pointsextended[len(pointsextended)-1][2],vect1[0],vect1[1],vect1[2], color='blue', arrow_length_ratio=0.01)

        #knee
        pointsknee = np.array([[110.75,160.75,135], [-110.75,160.75,135], [-110.75,-160.75,135], [110.75,-160.75,135]])

        for i in range(0, len(pointsknee)-1):
                vector4 = pointsknee[i] - point[i]
                ax.quiver(point[i][0] + x, point[i][1], point[i][2], vector4[0], vector4[1], vector4[2], color='blue', arrow_length_ratio=0.01)

        vector5= pointsknee[len(pointsknee)-1] - point[len(point)-1]
        ax.quiver(point[len(point)-1][0] + x, point[len(point)-1][1], point[len(point)-1][2], vector5[0], vector5[1], vector5[2], color='blue', arrow_length_ratio=0.01)

        #foot
        pointsfoot = np.array([[310.75, 160.75, 135],[-310.75, 160.75, 135],[-310.75, -160.75, 135],[310.75, -160.75, 135]])

        for i in range (0, len(pointsfoot)-1):
                vector6 = pointsfoot[i] - pointsknee[i]
                ax.quiver(pointsknee[i][0] + x, pointsknee[i][1], pointsknee[i][2], vector6[0], vector6[1], vector6[2], color='blue',  arrow_length_ratio=0.01)

        vector7 = pointsfoot[len(pointsfoot)-1] - pointsknee[len(pointsknee)-1]
        ax.quiver(pointsknee[len(pointsknee)-1][0] + x, pointsknee[len(pointsknee)-1][1], pointsknee[len(pointsknee)-1][2], vector7[0], vector7[1], vector7[2], color='blue', arrow_length_ratio=0.01)


        # Set the axis limits
        ax.set_xlim([-400, 400])
        ax.set_ylim([-350, 350])
        ax.set_zlim([200, 0])

        # Add labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('DOGYBOT')

        plt.draw()

def update_y(val):
        y = sy.val
        ax.clear()
        #upper base
        points = np.array([[249.75,126.25,44], [-249.75,126.25,44], [-249.75,-126.25,44], [249.75,-126.25,44]])
        #taking each 2 points
        for i in range(0, len(points)-1):

                vector = points[i+1] - points[i]
                ax.quiver(points[i][0], points[i][1] + y, points[i][2], vector[0], vector[1], vector[2], color='red', arrow_length_ratio=0.01)

        vector1= points[len(points)-1] - points[0]
        ax.quiver(points[0][0], points[0][1] + y, points[0][2], vector1[0], vector1[1], vector1[2], color='red', arrow_length_ratio=0.01)

        #extended point
        pointsextended =  np.array([[300.75,126.25,44], [-300.75,126.25,44], [-300.75, -126.25, 44], [300.75, -126.25, 44]])

        for i in range(0, len(points)-1):

                vector2 = pointsextended[i] - points[i]
                ax.quiver(points[i][0], points[i][1] + y, points[i][2], vector2[0], vector2[1], vector2[2], color='blue', arrow_length_ratio=0.01)

        vector3= pointsextended[len(pointsextended)-1] - points[len(points)-1]
        ax.quiver(points[len(points)-1][0], points[len(points)-1][1] + y, points[len(points)-1][2], vector3[0], vector3[1], vector3[2], color='blue', arrow_length_ratio=0.01)

        #joining between extended point and knee
        point = np.array([[300.75,160.75,44],[-300.75,160.75,44],[-300.75,-160.75,44],[300.75,-160.75,44]])

        for i in range(0,len(point)-1):
                vect = point[i] - pointsextended[i]
                ax.quiver(pointsextended[i][0],pointsextended[i][1] + y,pointsextended[i][2],vect[0],vect[1],vect[2], color='blue', arrow_length_ratio=0.01)

        vect1 = point[len(point)-1] - pointsextended[len(pointsextended)-1]
        ax.quiver(pointsextended[len(pointsextended)-1][0],pointsextended[len(pointsextended)-1][1] + y,pointsextended[len(pointsextended)-1][2],vect1[0],vect1[1],vect1[2], color='blue', arrow_length_ratio=0.01)

        #knee
        pointsknee = np.array([[110.75,160.75,135], [-110.75,160.75,135], [-110.75,-160.75,135], [110.75,-160.75,135]])

        for i in range(0, len(pointsknee)-1):
                vector4 = pointsknee[i] - point[i]
                ax.quiver(point[i][0], point[i][1] + y, point[i][2], vector4[0], vector4[1], vector4[2], color='blue', arrow_length_ratio=0.01)

        vector5= pointsknee[len(pointsknee)-1] - point[len(point)-1]
        ax.quiver(point[len(point)-1][0], point[len(point)-1][1] + y, point[len(point)-1][2], vector5[0], vector5[1], vector5[2], color='blue', arrow_length_ratio=0.01)

        #foot
        pointsfoot = np.array([[310.75, 160.75, 135],[-310.75, 160.75, 135],[-310.75, -160.75, 135],[310.75, -160.75, 135]])

        for i in range (0, len(pointsfoot)-1):
                vector6 = pointsfoot[i] - pointsknee[i]
                ax.quiver(pointsknee[i][0], pointsknee[i][1] + y, pointsknee[i][2], vector6[0], vector6[1], vector6[2], color='blue',  arrow_length_ratio=0.01)

        vector7 = pointsfoot[len(pointsfoot)-1] - pointsknee[len(pointsknee)-1]
        ax.quiver(pointsknee[len(pointsknee)-1][0], pointsknee[len(pointsknee)-1][1] + y, pointsknee[len(pointsknee)-1][2], vector7[0], vector7[1], vector7[2], color='blue', arrow_length_ratio=0.01)


        # Set the axis limits
        ax.set_xlim([-400, 400])
        ax.set_ylim([-350, 350])
        ax.set_zlim([200, 0])

        # Add labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('DOGYBOT')

        plt.draw()


def update_z(val):
        z = sz.val
        ax.clear()
        #upper base
        points = np.array([[249.75,126.25,44], [-249.75,126.25,44], [-249.75,-126.25,44], [249.75,-126.25,44]])
        #taking each 2 points
        for i in range(0, len(points)-1):

                vector = points[i+1] - points[i]
                ax.quiver(points[i][0], points[i][1], points[i][2] + z, vector[0], vector[1], vector[2], color='red', arrow_length_ratio=0.01)

        vector1= points[len(points)-1] - points[0]
        ax.quiver(points[0][0], points[0][1], points[0][2] + z, vector1[0], vector1[1], vector1[2], color='red', arrow_length_ratio=0.01)

        #extended point
        pointsextended =  np.array([[300.75,126.25,44], [-300.75,126.25,44], [-300.75, -126.25, 44], [300.75, -126.25, 44]])

        for i in range(0, len(points)-1):

                vector2 = pointsextended[i] - points[i]
                ax.quiver(points[i][0], points[i][1], points[i][2] + z, vector2[0], vector2[1], vector2[2], color='blue', arrow_length_ratio=0.01)

        vector3= pointsextended[len(pointsextended)-1] - points[len(points)-1]
        ax.quiver(points[len(points)-1][0], points[len(points)-1][1], points[len(points)-1][2] + z, vector3[0], vector3[1], vector3[2], color='blue', arrow_length_ratio=0.01)

        #joining between extended point and knee
        point = np.array([[300.75,160.75,44],[-300.75,160.75,44],[-300.75,-160.75,44],[300.75,-160.75,44]])

        for i in range(0,len(point)-1):
                vect = point[i] - pointsextended[i]
                ax.quiver(pointsextended[i][0],pointsextended[i][1],pointsextended[i][2] + z,vect[0],vect[1],vect[2], color='blue', arrow_length_ratio=0.01)

        vect1 = point[len(point)-1] - pointsextended[len(pointsextended)-1]
        ax.quiver(pointsextended[len(pointsextended)-1][0],pointsextended[len(pointsextended)-1][1],pointsextended[len(pointsextended)-1][2] + z,vect1[0],vect1[1],vect1[2], color='blue', arrow_length_ratio=0.01)

        #knee
        pointsknee = np.array([[110.75,160.75,135], [-110.75,160.75,135], [-110.75,-160.75,135], [110.75,-160.75,135]])

        for i in range(0, len(pointsknee)-1):
                vector4 = pointsknee[i] - point[i]
                ax.quiver(point[i][0], point[i][1], point[i][2] + z, vector4[0], vector4[1], vector4[2], color='blue', arrow_length_ratio=0.01)

        vector5= pointsknee[len(pointsknee)-1] - point[len(point)-1]
        ax.quiver(point[len(point)-1][0], point[len(point)-1][1], point[len(point)-1][2] + z, vector5[0], vector5[1], vector5[2], color='blue', arrow_length_ratio=0.01)

        #foot
        pointsfoot = np.array([[310.75, 160.75, 135],[-310.75, 160.75, 135],[-310.75, -160.75, 135],[310.75, -160.75, 135]])

        for i in range (0, len(pointsfoot)-1):
                vector6 = pointsfoot[i] - pointsknee[i]
                ax.quiver(pointsknee[i][0], pointsknee[i][1], pointsknee[i][2] + z, vector6[0], vector6[1], vector6[2], color='blue',  arrow_length_ratio=0.01)

        vector7 = pointsfoot[len(pointsfoot)-1] - pointsknee[len(pointsknee)-1]
        ax.quiver(pointsknee[len(pointsknee)-1][0], pointsknee[len(pointsknee)-1][1], pointsknee[len(pointsknee)-1][2] + z, vector7[0], vector7[1], vector7[2], color='blue', arrow_length_ratio=0.01)


        # Set the axis limits
        ax.set_xlim([-400, 400])
        ax.set_ylim([-350, 350])
        ax.set_zlim([200, 0])

        # Add labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('DOGYBOT')

        plt.draw()

sx.on_changed(update_x)
sy.on_changed(update_y)
sz.on_changed(update_z)

# Set the axis limits
ax.set_xlim([-400, 400])
ax.set_ylim([-350, 350])
ax.set_zlim([200, 0])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('DOGYBOT')

# Show the plot
plt.show()