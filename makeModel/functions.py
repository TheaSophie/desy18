##### functions ##################################
##### define the functions here that are needed to run and vary the parameters in combination with feynhiggs


####import all packages
import os
import pyslha
import matplotlib.pyplot as pyplot
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from collections import OrderedDict

####4. und 5. sind von Intersse! :)


####1. let feynhiggs run in the command line mode with the input file,
def runfeynh(input):
    runCommand = "/home/summerstudent/Programs/feynhiggs/x86_64-Linux/bin/FeynHiggs " + input + "#SLHA"
    os.system(runCommand)
#runfeynh('models/mhmodp.in')
#runfeynh('InputFeynHiggs/mhmodp_'+str(900)+'.in')


####2. vary the import parameter (for now it's not an SLHA File)
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
#writeInputFH({'MA0':600, 'TB':25}, "InputFeynHiggs/mhmodp_"+str(x)+".in")


####3. reading out the branching ratio of the created FeynHiggs SLHA file
def readoutBR(count):
    Array3 = []
    SLHAfile = pyslha.readSLHAFile("InputFeynHiggs/mhmodp_"+str(count)+".in.fh-001")
    particleBlock = 36
    for decay in SLHAfile.decays[particleBlock].decays:
        if decay.ids == [1000022, 1000022]: #decay to neutralino1, neutralino1
            #Array3.append([particleBlock, decay.br])
            Array3.append(decay.br)
            #BR = decay.br
            print Array3
            #print BR
    return Array3
    #return BR
    #print BR
#readoutBR(900)


####4. Plotting the output data in a nice contour plot
def plotting(Array1, Array2, Array3):
    fig = pyplot.figure()
    pyplot.contour(Array1, Array2, Array3)
    pyplot.xlabel(r'$m_{A^0}$ (GeV)')
    pyplot.ylabel(r'$tan{\beta}$')
    pyplot.title(r'\textbf{Contour Plot of Branching Ratios for A0 \rightarrow \}')
    #add legend of contour levels
    pyplot.savefig("contour.pdf") #safe 


####5. write a combined function, over which then can be looped in plot.py                                                                                   
def getBR(x,y,count):
    writeInputFH({'MA0':x, 'TB':y}, 'InputFeynHiggs/mhmodp_'+str(count)+'.in')
    runfeynh('InputFeynHiggs/mhmodp_'+str(count)+'.in')
    readoutBR(count)
getBR(600,45,1)
