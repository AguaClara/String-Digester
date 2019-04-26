import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

WT, TIME = np.loadtxt('DGST_WT_vs_TIME.csv', unpack=True, delimiter=',')
# WT = Weight of water in cup catching water dripping off strings
# TIME = time for weight of water to drip into cup in minutes

AWT = [0]*len(WT)
for i in range(len(WT)):
    AWT[i] = WT[i]-WT[0]  # AWT adjusted weight

FR = [0]*(len(WT)-1)  # one index shorter because there is no flow rate at time zero because divide by zero
for i in range(len(WT)-1):
    FR[i] = (AWT[i+1]-AWT[i])/(TIME[i+1]-TIME[i])
FR.insert(0, 0)

plt.figure(0)
plt.plot(TIME, WT, 'ro')
plt.title('Weight of Water Collected at \nDifferent Times')
plt.xlabel('Time (min)')
plt.ylabel('Weight of Water Collected (g)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/TIMEvsWT')
plt.show()

plt.figure(1)
plt.plot(TIME, FR, 'ro')
plt.title('Flow Rate Down the Strings at \nDifferent Times')
plt.xlabel('Time (min)')
plt.ylabel('Flow Rate (mL/min)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/TIMEvsFR')
plt.show()
