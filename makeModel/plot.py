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

#MA0=[], TanB=[]

###create BranchingRatio Array for plotting
#BR = []
#counter = 1
#for i in np.arange(100,1000,50):#18loops times
#    BRrow = []
#    for j in np.arange(2,50,3):#16loops = 288 loops
#        counter += 1
#        br = f.getBR(i,j,counter)
#        BRrow.append(br[1])
#    BR.append(BRrow)
#    print counter

#def getBR(x,y,count):
#    writeInputFH({'MA0':x, 'TB':y}, 'InputFeynHiggs/mhmodp_'+str(count)+'.in')
#    runfeynh('InputFeynHiggs/mhmodp_'+str(count)+'.in')
#    readoutBR(count)
#getBR(600,45,1)

BR = []
counter = 0
for x in np.arange(100,1000,50):#18loops times 
    BRrow = []
    for y in np.arange(2,50,3):#16loops = 288 loops
        br = []
        counter +=1
        #f.writeInputFH({'MA0':x, 'TB':y}, 'InputFeynHiggs/mhmodp_'+str(counter)+'.in')
        #f.runfeynh("InputFeynHiggs/mhmodp_"+str(counter)+".in")
        br = f.readoutBR(counter)
        BRrow.append(br)
        print counter
    print BRrow
    BR.append(BRrow)

print BR
BRArray = np.array(BR)
print BRArray
