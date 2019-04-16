
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
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsVWC')
plt.show()



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
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsRT')
plt.show()



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
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/CFRvsHN')
plt.show()


from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('DFRT_FR_vs_VWS.csv',
                unpack = True,
                delimiter = ',')

plt.plot(x,y)
plt.title('Volume of Water on Dacron String at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Dacron String (mL)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsVWC')
plt.show()



from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('DFRT_FR_vs_RT.csv',
               unpack = True,
               delimiter = ',')

plt.plot(x,y)
plt.title('Residence Time of Water on Dacron String \nat Different Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Residence Time (s)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsRT')
plt.show()


from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x,y = np.loadtxt('DFRT_FR_vs_HN.csv',
               unpack = True,
               delimiter = ',')

plt.plot(x,y)
plt.title('Height of Dacron String Needed for a \n15 Minute Residence Time')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Height of Chain (m)')
plt.savefig('/Users/gvsso/OneDrive/Documents/Gaby/String-Digester/Spring 2019/images/DFRvsHN')
plt.show()
