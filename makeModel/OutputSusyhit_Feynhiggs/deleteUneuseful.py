import os
import numpy as np

for i in np.arange(782, 840, 1): 
    DeleteCommand = 'git checkout -- susyhit_slha.out.fh-001_'+str(i) 
    os.system(DeleteCommand)
