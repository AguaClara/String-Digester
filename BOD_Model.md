```python
from aide_design.play import*
```
## A BOD kinetics model for a trickling Filter and how to improve
The modified Velz Equation from Logan et. al. 1987:

$C_{out} =\frac{C_{in}}{(R+1)e^{\frac{k_{20}A_{s}H\theta^{T-20}}{Q_{i}(R+1)^{n}}}- R}$

Where:
* $C_{out}=$ The $BOD_{5}$ leaving the filter
* $C_{in}=$ The $BOD_{5}$ entering the filter
* $R=$  The recycle ratio defined as the ratio of recirculation flow to the plant influent flow, a
* $k_{20}=$ The kinetic constant/treatability coefficient
* $A_{s}=$ The specific surface area
* $H=$ The filter height
* $\theta=$ an empirical correction factor typically set equal to 1.035
* $T=$ Temperature in degrees C
* $Q_{i}=$ The flow before recycle divided by filter cross sectional area

The team's preliminary design for the filter would not include any recycle, therefore the equation simplifies to:

$C_{out} ={C_{in}}{e^{\frac{-k_{20}A_{s}H\theta^{T-20}}{Q_{i}^{n}}}}$

The main points of improvement based on the kinetic model would be to increase the height/depth of the filter, increase the surface area, increase temperature, lower the flow rate, or increase the $k_{20}$ value. Since these would not be put in a temperature controlled area, temperature is not an area we can improve. 

### Increasing Height/Depth of filter
This is an area that could improve the performance of the trickling filter. The team is looking for a novel design that can make traditional filters more cost-effective. The team does not believe that there is a lot of room for improvement in just changing the height of the filter.

### Increasing the specific surface area
