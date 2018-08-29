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


#change into the right directory
wd = os.getcwd()
os.chdir('/home/summerstudent/checkmate2/bin/')


rArray = []
AnalysisArray = []
SignalArray = []

name = [7969,7973]

#for i in np.arange(7969, 7993, 4): #tanBPlane ( 6 values) M_A0 = 352GeV
for i in name:


    #copy the right SLHA file into that directory and name it shOutput1.slha
    CopyRenameCommand ="cp /home/summerstudent/Desktop/desy18/makeModel/OutputSusyhit_Feynhiggs/Folder600/susyhit_slha.out.fh-001_"+str(i)+" shOutput1.slha"
    os.system(CopyRenameCommand)

    #run CheckMATE
    runCommand = './CheckMATE stau-analysis/combined_higgs_stau.ini'
    os.system(runCommand)

    #read out the r value of results and everything + store in Pickle Data
    with open ('../results/combined_Higgs_stau_production/result.txt', 'rt') as gfile:

        lines = gfile.readlines()
        r = lines[2].split(": ")[1]
        r = r.rstrip()
        a = lines[3].split(": ")[1]
        a = a.rstrip()
        s = lines[4].split(": ")[1]
        s = s.rstrip()
        rArray.append(r)
        AnalysisArray.append(a)
        SignalArray.append(s)

        
rArray = np.array(rArray)
AnalysisArray = np.array(AnalysisArray)
SignalArray = np.array(SignalArray)


AL_tanB6_352_withHiggs = [rArray, AnalysisArray, SignalArray]
print AL_tanB6_352_withHiggs

#put the pickle File in the CheckMATE/bin/ directory in Folder ArrayStorage
with open("ArrayStorage/AL_tanB6_352_withHiggs.pkl",'web') as outputFile:
    pickle.dump(AL_tanB6_352_withHiggs, outputFile, -1)
    


os.chdir(wd)
