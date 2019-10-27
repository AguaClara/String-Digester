import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

NS, HW, HWTP, HTDS, AWC, TIME, TFR, FRPS, FRPSuL = np.loadtxt('CAP_ACT_FR_TESTS.csv',
                unpack = True,
                delimiter = ',')
#NS = Number of Strings
#HW = Height of Water
#HWTP = Height Water Travels to Peak
#HTDS = How far the water has to travel down the string
#AWC = Amount of Water Collected
#TIME = measured amount of time once water started being collected
#TFR = total flow rate
#FRPS = flow rate per string in mL/s
#FRPSuL = flow rate per string uL/s

plt.figure(0)
plt.plot(NS,TFR, 'ro')
plt.title('Total Flow Rate for \nDifferent Number of Strings')
plt.xlabel('Number of Strings')
plt.ylabel('Total Flow Rate (mL/s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Fall 2019/images/NSvsTFR')
