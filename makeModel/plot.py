#### PLOT #######################################
#### Plotting different Branching Ratios


#### import all needed packages
import pyslha
import functions as f
import os
import matplotlib.pyplot as pyplot
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict

#f.getBRArray(x,y,count)
#f.plotting(Array1, Array2, Array3)

for i in np.arange(100,1000,50):#18loops times
    for j in np.arange(2,50,3):#16loops = 288 loops
        counter += 1
        f.getBRArray(i,j,counter)
        
