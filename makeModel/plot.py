#import all needed packages
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#set up figure as 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = fig.gca(projection='3d')

#Data
X = np.array([[20, 20, 20, 20, 20],
           [22, 22, 22, 22, 22],
           [24, 24, 24, 24, 24],
           [26, 26, 26, 26, 26],
           [28, 28, 28, 28, 28]])#X=tanBeta
Y = np.array([[600, 605, 610, 615, 620],
           [600, 605, 610, 615, 620],
           [600, 605, 610, 615, 620],
           [600, 605, 610, 615, 620],
           [600, 605, 610, 615, 620]])#Y=MA0
#X, Y = np.meshgrid(X, Y)
Z = np.array([[0.00033629, 0.00033694, 0.00033759, 0.00033822, 0.00033885],
           [0.00029177, 0.00029233, 0.00029289, 0.00029344, 0.00029398],
           [0.00025642, 0.00025691, 0.0002574,  0.00025787, 0.00025834],
           [0.00022783, 0.00022826, 0.00022869, 0.0002291,  0.00022952],
           [0.00020432, 0.0002047,  0.00020508, 0.00020545, 0.00020581]])

#plot the surface
#surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.scatter(X, Y, Z, c='r', marker='o')

ax.set_xlabel('tan(Beta)')
ax.set_ylabel('M_A0')
ax.set_zlabel('BR')

pp = PdfPages('multipage.pdf')

#plt.plot([600,605,610,615,620],[20,22,24,26,28])

plt.show()

plt.savefig(pp, format='pdf')
pp.close()

