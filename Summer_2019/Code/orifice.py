```python
import math as m
from aguaclara.play import*
from scipy.constants import g as g # standard acceleration due to gravity
from scipy.constants import pi as pi

g = g * u.m/u.s**2
Pi_vc = 0.62 # Pi vena contracta
diam_orif = 0.00595313*u.m
A_orif = (pi*(diam_orif/2)**2)
h = 0.155 * u.m
Q = Pi_vc*A_orif*(2*g*h)**0.5
print(Q)
```
