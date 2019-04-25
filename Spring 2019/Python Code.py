import matplotlib.pyplot as plt
import pandas as pd
x = pd.read_csv('CFRT_FR_vs_VWC.csv', index_col = 0)
y = pd.read_csv('CFRT_FR_vs_VWC.csv', index_col = 1)
plt.plot(x,y, 'ro')
plt.title('Volume of Water on Chain at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Chain (mL)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsVWC')
