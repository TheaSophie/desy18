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

#name = [7969,7973]

for i in np.arange(7969, 7993, 4): #tanBPlane ( 6 values) M_A0 = 352GeV
#for i in name:


    #copy the right SLHA file into that directory and name it shOutput1.slha
    CopyRenameCommand ="cp /home/summerstudent/Desktop/desy18/makeModel/OutputSusyhit_Feynhiggs/Folder600/susyhit_slha.out.fh-001_"+str(i)+" stau-analysis/shOutput1.slha"
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


    if i == 7969:  
        #copy the important uncertainty files:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB2'
        os.system(copyCommand)

    if i == 7973:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB10'
        os.system(copyCommand)

    if i == 7977:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB18'
        os.system(copyCommand)

    if i == 7981:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB26'
        os.system(copyCommand)

    if i == 7985:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB34'
        os.system(copyCommand)

    if i == 7989:
        copyCommand = 'mv ../results/combined_Higgs_stau_production ../results/combined_Higgs_gauginos_MA325_tanB42'
	os.system(copyCommand)
        
    #remove the .slha file
    deleteCommand = 'rm stau-analysis/shOutput1.slha'
    os.system(deleteCommand)
    
    #empty the directory
    #if i < 7988: #last one is 7989
    #directoryCommand = 'rm -r /home/summerstudent/checkmate2/results/combined_Higgs_stau_production/*'
    #os.system(directoryCommand)
    
rArray = np.array(rArray)
AnalysisArray = np.array(AnalysisArray)
SignalArray = np.array(SignalArray)


AL_tanB6_352_withHiggs2 = [rArray, AnalysisArray, SignalArray]
print AL_tanB6_352_withHiggs2

#put the pickle File in the CheckMATE/bin/ directory in Folder ArrayStorage
with open("ArrayStorage/AL_tanB6_352_withHiggs2.pkl",'web') as outputFile:
    pickle.dump(AL_tanB6_352_withHiggs2, outputFile, -1)
    


os.chdir(wd)
