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


with open ('/home/summerstudent/checkmate2/bin/ArrayStorage/AL_tanB6_352_withHiggs.pkl') as input:
    ArrayList = pickle.load(input)
print ArrayList

with open ('/home/summerstudent/Desktop/desy18/makeModel/Arrays/AL_tanB6_352_withHiggs2.pkl') as input2:
    ArrayList2 = pickle.load(input2)
print ArrayList2

TanBArray = np.arange(2, 50, 8)#2
print TanBArray

rArray = ArrayList[0]

rArray[0] = 0.923437242568
rArray[3] = 0.813848965673
rArray[4] = 0.957357529542

rArray2 = ArrayList2[0]

rArray2[5] = 0.742063952015

TanBArray = np.array(TanBArray)#.reshape((12,12))
rArray = np.array(rArray)#.reshape((12,12))
rArray2 = np.array(rArray2)

rValues = [float(x) for x in rArray]
rValues2 = [float(x) for x in rArray2]

print TanBArray
print rValues
print rValues2

rValuesCombined = [0.5*(rValues[0]+rValues2[0]), 0.5*(rValues[1]+rValues2[1]), 0.5*(rValues[2]+rValues2[2]), 0.5*(rValues[3]+rValues2[3]), 0.5*(rValues[4]+rValues2[4]), 0.5*(rValues[5]+rValues2[5])]

print rValuesCombined

#rError = [,,,,,,]
#rError2 = [,,,,,,]

saveTitle = 'ppTOgaugau_6points_tanBPlane_13Tev_500000Events_checkmate2_includingHiggs2_run1_run2'

#fS.PlottingTanBr(TanBArray, rValues, TanBArray, rValues2, rError2, saveTitle)
fS.PlottingTanBr2(TanBArray, rValuesCombined, saveTitle)
