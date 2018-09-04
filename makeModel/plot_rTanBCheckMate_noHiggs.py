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


with open ('/home/summerstudent/checkmate2/bin/ArrayStorage/ArrayList_6tanBpoints_352GeV.pkl') as input:
    ArrayList = pickle.load(input)
print ArrayList

with open ('/home/summerstudent/Desktop/desy18/makeModel/Arrays/AL_noHiggs2.pkl') as input2:
    ArrayList2 = pickle.load(input2)
print ArrayList2

with open ('/home/summerstudent/Desktop/desy18/makeModel/Arrays/AL_noHiggs3.pkl') as input3:
    ArrayList3 = pickle.load(input3)
print ArrayList3


TanBArray = np.arange(2, 50, 8)#2
print TanBArray

rArray = ArrayList[0]
rArray[1] = 0.920519776893
rArray[3] = 0.983348057321
rArray[5] = 0.920519776893

rArray2 = ArrayList2[0]
rArray2[2] = 0.951899374257
rArray2[3] = 0.774770812218

rArray3 = ArrayList3[0]
rArray3[0] = 0.951899374257
rArray3[1] = 0.795755362564
rArray3[2] = 0.857979991787
rArray3[4] = 0.920519776893
rArray3[5] = 0.779528406486

TanBArray = np.array(TanBArray)#.reshape((12,12))
rArray = np.array(rArray)#.reshape((12,12))
rArray2 = np.array(rArray2)
rArray3 = np.array(rArray3)

rValues = [float(x) for x in rArray]
rValues2 = [float(x) for x in rArray2]
rValues3 = [float(x) for x in rArray3]

print TanBArray
print rValues
print rValues2
print rValues3

a = 0.3333333333333 #13

rValuesCombined = [a*(rValues[0]+rValues2[0]+rValues3[0]), a*(rValues[1]+rValues2[1]+rValues3[1]), a*(rValues[2]+rValues2[2]+rValues3[2]), a*(rValues[3]+rValues2[3]+rValues3[3]), a*(rValues[4]+rValues2[4]+rValues3[4]), a*(rValues[5]+rValues2[5]+rValues3[5])]

rValuesCombined = np.array(rValuesCombined)
print rValuesCombined

#rError = [,,,,,,]
#rError2 = [,,,,,,]

saveTitle = 'ppTOgaugau_6points_tanBPlane_13Tev_1500000Events_checkmate2_noHiggs'

#fS.PlottingTanBr(TanBArray, rValues, TanBArray, rValues2, rError2, saveTitle)
fS.PlottingTanBr3_noHiggs(TanBArray, rValuesCombined, saveTitle)
