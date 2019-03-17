```python
from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('CFRT_FR_vs_VWC.csv',
                unpack = True,
                delimiter = ',')

plt.plot(x,y)
plt.title('Volume of Water on Chain at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Chain (mL)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/FRvsVWC')
plt.show()
```


```python
from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('CFRT_FR_vs_RT.csv',
               unpack = True,
               delimiter = ',')

plt.plot(x,y)
plt.title('Residence Time of Water on Chain \nat Different Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Residence Time (s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/FRvsRT')
plt.show()
```


```python
from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('CFRT_FR_vs_HN.csv',
               unpack = True,
               delimiter = ',')

plt.plot(x,y)
plt.title('Height of Chain Needed for a \n15 Minute Residence Time')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Height of Chain (m)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/FRvsHN')
plt.show()
```
