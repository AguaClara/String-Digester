# Jet Flow Rate

**Goal:** Determine the flow rate, orifice size, and water height that will produce the best jet spray. Ideally the jet spray would cover a wide surface area evenly with small water droplets. Also determine the best material for deflecting the water to produce a jet stream.

**Observations:** We started out by testing various materials found around the lab by placing them under running water from the sink. These included a PVC pipe cut in half (producing a semi-cylinder), thick pieces of PVC sheets, wide pieces of PVC sheets, and bottles (to test a cylinder shape). However, the material that deflected water the best and produced the best jet stream were thin, flat, and narrow pieces of PVC sheets.

The best jet flow observed came from a narrow stream of water traveling at a high speed.

## Experiment 1

June 12, 2019

**Goal:** Determine if the orifice size and water heights theoretically calculated from the orifice equation produce the theoretical flow rate a good jet stream.

**Theoretical Calculation:** A 5 mm diameter orifice, with a water height of 15 cm, and a flow rate of 10 microliters/s per string would produce enough water for 2087 strings.

### Fabricate an apparatus

**Materials:**
- Clear PVC tube inner diameter 4.5 cm, about 20 cm in length
- Flat sheet of PVC (8 x 6.5 cm)
- 7/32" drill bit
- PVC cement and primer
- 100 mL graduated cylinder

**Fabrication:**
- Drill a hole in the middle of the PVC sheet about 5.5 mm in diameter using the 7/32" drill bit
- Glue the PVC tube onto the PVC sheet such that the hole is centered in the middle
- Draw a line on the PVC tube at a height of 15 cm from the PVC sheet base

### Procedure 1
- Plug the hole with a finger while filling it with water to a height of 15 cm
- Place the apparatus over a 100 mL graduated cylinder
- Unplug the hole and start a timer. Simultaneously pour more water into apparatus so the water height remains constant at 15 cm.
- When the water level gets close to the top of the graduated cylinder, plug the hole, stop the timer, and stop pouring more water in.
- Calculate the flow rate by dividing the volume of water in the graduated cylinder by the time of the trial. Compare this value to what was expected.

### Procedure 2
- Plug the hole with a finger while filling it with water to a height of 15 cm
- Hold the apparatus over a thin sheet of PVC
- unplug the hole and observe the quality of jet flow. Simultaneously add more water to maintain a water height of 15 cm

### Results 1
**Hole Size:** about 5 mm 7/32" diameter **Edit:** (06/18/2019) = 5.55625 mm

**Trial 1**
- It took about 5 seconds for approximately 80 mL to drain from the container = 16 mL/s = 16000 microL/s =  water for 1,600 strings
If the strings are 5 mm apart, arranged in a square, the square would have a side length of 200 mm = 20 cm
- Note: for this first trial the timing between when we stopped the timer and re-plugged the hole was a little off. Therefore this is not a very reliable measurement

**Trial 2**
It took about 3 seconds for 90 mL to drain from the container = 30 mL/s. This is about twice the flow rate for trial 1, meaning that it could supply water for approximately 3200 strings

### Results 2
- We observed that this set-up did not produce a good jet spray. The water spray was very concentrated and uneven. It did not travel far at all. We hypothesized that this poor flow was due to a low water velocity coming from the pipe.  

### Conclusions
In order to draw a conclusion about the flow rate from this system we would need to perform many more trials and average them together. However, we did not pursue this calculation as we also found that this setup did not produce a good jet spray.

**Questions:** How can we produce a faster water velocity from our apparatus?

We attempted to do this by using a smaller hole size and the same flow rate, etc.
We sealed the original hole with tape and drilled a smaller one next to it and repeated the experiment

Hole Size: 3/32" diameter about 2.35 mm diameter
Trial 1: 90 mL in 14.6 seconds = 6.16 mL/s

**Results:** This set-up produced an even weaker flow that the original design.

**Edit:** (7/2/19) This was not a valid attempt at increasing the velocity. The velocity cannot be increased just by decreasing the orifice size, because the flow rate is also dependent to the orifice size. Using only gravity, it is not possible to maintain the flow rate in this way without an additional source of pressure. Instead the velocity of water could be increased by increasing the distance between the orifice and the deflector plate. 

## Experiment 2

