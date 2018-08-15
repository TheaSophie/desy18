#### Execution #######################################
#### Create Arrays for different Branching Ratios

#### import all needed packages
import pyslha
import functions as f
import functions_includeSusyhit as fS
import os
import matplotlib.pyplot as pyplot
import numpy as np
import cPickle as pickle
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict

#H or A0 ?? -> change #1]HiggsNumber (35 or 36), #2]SaveFolder (ArrayListH or ArrayList)(very bottom)

HiggsNumber = 35 #Higgs H #1]
#HiggsNumber = 36 #Higgs A0 #1]

#Create the two Arrays which should be plotted against each other
MA0 = []
TanB = []

BRs = {}
counter = 0
count = 0
for fstate in [[-1000024,1000024],[-1000037,1000024],[-1000024,1000037],[-1000037,1000037],[1000022,1000022],[1000022,1000023],[1000022,1000025],[1000022,1000035],[1000023,1000023],[1000023,1000025],[1000023,1000035],[1000025,1000025],[1000025,1000035],[1000035,1000035]]:
#BR1: chargino1 chargino1
#BR2: chargino2 chargino1
#BR3: chargino1 chargino2
#BR4: chargino2 chargino2
#BR5: neutralino1 neutralino1
#BR6: neutralino1 neutralino2
#BR7: neutralino1 neutralino3
#BR8: neutralino1 neutralino4
#BR9: neutralino2 neutralino2
#BR10: neutralino2 neutralino3
#BR11: neutralino2 neutralino4
#BR12: neutralino3 neutralino3
#BR13: neutralino3 neutralino4
#BR14: neutralino4 neutralino4
    count += 1
    key = 'BR' + str(count)
    BR = []
    MA0 = []
    TanB = []
    for x in np.arange(100,1000,36):#25loops times
        BRrow = []
        MA0row = []
        TanBrow = []
        for y in np.arange(2,50,2):#24loops = 600loops
            counter += 1
            br = fS.getBRSF(x, y, counter, fstate, HiggsNumber) #getBRSF(a0, tanb, indize, fstate, HiggsBlockNumber):
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
ArrayListH = [MA0Array, TanBArray, BRs] #2]
with open("Arrays_SusyhitFeynhiggs/ArrayListH.pkl",'web') as outputFile:
    pickle.dump(ArrayListH, outputFile, -1)

#ArrayList = [MA0Array, TanBArray, BRs] #2]
#with open("Arrays_SusyhitFeynhiggs/ArrayList.pkl",'web') as outputFile:
#    pickle.dump(ArrayList, outputFile, -1)
