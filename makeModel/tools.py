import pyslha as slha
import errno
import json
from collections import OrderedDict
import os
## ----------------- DEFINITIONS (Change at will) ----------------- ##
baseSLHAPath =  "models/mhmodp_MA500_TB10.slha" # "models/tauphobic_MA800_TB45.slha"

SLHABlocksMap = {'M1' : [['EXTPAR', 1], ['MSOFT', 1]],
                'M2' : [['EXTPAR', 2], ['MSOFT', 1]],
                'MUE' : [['EXTPAR', 23], ['HMIX', 1]],
                'MA0' : [['EXTPAR', 26], ['MASS', 36]],
                'tanb' : [['EXTPAR', 25], ['MINPAR', 3], ['HMIX', 2]],
                'Atau' : ['EXTPAR', 13]}
# BR Name -> pid, decay pids
# SLHADecaysMap = { 'A0->Tautau' : [36, '-15 15'],
#                  }
# SLHADecaysMap = { 'A0->neutralino1neutralino1' : [36, '1000022 1000022'],
#}
SLHADecaysMap = { 'A0->chargino1chargino1' : [36, '-1000024 1000024'],
                  }


debug = False
# FHparams= OrderedDict()
# FHparams = {'MT': 173.2, 'M3SQ': 1500, 'M3SU': 1500, 'M3SD': 1500,
#           'M3SL': 500, 'M3SE': 500, 'Abs(Xt)': 3675, 'M2SQ': 1500,
#           'M2SU': 1500, 'M2SD': 1500, 'M2SL': 500, 'M2SE': 500,
#           'M1SQ': 1500, 'M1SU': 1500, 'M1SD': 1500, 'M1SL': 500,
#           'M1SE': 500, 'Abs(Ac)': 0, 'Abs(As)': 0, 'Abs(Amu)': 0,
#           'Abs(M_3)': 1500, 'Abs(M_2)': 200, 'Abs(MUE)': 2000, 'TB': 20}
# soft-breaking right and left handed stau mass params ?
## ----------------------------------------------------------------- ##

def run(params, runVals, runNumber, counter, interested):
    # Create SLHA files
    dir = 'runs/run' + str(runNumber)
    dirIn = dir + '/in'
    params.append(runVals)
    FHPath, SHPath = manageDirectories(dir, counter)
    writeFH(runVals, FHPath)
    # slha.writeSLHAFile(FHPath, editBaseSLHA(runVals))
    with open(dirIn + '/debug/variedParameters.txt', 'w') as file:
        file.write(json.dumps(params))
        file.close()

    # Run the packages
    try:
        runPackages(FHPath, SHPath, dir, counter)
    except IOError:
        return []
        print "Model didn't work"
    # Extract FH params
    file = slha.readSLHAFile(dir + "/out/temp/fhOutput" + str(counter) + ".slha")
    paramsOut = []
    decaysUseful = convertDecays(file)
    for decayDef in interested:
        pid = SLHADecaysMap[decayDef][0]
        try:
            decayProd = SLHADecaysMap[decayDef][1]
            paramsOut.append(decaysUseful[pid][decayProd])
        except:
            print "%s branching ratio not found" %(decayDef)
        # if (len(vals) > 1) and (len(vals) == len(set(vals))): # ensure all vals same
        #     raise Exception("Non-identical parameter entries in FeynHiggs SLHA output")
    return paramsOut

def runPackages(FHPath, SHPath, dir, counter):
    feynhiggs(FHPath, dir, counter)
    # susyhit(FHPath, dir, counter)

def writeFH(varyParams, FHPath):
    # Change desired parameters
    FHParams = open("models/mhmodp.in", "r")
    params = OrderedDict()
    for line in FHParams:
        content = line.split()
        if not content[0] in varyParams:
            params[content[0]] = content[1]
        else:
            params[content[0]] = varyParams[content[0]]
    # Write out into input file
    f = open(FHPath, 'w')
    for key in params.keys():
        spaces = (13 - len(key)) * " "
        f.write(key + spaces + str(params[key]) + "\n")
    f.close()


# def runScan(paramNames, paramVals, baseFile):
#     params = convertInput(paramNames, paramVals)
#     for dict in params:
#         newSLHA = editBaseSLHA(dict, baseFile)
#         feynhiggs(newSLHA)
#         susyhit(dict, baseFile)
#         combineAndSave()

def convertDecays(file):
    decays = {}
    for pid in file.decays:
        particleDecays = {}
        for decay in file.decays[pid].decays:
            particleDecays[' '.join(map(str, decay.ids))] = decay.br
        if len(particleDecays) > 0 : decays[pid] = particleDecays
    return decays

def convertInput(paramNames, paramVals):
    paramList = []
    for i in range(0, len(paramVals)):
        dict = {}
        for j in range(0, len(paramNames)):
            dict[paramNames[j]] = paramVals[i][j]
        paramList.append(dict)
    return paramList

