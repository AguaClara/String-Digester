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


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

NS, HW, HWTP, HTDS, AWC, TIME, TFR, FRPS, FRPSuL = np.loadtxt('https://github.com/AguaClara/String-Digester/blob/master/Fall%2019/CAP_ACT_FR_TESTS.csv', unpack = True, delimiter = ',')
#NS = Number of Strings
#HW = Height of Water
#HWTP = Height Water Travels to Peak
#HTDS = How far the water has to travel down the string
#AWC = Amount of Water Collected
#TIME = measured amount of time once water started being collected
#TFR = total flow rate
#FRPS = flow rate per string in mL/s
#FRPSuL = flow rate per string uL/s

#plt.figure(0)
#plt.plot(NS,TFR, 'ro')
#plt.title('Total Flow Rate for \nDifferent Number of Strings')
#plt.xlabel('Number of Strings')
#plt.ylabel('Total Flow Rate (mL/s)')
#plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Fall 2019/images/NSvsTFR')


#df = pd.read_csv('https://github.com/AguaClara/String-Digester/blob/master/Fall%2019/CAP_ACT_FR_TESTS.csv')
#NS = df.iloc[:, 0] # Number of Strings
#HW = df.iloc[:, 1] # Height of Water
#HWTP = df.iloc[:, 2] # Height Water Travels to Peak
#HTDS = df.iloc[:, 3] # How far the water has to travel down the string
#AWC = df.iloc[:, 4] # Amount of Water Collected
#TIME = df.iloc[:, 5] #measured amount of time once water started being collected
#TFR = df.iloc[:, 6] #total flow rate
#FRPS = df.iloc[:, 7] #flow rate per string in mL/s
#FRPSuL = df.iloc[:, 8] #flow rate per string uL/s

plt.figure(0)
plt.plot(NS,TFR)
plt.title('Total Flow Rate for \nDifferent Number of Strings')
plt.xlabel('Number of Strings')
plt.ylabel('Total Flow Rate (mL/s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Fall 19/images/NSvsTFR')
plt.show()
