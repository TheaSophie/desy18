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
with open ('/home/summerstudent/checkmate2/bin/ArrayStorage/AL_tanB6_352_withHiggs.pkl') as input:
#with open ('/home/summerstudent/checkmate2/bin/ArrayStorage/ArrayList_6tanBpoints_352GeV.pkl') as input:
    ArrayList = pickle.load(input)
    #ArrayList = [rArray,AnalysisArray,SignalArray]

print ArrayList
'''   
#create TanBArray  
TanBArray = np.arange(2, 50, 8)#2
#TanBArray = np.arange(1, 3, 1)#1,2

print TanBArray

rArray = ArrayList[0]
print rArray

rArray[0] = 0.923437242568
rArray[3] = 0.813848965673
rArray[4] = 0.957357529542

TanBArray = np.array(TanBArray)#.reshape((12,12))
rArray = np.array(rArray)#.reshape((12,12))

#rArray = np.round(rArray, 2)
print rArray

rValues = [float(x) for x in rArray]

#for i in range(0, 12):
#	 rValues.append(float(rArray[i]))
	 #rArray_i = round(rArray_i, 2)
	 #rArray[i] = rArray_i
	 #rArray.append(rArray_+str(i))
	 
print TanBArray
print rValues

saveTitle = 'ppTOgaugau_6points_tanBPlane_13Tev_500000Events_checkmate2_includingHiggs'

fS.PlottingTanBr(TanBArray, rValues, saveTitle)
'''
