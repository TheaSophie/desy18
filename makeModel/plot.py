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

#### create the two Arrays which should be plotted against each other
MA0 = []
TanB = []

### create BranchingRatio Array for plotting
BR = []
counter = 0
for x in np.arange(100,1000,36):#25loops times
    BRrow = []
    MA0row = []
    TanBrow = []
    for y in np.arange(2,50,2):#24loops = 600 loops
        counter += 1
        br = f.getBR(x,y,counter)
        BRrow.append(br)
        print counter
        MA0row.append(x)
        TanBrow.append(y)
    print BRrow
    print MA0row
    print TanBrow
    BR.append(BRrow)
    MA0.append(MA0row)
    TanB.append(TanBrow)
    
print BR
BRArray = np.array(BR)
print BRArray
MA0Array = np.array(MA0)
TanBArray = np.array(TanB)
print MA0Array


### plot the Arrays in a contour plot
f.plotting(MA0Array, TanBArray, BRArray)
