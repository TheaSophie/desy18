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
with open("Arrays/ArrayList.pkl",'rb') as input:                        
    ArrayList = pickle.load(input)
#ArrayList = [MA0Array,TanBArray,BRs] & BRS={'BR0':[BR(A0->charg1charg1)],'BR1':[BR(A0->charg2charg1)],...}

MA0Array = []
TanBArray = []
BRArray = []

MA0Array = ArrayList[0]
TanBArray = ArrayList[1]
BRArray = ArrayList[2]['BR5']
Motherparticle = 'A0'
Daughterparticle1 = 'Neutr1'
Daughterparticle2 = 'Neutr1'


#### plotting the arrays
f.plotting(MA0Array, TanBArray, BRArray, Motherparticle, Daughterparticle1, Daughterparticle2)
