# ---------- Parameter Definition Script ------------------------
#   1. Define parameters and feed to FeynHiggs + SUSY-HIT
#   2. Extract SLHAs and feed to formatSLHA
# --------------------------------------------------------------
import tools
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# -- Set Run Number --
run = 1

# -- Define parameter set --
params = []; counter = 0
paramsOut = [];
tbs = []
m1s = []
brs = []

sqrtNumPoints = 10;
# loop over many params
for i in range (0, sqrtNumPoints):
    tbsRow = []; m1sRow = []; brsRow = []
    for j in range(0, sqrtNumPoints):
        counter += 1
        tb = 20 + i*5#tanBeta
        ma = 600 + j*5#MA0
        tbsRow.append(tb)
        m1sRow.append(ma)
        # Use name of files per FeynHiggs convention
        runVals = {'TB' : tb,
                   'MA0' : ma}

        #br = tools.run(params, runVals, run, counter, ['A0->neutralino1neutralino1'])
        br = tools.run(params, runVals, run, counter, ['A0->chargino1chargino1'])
        brsRow.append(br[0])
    tbs.append(tbsRow)
    m1s.append(m1sRow)
    brs.append(brsRow)
    print counter

tbs = np.array(tbs)
m1s = np.array(m1s)
brs = np.array(brs)

print tbs
print m1s
print brs
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.contour(m1s, tbs, brs)
plt.xlabel(r'$m_{A^0}$ (GeV)')
plt.ylabel(r'$tan{\beta}$')
plt.title(r'\textbf{Branching Ratio Contour Plot}')
plt.savefig("contour.pdf")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(m1s, tbs, brs)
ax.set_xlabel(r'$m_{A^0}$ (GeV)')
ax.set_ylabel(r'$tan{\beta}$')
ax.set_zlabel(r'Branching Ratio')
ax.set_title(r'\textbf{Variation of BR')
fig.savefig("3d.pdf")
plt.show()
# fish = filter(lambda x : x % 2 == 0, range(0,10))
