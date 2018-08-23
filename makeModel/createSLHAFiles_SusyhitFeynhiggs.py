#### Execution #######################################
#### Create Arrays for Plotting (same dimension as the r values of Checkmate -> get pickled Array and np.reshape(25,24)!])
#### Create SLHA InputFiles for CheckMATE - Output of Susyhit and Feynhiggs


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

count = 0
counter = 0

susyhit_folder = '/home/summerstudent/tools/susyhit/'

MA0 = []
TanB = []
for x in np.arange(100,1036,36):#26loops times ##vary 36 for more precision(->10xx)
    MA0row = []
    TanBrow = []
    count += 1
    for y in np.arange(2,52,2):#25loops = 600loops ##vary 2 for more precision(->5x)
        counter += 1
        MA0row.append(x)
        TanBrow.append(y)
        #create SLHA File
        fS. writeInputSLHASusyhit(x, y)#create SusyhitInputFile with x = MA0 value, y = tanBeta value
        DeleteEmptyLines = " sed '/^$/d' -i {}".format(susyhit_folder +'suspect2_lha.in')
        os.system(DeleteEmptyLines)
        fS.runSusyhit()#run Susyhit with new created SLHA InputFile
        fS.runFeynhiggsAfterSusyhit(counter)#create SusyhitInputFile with x = MA0 value, y = tanBeta value
        #SLHA files are safed to : /home/summerstudent/Desktop/desy18/makeModel/OutputSusyhit_Feynhiggs/susyhit_slha.out.fh-001_"+str(indize)

    MA0.append(MA0row)
    TanB.append(TanBrow)

MA0Array = np.array(MA0)
TanBArray = np.array(TanB)

#safe the Arrays in a list
ArrayList = [MA0Array, TanBArray]
print ArrayList
with open("Arrays_tanB_MA0_rScan/ArrayList.pkl",'web') as outputFile:
    pickle.dump(ArrayList, outputFile, -1)