**Goal:** Experimentally determine the orifice area and the flow rate that produces a strong and even jet spray

**Methods:**
- Obtain a thin piece of PVC sheet and hold it under the faucet
- Adjust the strength of the faucet until a jet spray forms that is wide, flat, and even.
- Using this same faucet setting, time how long it takes to fill 3 Liters of water. Repeat for a total of 3 trials and average the results

**Results:**
- Times: 26.53, 26.05, and 25.03 seconds
- Average time = 25.87 seconds
- Average flow rate = 0.115964 L/s = 0.000115964 m^3/s = 115964 microL/s = 11,596.4 strings
If strings are 5mm apart in a square, square length is = 538 mm long = 53.8 cm long

**See pictures comparing the dimension of the string matrix to the area that the jet can spray**

## Experiment 3.1

**Goal:** Determine if the spray pattern generated by the faucet, can be replicated by water flow due to gravity

### Trial 1
What is the height needed to give the same flow as the faucet?
N = 11596; %strings
Q = 0.000115964; %m^3/s
diam_orif = 0.005; %m
A_orif = pi*(diam_orif/2)^2;
h = ((Q/(Pi_vc*A_orif))^2)/(2*g)
**h = 4.63 m**

but with diam_orif = 0.01 m, **h = 0.2894 m**

**Methods:** Drill a new hole next to the 5mm one using the 3/8" drill bit which is ~ 9.43 mm in diameter

**Observations:** the spray produced was similar to that produced by the faucet in Experiment 2, however water droplets were slightly less even in size and distribution. Additionally the water spray reached a small area.  Even so the flow rate could be scaled down a little bit.

**Edit:** the drill bit below was not actually 1 cm, really 9.525 mm if you convert 3/8 inches to mm, gives you a height of 35.15 cm Perhaps this is why the flow didn't look quite as nice as we thought that it would. Conclusion, we need to be more careful about using the exact size of the orifice in our calculations.

**We don't have a video for this trial at this point in time. DO we need one?**

## Experiment 3.2
The subteam wanted to see if a reasonable spray pattern could be produced with a lower flow rate.

### Trial 1:
June 17, 2019
17/64" drill bit approximately 6.72 mm in diameter
N = 11596/2; % **5798 strings = square with side length 38.1 cm**
Q = 0.000115964/2; %m^3/s
diam_orif = 0.00672; %m
A_orif = pi*(diam_orif/2)^2;
h = ((Q/(Pi_vc*A_orif))^2)/(2*g)
**h = 0.3547**

this setup produced a spray which was 30 cm long with an influent velocity of Q/A_orif = 1.6348 m/s.

**see video on google drive. note both images screenshotted at 35.47 cm**

**Edit:** (06/18/2019) based on the picture for this trial it seems like the length of the water spray was closer to 20 cm rather than 30 cm. Either way, the spray doesn't quite reach large enough to cover a square with sides 38.1 cm.

**Edit:** (06/18/2019) with a correction to 6.75 mm diameter, we should have used a height of 34.85 in our experiment

**Conclusion:** The spray pattern was relatively even, however, the flow rate was a lot higher than we would have liked and the water droplets were very large. Will decreasing the flow rate fix the problem while being strong enough to create a good spray?

**Note:** there were no drill bits in the lab between the 3/8" (~1 cm) and 7/32" (~5 mm) besides the 17/64" (6.72 mm) drill bit. Another possibility is to ask in the machine shop. Otherwise the only variables left to vary are the flow rate and water height


### Trial 2
June 18, 2019
We decreased the flow rate even further as we repeated Trial 1
N = 11596/3 % **3865 strings = square with side length 31.08 cm**
Q = 0.000115964/3 %m^3/s = **0.038655 L/s**
diam_orif = 0.00672; %m
A_orif = pi*(diam_orif/2)^2;
h = ((Q/(Pi_vc*A_orif))^2)/(2*g)
velocity = Q/A_orif %m/s
**h = 0.1577 m**
**velocity  = 1.0899 m/s**

**Observations:**
- water droplets are visibly uneven in size: bigger in the middle, smaller towards the edges
- width: 35 - 50 cm = 15 cm long

