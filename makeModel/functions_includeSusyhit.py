##### functions ##################################
##### define the functions here that are needed to run and vary the parameters in combination with susyhit+feynhiggs

#### import all packages
import os
import pyslha
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict


#H or A0? (2)For EXECUTION: #1]1. runFeynhiggsAfterSusyhit Savecommand #2]3. readoutBR SLHAFile-directory/source
# (2)For PLOTTING: #1]4. plotting pyplot.xlabel 2]4. plotting pyplot.savefig


susyhit_folder = '/home/summerstudent/tools/susyhit/'
Feynhiggs_folder = '/home/summerstudent/Programs/feynhiggs/x86_64-Linux/bin/FeynHiggs' 


#### 1. let feynhiggs run in the command line mode with the input file,
def runFeynhiggsAfterSusyhit(indize):
    runCommand = Feynhiggs_folder+" "+susyhit_folder+"susyhit_slha.out#SLHA > /dev/null 2>&1"
    os.system(runCommand)
    safeCommand = "mv " + susyhit_folder + "/susyhit_slha.out.fh-001 /home/summerstudent/Desktop/desy18/makeModel/OutputSusyhit_Feynhiggs/susyhit_slha.out.fh-001_"+str(indize)
    safeCommandH = "mv " + susyhit_folder + "/susyhit_slha.out.fh-001 /home/summerstudent/Desktop/desy18/makeModel/OutputSusyhit_FeynhiggsH/susyhit_slha.out.fh-001_"+str(indize)
    os.system(safeCommand) #1]
    #os.system(safeCommandH) #1]
    
def runSusyhit():
    wd = os.getcwd()
    os.chdir(susyhit_folder)
    runCommand = "./run suspect2_lha.in"
    os.system(runCommand)
    os.chdir(wd)


#### 2. vary the input parameter
def writeInputSLHASusyhit(a0, tanb):
    SLHAfile = pyslha.readSLHAFile(susyhit_folder+'suspect2_lha.in')
    #BlockTanB1 = MINPAR #TanBeta is two times defined!! TanB=3
    #BlockA0 = EXTPAR #A0=26, TanB=25
    SLHAfile.blocks['MINPAR'][3] = tanb
    SLHAfile.blocks['EXTPAR'][25] = tanb
    SLHAfile.blocks['EXTPAR'][26] = a0
    pyslha.writeSLHAFile(susyhit_folder+'suspect2_lha.in', SLHAfile)


#### 3. reading out the branching ratio of the created FeynHiggs SLHA file
def readoutBR(indize, fstate, HiggsBlockNummer):
    branchr = 0
    #SLHAFile = pyslha.readSLHAFile('OutputSusyhit_Feynhiggs/susyhit_slha.out.fh-001_'+str(indize)) #2]
    SLHAFile = pyslha.readSLHAFile('OutputSusyhit_FeynhiggsH/susyhit_slha.out.fh-001_'+str(indize)) #2]
    particleBlock = HiggsBlockNummer
    for decay in SLHAFile.decays[particleBlock].decays:
        if decay.ids == fstate:#fstate = [1000022, 1000022] decay to neutralino1, neutralino1
            branchr = decay.br
    return branchr


#### 4. Plotting the output data in a nice contour plot
#write dictionary for title LATEX for duaghterparticles 
LatexDaughterparticle = {'charg1charg1':'$\chi^{-}_{1}\chi^{+}_{1}$', 'charg1charg2':'$\chi^{-}_{1}\chi^{+}_{2}$', 'charg2charg1':'$\chi^{-}_{2}\chi^{+}_{1}$', 'charg2charg2':'$\chi^{-}_{2}\chi^{+}_{2}$', 'neutr1neutr1':'$\chi^{0}_{1}\chi^{0}_{1}$', 'neutr1neutr2':'$\chi^{0}_{1}\chi^{0}_{2}$', 'neutr1neutr3':'$\chi^{0}_{1}\chi^{0}_{3}$', 'neutr1neutr4':'$\chi^{0}_{1}\chi^{0}_{4}$', 'neutr2neutr2':'$\chi^{0}_{2}\chi^{0}_{2}$', 'neutr2neutr3':'$\chi^{0}_{2}\chi^{0}_{3}$', 'neutr2neutr4':'$\chi^{0}_{2}\chi^{0}_{4}$', 'neutr3neutr3':'$\chi^{0}_{3}\chi^{0}_{3}$', 'neutr3neutr4':'$\chi^{0}_{3}\chi^{0}_{4}$', 'neutr4neutr4':'$\chi^{0}_{4}\chi^{0}_{4}$'}

