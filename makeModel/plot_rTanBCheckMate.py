#! /bin/bash

#### Plot ######################################################
#### plot r of CheckMate of the tanBeta Plane

#### import all needed packages
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
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


#with open ('/home/summerstudent/checkmate/bin/ArrayStorage/ArrayList.pkl') as input:
with open ('/home/summerstudent/checkmate/bin/ArrayStorage/ArrayList_12tanBpoints.pkl') as input:
#with open ('/home/summerstudent/checkmate/bin/ArrayStorage/rArray_13Tev_nn_cc_nc_100000.pkl') as input:
    ArrayList = pickle.load(input)
    #ArrayList = [rArray,AnalysisArray,SignalArray]

print ArrayList
    
#create TanBArray  
TanBArray = np.arange(2, 50, 4)#2
#TanBArray = np.arange(1, 3, 1)#1,2

print TanBArray

rArray = ArrayList[0]
print rArray

rArray[2] = 0.931040928048
rArray[3] = 0.50568648183
rArray[6] = 0.50568648183
rArray[10] = 0.505686457274

TanBArray = np.array(TanBArray)#.reshape((12,12))
rArray = np.array(rArray)#.reshape((12,12))

#rArray = np.round(rArray, 2)
print rArray

for i in range(0, 12):
	 rArray_i = float(rArray[i])
	 rArray_i = round(rArray_i, 2)
	 rArray[i] = rArray_i
	 #rArray.append(rArray_+str(i))
	 
print TanBArray
print rArray

saveTitle = 'ppTOgaugau_12points_tanBPlane_13Tev_200000Events'

fS.PlottingTanBr(TanBArray, rArray, saveTitle)
