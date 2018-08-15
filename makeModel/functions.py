#! /bin/bash

##### functions ##################################
##### define the functions here that are needed to run and vary the parameters in combination with feynhiggs


#### import all packages
import os
import pyslha
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict

#### 4. und 5. sind von Intersse! :)


#### 1. let feynhiggs run in the command line mode with the input file,
def runfeynh(input):
    runCommand = "/home/summerstudent/Programs/feynhiggs/x86_64-Linux/bin/FeynHiggs " + input + "#SLHA > /dev/null 2>&1"
    os.system(runCommand)


#### 2. vary the import parameter (for now it's not an SLHA File)
def writeInputFH(varyParams, newfilePath):
    InputParameters = open("models/mhmodp.in", "r")
    params = OrderedDict()
    for line in InputParameters:
        content = line.split() #splits due to the space: 0 1, further: 0 = 1
        if not content[0] in varyParams:
            params[content[0]] = content[1]
        else:
            params[content[0]] = varyParams[content[0]]
    # Write new/changed input file
    newfile = open(newfilePath, 'w')#create new file
    for key in params.keys():
        spaces = (13 - len(key)) * " "
        newfile.write(key + spaces + str(params[key]) + "\n")
    newfile.close()


#### 3. reading out the branching ratio of the created FeynHiggs SLHA file
def readoutBR(counter, fstate, HiggsNumber):
    branchr = 0
    SLHAfile = pyslha.readSLHAFile("InputFeynHiggs/mhmodp_"+str(counter)+".in.fh-001")
    particleBlock = HiggsNumber
    for decay in SLHAfile.decays[particleBlock].decays:
        #if decay.ids == [1000022, 1000022]: #decay to neutralino1, neutralino1
        if decay.ids == fstate:
            branchr = decay.br
    return branchr


#### 4. Plotting the output data in a nice contour plot
#write dictionary for title LATEX for duaghterparticles
LatexDaughterparticle = {'charg1charg1':'$\chi^{-}_{1}\chi^{+}_{1}$', 'charg1charg2':'$\chi^{-}_{1}\chi^{+}_{2}$', 'charg2charg1':'$\chi^{-}_{2}\chi^{+}_{1}$', 'charg2charg2':'$\chi^{-}_{2}\chi^{+}_{2}$', 'neutr1neutr1':'$\chi^{0}_{1}\chi^{0}_{1}$', 'neutr1neutr2':'$\chi^{0}_{1}\chi^{0}_{2}$', 'neutr1neutr3':'$\chi^{0}_{1}\chi^{0}_{3}$', 'neutr1neutr4':'$\chi^{0}_{1}\chi^{0}_{4}$', 'neutr2neutr2':'$\chi^{0}_{2}\chi^{0}_{2}$', 'neutr2neutr3':'$\chi^{0}_{2}\chi^{0}_{3}$', 'neutr2neutr4':'$\chi^{0}_{2}\chi^{0}_{4}$', 'neutr3neutr3':'$\chi^{0}_{3}\chi^{0}_{3}$', 'neutr3neutr4':'$\chi^{0}_{3}\chi^{0}_{4}$', 'neutr4neutr4':'$\chi^{0}_{4}\chi^{0}_{4}$'}

def plotting(Array1, Array2, Array3, Motherparticle, Daughterparticle):
    fig = pyplot.figure()
    #im = pyplot.imshow(Array3, interpolation='bilinear', origin='lower', cmap=cm.gray, extent=(-3,3,-2,2))
    v = np.arange(0.00, 1.00, 0.02)
    CT = pyplot.contourf(Array1, Array2, Array3, v)
    CB = pyplot.colorbar(CT, shrink=0.8, extend='both')
    CS = pyplot.contour(Array1, Array2, Array3, 6, colors='k')
    pyplot.rc('text', usetex=True)
    pyplot.rc('font', family='serif')
    #pyplot.xlabel(r'm$_{H}$ (GeV)')
    pyplot.xlabel(r'm$_{A}$ (GeV)')
    pyplot.ylabel(r'$tan{\beta}$')
    Decayparticles = LatexDaughterparticle[str(Daughterparticle)]
    pyplot.title(r'Branching Ratios('+str(Motherparticle)+r' $\rightarrow$ '+str(Decayparticles)+')')
    #add legend of contour level
    pyplot.clabel(CS, inline=1, fontsize=8)
    #pyplot.savefig("Plots_Feynhiggs/Plots_BR_H/contour_H_"+str(Daughterparticle)+".pdf") #safe
    pyplot.savefig('Plots_Feynhiggs/Plots_BR_A0/contour_A_'+str(Daughterparticle)+'.pdf')
    
    
#### 5. write a combined function, over which then can be looped in plot.py
def getBR(x,y,counter, fstate, HiggsNumber):
    writeInputFH({'MA0':x, 'TB':y}, 'InputFeynHiggsH/mhmodp_'+str(counter)+'.in')
    runfeynh('InputFeynHiggsH/mhmodp_'+str(counter)+'.in')
    br = readoutBR(counter, fstate, HiggsNumber)
    return br
