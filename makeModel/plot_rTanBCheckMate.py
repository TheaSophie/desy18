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


#with open ('/home/summerstudent/checkmate/bin/ArrayStorage/rArray.pkl') as input:
with open ('/home/summerstudent/checkmate/bin/ArrayStorage/rArray_13Tev_nn_cc_nc_100000.pkl') as input:
    ArrayList = pickle.load(input)
    #ArrayList = [rArray,AnalysisArray,SignalArray]

#create TanBArray  
TanBArray = np.arange(2, 50, 2)

rArray = []
rArray.append(ArrayList[0])

TanBArray= np.array(TanBArray)
rArray=np.array(rArray)

fS.PlottingTanBr(TanBArray, rArray)
