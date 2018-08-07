#### Plot ######################################################
#### plot the Arrays as Contourplots

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

#### load arrays
with open("Arrays/ArrayListH.pkl",'rb') as input:                        
    ArrayListH = pickle.load(input)
#ArrayList = [MA0Array,TanBArray,BRs] & BRS={'BR0':[BR(A0->charg1charg1)],'BR1':[BR(A0->charg2charg1)],...}

MA0Array = []
TanBArray = []

MA0Array = ArrayListH[0]
TanBArray = ArrayListH[1]

dictParticles = {'1':'charg1 charg1', '2':'charg1 charg2', '3':'charg2 charg1','4':'charg2 charg2', '5':'neutr1 neutr1', '6':'neutr1 neutr2', '7':'neutr1 neutr3', '8':'neutr1 neutr4', '9':'neutr2 neutr2', '10':'neutr2 neutr3', '11':'neutr2 neutr4', '12':'neutr3 neutr3', '13':'neutr3 neutr4', '14':'neutr4 neutr4'}



for i in range(1,14):
    BRArray = []
    BRArray = ArrayListH[2]['BR'+str(i)]
    Motherparticle = 'H'
    Daughterparticle = dictParticles[str(i)]
    f.plotting(MA0Array, TanBArray, BRArray, Motherparticle, Daughterparticle)
