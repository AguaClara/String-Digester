Data from: http://www.wastewater.com/docs/default-source/corporate/aeration-efficiency-guide.pdf?sfvrsn=4
```python
from aide_design.play import*
activated_sludge_energy = 3954 *u.kW *u.hour
volume = 1000000 * u.gallon
Temp = 20 * u.degC
mass = pc.density_water(Temp) * volume
string_height = 40 * u.ft
pump_efficiency_low = 0.50
string_energy = string_height * pc.gravity * mass / pump_efficiency_low
percent = abs(string_energy - activated_sludge_energy) / activated_sludge_energy * 100
print(percent.to(u.dimensionless))
```
The proposed string design uses 93.65% less energy than an activated sludge tank. 