def plotting(Array1, Array2, Array3, Motherparticle, Daughterparticle):
    fig = pyplot.figure()
    v = np.arange(0.00, 1.00, 0.02)
    CT = pyplot.contourf(Array1, Array2, Array3, v)
    CB = pyplot.colorbar(CT, shrink=0.8, extend='both')
    CS = pyplot.contour(Array1, Array2, Array3, 6, colors='k')
    pyplot.rc('text', usetex=True)
    pyplot.rc('font', family='serif')
    pyplot.xlabel(r'm$_{H}$ (GeV)') #1]
    #pyplot.xlabel(r'm$_{A}$ (GeV)') #1]
    pyplot.ylabel(r'$\tan{\beta}$')
    Decayparticles = LatexDaughterparticle[str(Daughterparticle)]
    pyplot.title(r'Branching Ratios('+str(Motherparticle)+r' $\rightarrow$ '+str(Decayparticles)+')')
    pyplot.clabel(CS, inline=1, fontsize=8)
    pyplot.savefig("Plots_SusyhitFeynhiggs/Plots_BR_H/contour_H_"+str(Daughterparticle)+".pdf") #save #2]
    #pyplot.savefig('Plots_SusyhitFeynhiggs/Plots_BR_A0/contour_A_'+str(Daughterparticle)+'.pdf') #2]


def PlottingTanBr(tanB, r, tanB2, r2, XERR, saveTitle):
    fig = pyplot.figure()
    pyplot.plot(tanB, r, color='green', marker='o', markersize=8, linestyle='dashed', linewidth=1)
    pyplot.plot(tanB2, r2, color='orange', marker='o', markersize=8, linestyle='dashed', linewidth=1)
    pyplot.errorbar(tanB2, r2, yerr=None, xerr=XERR, fmt='', ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, hold=None, data=None, **kwargs)
    #pyplot.setp(lines, color='r', linewidth=2.0)
    pyplot.rc('text', usetex=True)
    #pyplot.rf('font', family='serif')
    pyplot.xlabel(r'$\tan{\beta}$')
    pyplot.ylabel(r'r = $\frac{signal}{95\%CL \ limit\ on\ signal}$')
    pyplot.title(r'r in dependence of $\tan{\beta}$ with heavy Higgs, M$_{A0}$=352GeV')
    pyplot.savefig('Plots_CheckMATE/'+str(saveTitle)+'.pdf')
    

def PlottingTanBr2_includingHiggs(tanB, r, saveTitle):
    fig, ax = pyplot.subplots()
    pyplot.plot(tanB, r, color='blue', marker='o', markersize=7, linestyle='dashed', linewidth=1)
    yerr2 = r*87/1000
    ax.errorbar(tanB, r, yerr=yerr2, color='blue', barsabove='False', linestyle='none', linewidth=0.7) 
    pyplot.rc('text', usetex=True)
    pyplot.xlabel(r'$\tan{\beta}$')
    pyplot.ylabel(r'r = $\frac{signal}{95\%CL \ limit\ on\ signal}$')
    pyplot.title(r'r in dependence of $\tan{\beta}$, with heavy Higgs')#, M$_{A0}$=352GeV')
    pyplot.savefig('Plots_CheckMATE/'+str(saveTitle)+'.pdf')


def PlottingTanBr3_noHiggs(tanB, r, saveTitle):
    fig, ax = pyplot.subplots()
    pyplot.plot(tanB, r, color='blue', marker='o', markersize=7, linestyle='dashed', linewidth=1)
    yerr2 = r*87/1000
    ax.errorbar(tanB, r, yerr=yerr2, color='blue', barsabove='False', linestyle='none', linewidth=0.7)
    pyplot.rc('text', usetex=True)
    pyplot.xlabel(r'$\tan{\beta}$')
    pyplot.ylabel(r'r = $\frac{signal}{95\%CL \ limit\ on\ signal}$')
    pyplot.title(r'r in dependence of $\tan{\beta}$, no Higgs')#, M$_{A0}$=352GeV')
    pyplot.savefig('Plots_CheckMATE/'+str(saveTitle)+'.pdf')


    

#### 5. write a combined function, over which then can be looped in plot.py
def getBRSF(a0, tanb, indize, fstate, HiggsBlockNummer):
    writeInputSLHASusyhit(a0, tanb)
    DeleteEmptyLines = " sed '/^$/d' -i {}".format(susyhit_folder +'suspect2_lha.in')
    os.system(DeleteEmptyLines)
    runSusyhit()
    runFeynhiggsAfterSusyhit(indize)
    br = readoutBR(indize, fstate, HiggsBlockNummer)
    return br
