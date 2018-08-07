##### functions ##################################
##### define the functions here that are needed to run and vary the parameters in combination with feynhiggs


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
def plotting_withLegendInLines(Array1, Array2, Array3, Motherparticle, Daughterparticle1, Daughterparticle2):
    fig = pyplot.figure()
    CS = pyplot.contour(Array1, Array2, Array3)
    pyplot.xlabel(r'$m_{A^0}$ (GeV)')
    pyplot.ylabel(r'$tan{\beta} (degree)$')
    pyplot.title(r'Contour Plot of Branching Ratios('+str(Motherparticle)+'->'+str(Daughterparticle1)+' '+str(Daughterparticle2)+')')
    #add legend of contour levels
    pyplot.clabel(CS, inline=1, fontsize=10)
    pyplot.savefig("contour.pdf") #safe 

def plotting(Array1, Array2, Array3, Motherparticle, Daughterparticle):
    fig = pyplot.figure()
    #im = pyplot.imshow(Array3, interpolation='bilinear', origin='lower', cmap=cm.gray, extent=(-3,3,-2,2))
    #levels = np.arange(0, 1, 0.2)
    CS = pyplot.contour(Array1, Array2, Array3)
    CB = pyplot.colorbar(CS, shrink=0.8, extend='both')
    pyplot.xlabel(r'$m_{A^0}$ (GeV)')
    pyplot.ylabel(r'$tan{\beta}$')
    pyplot.title(r'Contour plot of BRs('+str(Motherparticle)+r' $\rightarrow$ '+str(Daughterparticle)+')')
    #add legend of contour levels
    #pyplot.clabel(CS, inline=1, fontsize=10)
    pyplot.savefig("Plots_BR_H/contour_H_"+str(Daughterparticle)+".pdf") #safe

    
#### 5. write a combined function, over which then can be looped in plot.py
def getBR(x,y,counter, fstate, HiggsNumber):
    writeInputFH({'MA0':x, 'TB':y}, 'InputFeynHiggsH/mhmodp_'+str(counter)+'.in')
    runfeynh('InputFeynHiggsH/mhmodp_'+str(counter)+'.in')
    br = readoutBR(counter, fstate, HiggsNumber)
    return br