**Conclusion:** This flow rate is too low to use. Even if the spray pattern was even it would not reach the ends of a 31 cm square
**Note:** picture is screenshotted at 15.77 cm

### Trail 3
- use a flow rate in between that of trial 1 and 2 by changing the water height **filled the apparatus well beyond the 35 cm mark and watched the spray as it drained. There was no water height below the 35 cm mark that really produce a good spray**
**What we can try to get a better spray?**

### Trial 4
- retry the small 5 mm diameter orifice with different heights

**Note:** in the video, the word 'now' is spoken at a water height of 35 cm. both pictures are screenshotted at this height

**Observations:** It seemed like over 35 cm produced an okay spray. Droplets were about the same size as before, maybe slightly smaller.
For a diameter of 5.55625 mm (the "5 mm" hole) and a height of 35 cm, the flow rate would be **0.039374 L/s.** This would require 3937 strings, arranged in a square of side length of 31.3 cm. The length covered by the spray was about 30-31 cm.

### Trial 5
- find a drill bit in between the 1 cm and the 6.75 mm and experiment with a different hole size
- also varied the distance between the orifice and the deflector plate (11 cm vs. 25 cm). You can get really tiny but sprits of water if you hold it higher up using low flow rates. At 11 cm and at a water height <= 15.5 cm there appear to be two different splashing regimes: really tiny droplets that shoot up and out, and larger droplets towards the bottom that don't travel as far

 15/64" = 0.00595313 m  diameter

 At a water height of 15.5 cm the flow rate was theoretically calculated to be 3.0079e-05 m^3/s = **0.030079 L/s** which corresponds to **3008 strings**, square of side length **27.4 cm** By looking at the video, the splash only reached about 20 cm

**Note:** Video 1: distance between the orifice and the deflector is about 11 cm. for Video 2, this distance is about 25 cm. The words "last one" were spoken at a water height of 15.5 cm. The picture is screenshotted from video 2 at this height.

## Experiment 3.3

**Goal:** Determine the ideal distance between the orifice and the deflecting plate to produce the best spray.

**Motivation:** We found the minimum flow to produce a good spray to be approximately 0.035 +_ 0.005 L/s. However, we hypothesize that water traveling at a higher velocity produces a better spray. Therefore, we could hypothetically achieve the same quality of spray at a lower flow rate.

**Methods:** 15/64" = 0.00595313 m  diameter


Distance = distance between orifice and deflector plate in cm

 - minimum height of water necessary to produce spray at different distances

**Results:**

 Madeline
|Distance [cm]|Water Height [cm]| Flow Rate [L/s] | Spray Width [cm]|Time in Video [s]|
|:---:|:---:|:---:|:---:|:---:|
|10|9|0.02293|7|10|
|20|6|0.01872|8|18|
|30|4|0.01529|9|20|
|40|2|0.01081|9|23|
|50|1|0.007643|10|24|


Emily
|Distance [cm]|Water Height [cm]|Flow Rate [L/s] |Spray Width [cm]|Time in Video [s]|
|:---:|:---:|:---:|:---:|:---:|
|10 |20+|0.03418|14|4.0|
|20|30- |0.04186| 25  |8.0|
|30| 4 |0.01529|  9 | 20.0  |
|40| 2  |0.01081| 14  | 23.0  |
|50| 2  |0.01081| 19.0 | 23.0  |

''+'' = well over 20
'-' = a little below 30

```python
import math as m
from aguaclara.play import*
import numpy as np
from scipy.constants import g as g # standard acceleration due to gravity
from scipy.constants import pi as pi

g = g * u.m/(u.s**2)
Pi_vc = 0.62 # Pi vena contracta
diam_orif = 0.00595313*u.m
A_orif = (pi*(diam_orif/2)**2)
h1 = 0.01*u.m
Q = Pi_vc*A_orif*((2*g*h1)**0.5)
Flowrate = [Q]

for h in range(2,30):
  Q = Pi_vc*A_orif*(2*g*h*u.m/100)**0.5
  Flowrate.append(Q)

for i in range (0,30):
  print(Flowrate[i])

```
July 1 2019

Retesting flow rates to try to get a flatter sprays
using 5 mmm diameter orifice
water height roughly between 20 cm and 10 cm produced a flat spray, but down to 2 cm produced a spray.
