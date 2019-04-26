import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

FR,VWC = np.loadtxt('CFRT_FR_vs_VWC.csv',
                unpack = True,
                delimiter = ',')
#FR = flow rate
#VWC = volume of water on the chain
length = .9144 # length of the chain(can be changed)
optimalrestime = 900 # optimal residence time in seconds(can be changed)

plt.figure(0)
plt.plot(FR,VWC, 'ro')
plt.title('Volume of Water on Chain at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Chain (mL)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsVWC')

RT = [0]*len(FR)
for i in range(len(FR)):
    RT[i] = VWC[i]/FR[i] #RT residence time

plt.figure(1)
plt.plot(FR,RT, 'ro')
plt.title('Residence Time of Water on Chain \nat Different Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Residence Time (s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsRT')

secperm = [0]*len(RT)
HN = [0]*len(RT)
for i in range(len(RT)):
    secperm[i] = RT[i]/length
    HN[i] = optimalrestime/secperm[i]

plt.figure(2)
plt.plot(FR,HN, 'ro')
plt.title('Height of Chain Needed for a \n15 Minute Residence Time')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Height of Chain (m)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsHN')
