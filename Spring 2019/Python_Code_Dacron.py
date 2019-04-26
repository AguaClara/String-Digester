import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

FR, VWS = np.loadtxt('DFRT_FR_vs_VWS.csv', unpack=True, delimiter=',')
# FR = flow rate
# VWS = volume of water on the string
length = .78  # length of the string(can be changed)
optimalrestime = 900  # optimal residence time in seconds(can be changed)

plt.figure(0)
plt.plot(FR, VWS, 'ro')
plt.title('Volume of Water on Dacron String at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Dacron String (mL)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsVWC')

RT = [0]*len(FR)
for i in range(len(FR)):
    RT[i] = VWS[i]/FR[i]  # RT residence time

plt.figure(1)
plt.plot(FR, RT, 'ro')
plt.title('Residence Time of Water on Dacron String \nat Different Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Residence Time (s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsRT')

secperm = [0]*len(RT)
HN = [0]*len(RT)
for i in range(len(RT)):
    secperm[i] = RT[i]/length
    HN[i] = optimalrestime/secperm[i]

plt.figure(2)
plt.plot(FR, HN, 'ro')
plt.title('Height of Dacron String Needed for a \n15 Minute Residence Time')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Height of Chain (m)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsHN')
