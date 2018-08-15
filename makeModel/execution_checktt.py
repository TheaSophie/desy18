import os
import numpy as np
import pyslha as slha

count = -1
br = []
ma = []
tanb = []
directory = "temp_output"
filenames = os.listdir(directory)
filenames = sorted(filenames)

for filename in filenames:
   print filename
   count += 1
   if count == 600: break;
   file = os.path.join(directory, filename)
   slhaData = slha.readSLHAFile(file)
   tanb.append(slhaData.blocks['EXTPAR'][25])
   ma.append(slhaData.blocks['MASS'][36])
   for decay in slhaData.decays[36].decays:
        if decay.ids == [-6, 6]:#fstate = [1000022, 1000022] decay to neutralino1, neutralino1
           br.append(decay.br)
           print "decays not present"
   print decay.br
   if (count > 300): exit(0)
# rowSize = np.sqrt(len(tanb)).astype(int)
tanb = np.array(tanb).reshape((25, 24))
ma = np.array(ma).reshape((25, 24))
br = np.array(br).reshape((25, 24))