# Function takes in the base SLHA and a set of parameters to add / overwrite
def editBaseSLHA(params):
    base = slha.readSLHAFile(baseSLHAPath)
    # convert input to blocks via map
    for valPair in params.items():
        name = valPair[0]
        value = valPair[1]
        for blockInfo in SLHABlocksMap[name]:
            blockName = blockInfo[0]
            valID = blockInfo[1]
            # now edit block in the file
            try:
                base.blocks[blockName][valID] = str('{:.8e}'.format(value))
            except KeyError:
                newBlock = slha.Block(blockName)
                newBlock.add_entry[valID, str('{:.8e}'.format(value))]
                base.blocks[blockName] = newBlock
    return base


# -- TO RUN PROGRAMS --s
def feynhiggs(inputFile, dir, counter):
    # Running FeynHiggs in "Command line mode"
    fhPath = "/home/summerstudent/Programs/feynhiggs/"
    runPath = fhPath + "x86_64-Linux/bin/FeynHiggs " + inputFile + "#SLHA"
    if debug:
        cmd = runPath + " | grep -v %"
    else :
        cmd = runPath + " > /dev/null 2>&1"
    os.system(cmd)
    os.system("mv " + inputFile + ".fh-001 " + dir + "/out/temp/fhOutput" + str(counter) + ".slha")

def susyhit(SLHA, dir, counter):
    # Run Susyhit
    susyhitPath = "/usr/lib/susyhit/"
    os.system("cp " + SLHA + " " + susyhitPath + "suspect2_lha.in")
    os.system(susyhitPath + "run susyhit.in")
    os.system("cp " + susyhitPath + "susyhit_slha.out " + "out/temp/shOutput" + str(counter))



# -- TO PROCESS OUTPUT --
def combineAndSave():
    # Read in FeynHiggs file and fix the feynhiggs block
    fh = slha.read("tempf/fhOutput")
    fixFHBlock(fh, "2.9.5")
    fh = ParamSet.fromPYSLHA(fh)
    sh = ParamSet.fromSLHA("temp/shOutput")
    makeSushiBlock()

# Function to create new FeynHiggs block
# Takes a pyslha object and the feynhiggs version being used
def fixFHBlock(pyslhaObj, FHVersion):
    addBlock(pyslhaObj, ['SPINFO', pyslhaObj.blocks['SPINFO'][1], FHVersion], pyslhaObj.blocks['SPINFO'][2])

# Create Sushi Block - Higgsmode (0 = h, 1 = A, 2 = H)
def makeSushiBlock(pyslhaObj, higgsMode):
    higgsModeMap = {'h' : 0, 'A' : 1, 'H' : 2}
    higgsMode = higgsModeMap[higgsMode]
    mode = 1 # Set mode : model: 0 = SM, 1 = MSSM, 2 = 2HDM
    addBlock(pyslhaObj, ['SUSHI', mode, higgsMode])
    addBlock(pyslhaObj, ['RENORMBOT', 0, 2 ,1 , '4.75d0'])
    addBlock(pyslhaObj, ['RENORMSBOT', 2, 0, 0])
    addBlock(pyslhaObj, ['FACTORS', '0.d0', '1.d0', '1.d0', '1.d0', '1.d0'])
    print pyslhaObj
    slha.write('models/testout.slha', pyslhaObj)

def addBlock(pyslhaObj, blockList):
    block = slha.Block(blockList[0])
    for i in range(1, len(blockList)):
        block.add_entry([i, blockList[i]])
    pyslhaObj.blocks[blockList[0]] = block

def manageDirectories(dir, counter):
    FHPath = dir + '/in/FHinputs/valSet' + str(counter) + '.in'
    SHPath = dir + '/in/SHinputs/valSet' + str(counter) + '.slha'
    if not os.path.exists(dir):
        try:
            os.makedirs(dir + "/in/debug")
            os.makedirs(dir + "/in/FHinputs")
            os.makedirs(dir + "/in/SHinputs")
            os.makedirs(dir + "/out/temp")
            os.makedirs(dir + "/out/models")
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return FHPath, SHPath


class ParamSet:
    def __init__(self):
        self.params = {}

    @classmethod
    def fromSLHA(cls, file):
        return cls.fromPYSLHA(slha.readSLHAFile(file))

    @classmethod
    def fromPYSLHA(cls, pyslhaObj):
        self = ParamSet()
        d = pyslhaObj
        for blockName in d.blocks.keys():
            for value in d.blocks[blockName].keys():
                self.params[blockName, value] = d.blocks[blockName][value]
        return self

    def addParam(self, key, val):
        self.params[key] = val

    def printParams(self):
        for key in self.params.items():
            print key, self.params.get(key)
    def writeSLHA(self):
        print 1;











