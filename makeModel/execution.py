#### Execution #######################################
#### Create Arrays for different Branching Ratios

#### import all needed packages
import pyslha
import functions as f
import os
import matplotlib.pyplot as pyplot
import numpy as np
import cPickle as pickle
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict


#### create the two Arrays which should be plotted against each other
MA0 = []
TanB = []

#create list for fstate, give Number for HiggsSector in SLHA File
#fstate = [1000022,1000022]
HiggsNumber = 36

BRs = {}
counter = 0
count = 0
for fstate in [[-1000024,1000024],[-1000037,1000024],[-1000024,1000037],[-1000037,1000037],[1000022,1000022],[1000022,1000023],[1000022,1000025],[1000022,1000035],[1000023,1000023],[1000023,1000025],[1000023,1000035],[1000025,1000025],[1000025,1000035],[1000035,1000035]]:
#1: chargino1 chargino1
#2: chargino2 chargino1
#3: chargino1 chargino2
#4: chargino2 chargino2
#5: neutralino1 neutralino1
#6: neutralino1 neutralino2
#7: neutralino1 neutralino3
#8: neutralino1 neutralino4
#9: neutralino2 neutralino2
#10: neutralino2 neutralino3
#11: neutralino2 neutralino4
#12: neutralino3 neutralino3
#13: neutralino3 neutralino4
#14: neutralino4 neutralino4
    key = 'BR' + str(count)
    count += 1
    BR = []
    MA0 = []
    TanB = []
    for x in np.arange(100,1000,450):#2loops times
        BRrow = []
        MA0row = []
        TanBrow = []
        for y in np.arange(2,50,24):#2loops = 4loops
            counter += 1
            br = f.getBR(x,y,counter,fstate,HiggsNumber)
            BRrow.append(br)
            print counter
            MA0row.append(x)
            TanBrow.append(y)
        BR.append(BRrow)
        MA0.append(MA0row)
        TanB.append(TanBrow)
    BRs[key] = np.array(BR)
    
MA0Array = np.array(MA0)
TanBArray = np.array(TanB)

#safe the Arrays in a list
ArrayList = [MA0Array,TanBArray,BRs]
with open("Arrays/ArrayList.pkl",'web') as outputFile:
    pickle.dump(ArrayList, outputFile, -1)
