# Design #1: Converging Strings

**Basic Premise:** Spray or pour water over a group of strings that are all touching at a single point or along a single line. Water will ideally distribute itself evenly among all strings and follow each string towards a collection basin. Align the strings at an angle such that they get farther apart from each other as water trickles downwards. Ideally the strings would reach a final separation of 5 mm at the base where they would be anchored in place. This idea is advantageous, because it would create a solid layer of strings or a large target area for the wastewater spray to land on.

## Experiment 1
**June 4, 2019**

**Goal:** Determine if water will distribute itself over several lines of string brought together, and if it will subsequently trickle down the strings without falling off.

Consider whether the angle between two adjacent strings influences the ability of water to remain on the string.  

### Experimental Apparatus
**Insert pictures here**

**Materials:**
- 7 pieces of **Dacron** string
- ...

**Dimensions:**
- Height of support: 18 cm
- Perpendicular distance from support to strings at the farthest anchor point: 12.5 cm (this is only true for Trial 1, this distance may have varied for Trials 2 and 3)

### Methods & Results

#### Trial 1

**Setup:**
- strings anchored to every other chain link
- Base of "String triangle": 5.5 cm
- height of "string triangle": 18.0 cm from center of base to top of triangle

**Observations:**
- some of the water traveled down the strings (mostly the middle string) while some fell off near the base of the support.
- water often flowed between 2 strings, the surface tension from the water often pulled two strings close together such that they were touching.
- applying tension did not improve flow much. Droplets clearly fell off before reaching the bottom of the string.

**Conclusions:**
- need a wider angle between strings
- also try to increase the tension of the strings

#### Trial 2

**Setup:**
- 2 spaces in chainlink between each strings
- Angle between adjacent springs: 5 degrees
- Base of "String triangle": 8.5 cm
- height of "string triangle": 24.0 cm from center of base to top of triangle

**Observations:**
- water still flows between strings, but there is less string-string interaction.
- larger water droplets caused the strings to interact

**Conclusions:**
- try using the peristaltic pump to create smaller and more consistent water
- try using a small piece of foam to apply water more evenly across all strings

#### Trial 3

**Setup:**
- 3 spaces in chainlink between each strings
- Angle between adjacent springs: 10 degrees
- used the peristaltic pump at 100 RPM and the microtubing to apply water to strings
- only used the three middle strings in this trial for simplicity

**Observations:**
- adjacent strings did not get pulled together by the water at this angle, but when water flowed between them, it stills fell off as soon as the distance between the strings got too wide
- making the strings more vertical improved flow downwards but the water was still falling off.

### Experiment Conclusions:
The idea of converging strings remains a challenge. There are two main problems with this design: first, is finding a realistic way to get the water on the strings in a way that distributes it evenly. The second problem is keeping that water on the string as the distance between adjacent strings increases. With all of the strings converging at the water source, it is inevitable that some of the water flows between the strings rather than on individual strings. At some point, however, the water must 'pick a string' when the distance between two adjacent strings becomes too wide. Our experiment shows, however, that instead of 'picking a string' the water simply fell off the strings altogether. This occurred at every angle that was tested.

The issue of keeping water on the string could potentially be resolved by using a material that is more hydrophilic or has an increased ability to hold water. In the future, this experiment could be repeated using an acrylic loopy yarn rather than the Dacron string. Additionally a simpler experimental apparatus could be used for this test, by using only two strings and tying them together at the top.

## Experiment 2

June 20, 2019

**Goal:** repeat Experiment 1 with modifications to get better results

**Methods:**
The subteam repeated Experiment 1, but with some modifications to the experimental design. First, the Dacron string was replaced with acrylic loopy yarn. Second, only 2 strings were used. The strings were taped 3 cm apart on the lab table. A small container of water was place on top of tape to keep it secure when tension was applied. The other ends of the string were pinched together in the air such that they were 18 cm long. The subteam hypothesized that using a lower flow rate of water would prevent the water from accumulating between the strings, thus reducing the amount of water that would fall off.  An eye dropper was used to apply water to the pinched ends of the strings, one drop at a time. The drops were applied slow enough that little to no water accumulated between the strings.

- 67 seconds 50 drops, so about 1 drop every 1.34 seconds.
- placed 50 drops in a 10 mL graduated cylinder. Volume read 1.19 mL. So average drop size was 0.0238 mL.
- Therefore the flow rate down the string was about 1.19 mL/67 s = 0.0178 mL/s = 17.8 microL/s
- angle between strings was calculated to be 9.56 degrees using the Law of Cosines (see code below)

```python
import math as m
from aguaclara.play import*
import numpy as np

# Uses the Law of Cosines to calculate the angle of a triangle where the length of all three sides are known

a = 18*u.cm # side length
b = 18*u.cm # side length
c = 3*u.cm  # base length

C = np.arccos((a**2 + b**2 - c**2 )/(2*a*b))
print(C)
```

**Observations:**
The subteam observed a small pool of water on the table that accumulated at the base of each string, indicating that the water was in fact making it all of the way down the string. No water was absorbed falling off of the strings.

**Conclusions:** These results reinforce the idea that converging strings could be used in a trickling filter design. Specifically, the low flow rate of 17.8 microL/s was promising as the target flow rate for the string digester is 10 microL/s. This experiment could be repeated using a peristaltic pump to get consistent drop size and rate.

## Experiment 3

**Goal:** Determine the minimum angle between loopy strings such that water flows down the strings and not between them.

**Methods:**
- operate the peristaltic pump at 20 microL/s. According to the Spring 2019 Final Report, an RPM of 1.6 corresponded to 5 microL/s. So to get a average flow rate of 10 microL/s, we would need an RPM of 3.2 was used.
- The flow rate was tested experimentally by timing how long it took to fill a 10 mL graduated cylinder to the 1 mL mark. It was found that an RPM of 25.0 produced a flow rate much closer to the 10 microL/s.

Trial 1: 94.6 s = 10.57 microL/s
Trial 2: 100.53 s = 9.947 microL/s

- measure and cut 2 pieces of loopy yarn approximately 80 cm in length. Tie them together, forming a loop at one end.
- pre-wet the strings by submerging them in a bucket
- hang the strings from the scale
- tie the loose end of each string to the wooden rod such that it's length is 70 cm. Trim the excess string.
- peristaltic pump run for a few minutes at start to saturate tube with water
- aim the effluent tube of the peristaltic pump such that it drips directly below the knot on the string
- set the base width by sliding the strings apart the appropriate distance
- Starting with the strings touching, observe how the water flows. Gradually increase the angle between the strings until they don't interact with each other.

**Observations:** at such a low flow rate, the water always remained on the string and did not flow between the two strings.

**Conclusion:** The flow rate is much more important than the angle between two strings in determining whether water will stay on an individual string or travel between 2 strings.

Summer 2019 Symposium material ends here
____________________________________________
