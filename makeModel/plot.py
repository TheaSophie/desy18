#! /bin/bash

#### Plot ######################################################
#### plot the Arrays as Contourplots

#### import all needed packages
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
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

#### load arrays
#with open("Arrays_Feynhiggs/ArrayListH.pkl",'rb') as input:                        
#    ArrayListH = pickle.load(input)
with open ('Arrays_Feynhiggs/ArrayList.pkl','rb') as input:
    ArrayList = pickle.load(input)

    #ArrayList = [MA0Array,TanBArray,BRs] & BRS={'BR0':[BR(A0->charg1charg1)],'BR1':[BR(A0->charg2charg1)],...}

MA0Array = []
TanBArray = []

#MA0Array = ArrayListH[0]
#TanBArray = ArrayListH[1]

MA0Array = ArrayList[0]
TanBArray = ArrayList[1]

dictParticles = {'1':'charg1charg1', '2':'charg1charg2', '3':'charg2charg1','4':'charg2charg2', '5':'neutr1neutr1', '6':'neutr1neutr2', '7':'neutr1neutr3', '8':'neutr1neutr4', '9':'neutr2neutr2', '10':'neutr2neutr3', '11':'neutr2neutr4', '12':'neutr3neutr3', '13':'neutr3neutr4', '14':'neutr4neutr4'}


for i in range(1,15):
    print(i)
    BRArray = []
    #BRArray = ArrayListH[2]['BR'+str(i)]
    BRArray = ArrayList[2]['BR'+str(i)]
    Motherparticle = 'A'
    #Motherparticle = 'H'
    Daughterparticle = dictParticles[str(i)]
    print(Daughterparticle)
    f.plotting(MA0Array, TanBArray, BRArray, Motherparticle, Daughterparticle)
