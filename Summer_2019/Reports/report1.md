# String Digester, Summer 2019 Subteam
#### Emily Wood, Madeline Garell
#### 3 July 2019

## Abstract

## Table of Contents

- [Introduction](#Introduction)
- [Literature Review](#Literature-Review)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Previous Work](#Previous-Work)
- [Methods](#Methods)
  - [Experimental apparatus](#Eperimental-Apparatus)
  - [Experimental Procedure](#Experimental-Procedure)
- [Results and Analysis](#Results-and-Analysis)
- [Conclusions](#Conclusions)
- [Future Work](#Future-Work)
- [Bibliography](#Bibliography)
- [Manual](#Manual)
  - [Experimental Methods](#Experimental-Methods)
  - [Fabrication Manual](#Fabrication-Manual)
  - [Python Code](#Python-Code)


## Introduction

The String Digester sub-team was created in response to the need for additional wastewater treatment after treatment from the Upflow Anaerobic Sludge Blanket (UASB) reactor. A trickling filter is a secondary wastewater treatment system that removes organic matter from the wastewater through biological means, and is crucial for the removal of harmful pathogens. The goal of the String Digester subteam was to design a new trickling filter using strings as media that addresses the expensive nature and inefficiency of conventional designs. Current trickling filters utilize a large mechanical distributor arm to spray water onto filter media, which require costly distributor arms which clog easily and distribute water unevenly. are inefficient due to uneven distribution of water and preferential flow. Additionally, the clogging of distributor arms causes problems in daily operation.

 The subteam aimed to increase space efficiency by using a matrix of densely packed strings as the filter media. Additionally, the subteam began designing a

The subteam began designing a distribution system that would disperse water evenly to all strings and eliminate preferential pathways for water flow.


eliminating the need for a mechanical rotating arm,

- define preferential pathways


Like conventional trickling filters, the subteam's design incorporates a sprinkler system. This is advantageous because such a system could be accomplished without introducing a small hole into the system that could get clogged.







## Literature Review


### Trickling Filters
The filter media in a conventional trickling filter is usually a material such as rocks, gravel, shredded PVC bottles, or special pre-formed plastic filter media. Because all these materials are not regularly shaped and wastewater is not distributed exactly equally across the top of the media, the water follows the paths of least resistance and preferential flow occurs. Thus, there is wasted space in the filter that remains dry and unused. This leads to a less efficient treatment of organic matter than if all of the space in the filter were utilized. In their paper, Spuhler recommends using specially manufactured plastic media, like corrugated plastic sheets or even hollow plastic cylinders, to optimize surface area for biofilm formation & allow for free movement of air [(Spuhler 2018).](https://www.sswm.info/node/8215)

In addition to non-homogenous distribution of wastewater throughout the filter, there is significant documentation of other problems plant operators experience when dealing with trickling filters. Ali and co-authors state that one major problem is clogging and ponding occurring within the filter media due to high biomass sloughing rate. In the context of a trickling filter, sloughing refers to when a layer of the microbial growth loses the ability to stay attached and is shed from the filter media and washed away by water flow. If the layer of biofilm is not maintained at a desired thickness, treatment performance will decrease. Clogging results in a decreased efficiency of treatment and if it is not addressed, the quality of the effluent will suffer. Current solutions include flashing with low doses of chlorine to remove deposited solids and kill excess biomass or periodic flooding [(Ali et al. 2017)](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf). The team aims to avoid the problem altogether by using chains and having a media that will not clog up. It is still an important factor to consider in the design because any small slots or holes that the wastewater travels through in the system will likely clog up with biofilm growth.

Ali also states that the aforementioned sloughing and clogging is often caused by uneven hydraulic loading rates (HLR). Hydraulic loading rate is the amount of flow arriving at the treatment plant and going entering the treatment process at any given time. Uneven HLR is caused by clogging of the distribution arm and an uneven distribution of influent. Therefore, proper distribution of wastewater onto the filter media is crucial for optimizing efficiency of treatment. The most common method of influent distribution is rotating distributors. Rotating distributors consist of moving parts that require more maintenance and may be a burden in a plant to operators. Additionally, this system will not serve the chain-focused design.

The less common method of distribution, the fixed distribution system as seen below (**Figure 1.**), utilizes lateral and main distribution pipes, which are placed just above the trickling filter medium and spaced to give uniform distribution of water. The pipes generally have nozzles with a circular hole and a deflector. This method is commonly used with intermittent dosing, meaning flow from the system varies; it starts at a maximum and lowers as the tank empties. Currently, fixed distribution systems are mostly used in deep filter and biotowers (i.e. very tall filters). Since this method is non-rotating, it may be more applicable for the proposed use of a chain media. However, Sperling and colleagues showed that both the fixed and rotating distribution systems have an inconsistent hydraulic load of the influent [(Sperling 2007)](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402123.pdf). Therefore, the distribution system is another area where there is huge potential for the team to increase the productivity of trickling filters.

<center>

![Fixed Distribution System](https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/Fixed%20Distribution%20Trickling%20Filter.gif?raw=true)

**Figure 1.** Trickling filter with a fixed distribution system.

</center>

Although there are multiple problems with trickling filters, one main advantage of trickling filters is that they have a relatively low residence time. This is a consideration which the team should plan to maintain in future designs. Hinton and Stensel measured residence time per unit length of between 30 and 40 sec/m with dye tests. Their predicted residence times, calculated from laminar flow theory, were closer to about 15 sec/m. The authors attributed this discrepancy to "dye sorption and desorption by the biofilm." In either case, the residence time for a 5 meter deep trickling filter would be well under 5 minutes [(Hinton and Stensel 1991)](https://ac.els-cdn.com/0043135491901179/1-s2.0-0043135491901179-main.pdf?_tid=e8d2db22-8e0f-4d3c-a421-352ef74e6f5e&acdnat=1540500088_4808114af12660c061fbd139ac0fbd33). This short treatment time makes trickling filters an appealing wastewater treatment option if problems such as uneven HLR and clogging can be minimized.

[Above review of current trickling filters from [Spring 2019 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/String_Digester_Final_Report.md)]

### Water Distribution
Uniform water distribution is essential for many applications such as irrigation and water treatment. One common method for distributing water over a relatively large area is using a spray. There are several different methods for creating a spray, two being the Fixed Spray Plate Sprinklers (FSPS) and Rotating Spray Plate Sprinklers (RSPS). A comparative study conducted by [Faci et al. (2001)](https://ascelibrary.org/doi/pdf/10.1061/%28ASCE%290733-9437%282001%29127%3A4%28224%29) found that both methods resulted in a highly uniform distribution, with RSPS slightly more uniform than FSPS (94.6% versus 93.7%). While the study also focused on the effect of wind and overlapping sprinkler arrays, the methods and materials of the sprinklers are more applicable to this report.

The FSPS design involves a water jet impinging on a fixed deflector plate, which then sprays water radially outward in the horizontal plane. The RSPS differs in that the deflector plate rotates when hit with the water jet. The nozzle diameters used in the study for both the FSPS and the RSPS were 3.8, 6.7, and 7.9 mm. The deflector plate is what creates the spray pattern, and different deflectors can result in sprays at different angles. For the FSPS, the deflector had 33 grooves which resulted in flow being divided into 33 streams for the 3.8 mm nozzle. One note from the study was that as the number of grooves in the deflector plate is increased, the drop size (for a set pressure and nozzle diameter) decreases [(Kincaid et al. 1996)](https://elibrary.asabe.org/azdez.asp?JID=3&AID=27568&CID=t1996&v=39&i=3&T=1&refer=7&access=&dabs=Y).

For each of the sprinkler types, the distribution pattern was observed in varying wind conditions (low wind and medium wind) and with the sprinkler at different heights (1m and 2.5m) above the ground. Figure 2 shows that the RSPS results in a distribution with the highest density at the center (directly under the sprinkler) with the water density decreasing gradually as the radius from the center increases. However the FSPS results in a maximum density in a circular crown several meters from the center where the sprinkler is located. This difference in precipitation patterns is caused by the variation in the size of droplets from an RSPS (which can travel a wide range of distances depending on droplet diameter) compared with the relatively uniform droplet size from an FSPS.

<center>

**image

**Figure 2.** Water distribution from RSPS and FSPS sprinklers in different wind conditions at different heights.

</center>

[Faci et al. (2001)](https://ascelibrary.org/doi/pdf/10.1061/%28ASCE%290733-9437%282001%29127%3A4%28224%29) describe how varying sprinkler head height causes changes in water distribution. As the sprinkler height from the ground increases, the total wetted area increases as drops emitted in the horizontal direction are able to travel a longer distance. However, drops traveling further have a tendency to drift or evaporate causing less uniformity in the sprinkler distribution, especially at higher wind speeds.

While sprinklers create a uniform spray pattern that can be manipulated by varying parameters such as droplet size, nozzle diameter, and sprinlker height, sprinklers also require small orifices which may not be feasible with wastewater. However the methods used to spray water outward in the radial direction could be useful when designing a system to spray water in a specific pattern, such as a straight line, and the methods used to split a water stream into several smaller jets may be applicable to future string digester designs.

- add info from previous subteam about inefficiency of distributor arm from ithaca wastewater plant

### Orifice
- orifice equation

### Biofilm Growth
A component of the string digester that is crucial to its success is the growth of biofilm on the chains. "A biofilm is an assemblage of microbial cells that is irreversibly associated (not removed by gentle rinsing) with a surface and enclosed in a matrix of primarily polysaccharide material." [(Donlan 2002).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/) Biofilm attachment is a complex process regulated by diverse characteristics of the growth medium, substratum, and cell surface. Biofilm on trickling filters is composed of a variety of organisms and are typically enclosed in a polysaccharide. The biofilm matrix may also contain mineral crystals, corrosion particles, and clay or silt particles. In conclusion, biofilms in wastewater systems are often highly complex [(Donlan 2002).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/)

Some testing has been done of the growth of biofilm in different surfaces. One study compared growth on glossy electro-polished, bright annealed stainless steel to matte stainless steel and to PVC. The paper notes that stainless steel is hydrophilic and PVC is hydrophobic. In the last 45 days of the 167 day experiment, the matte steel had about 1.44 times more microorganisms than the electro-polished steel, and there was no significant difference between the PVC and polished steel. In discussion of why this occurs, Pedersen cites two reasons: "detachment due to shear forces from the flow will be reduced on the rougher surface since cells can be shielded from the bulk flow and more substratum surface area may be available for the biofilm" [(Pedersen 1990).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/)

[Above review of biofilm from [Spring 2019 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/String_Digester_Final_Report.md)]

-degradation of acrylic yarn?


### String reaeration
One of Monroe's grad students tested the reaeration of the loopy string. Can we get info on this?

## Previous Work

### Spring 2018
In Spring 2018, the Trickling Filter team spent a substantial amount of time doing research on the operational difficulties, the kinetics, and typical design parameters of trickling filters. The team aimed to address many of the issues plant operators encounter with trickling filters, like clogging and ponding, lack of moisture in parts of the filter, and general inefficiency of the filter. The two main areas for improvement the team identified were the filter media itself and the distribution system ([Spring 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Spring%20'18/TricklingFilter_Final_Report.md)).

The team fabricated a bench top model for flow mapping and conducted several rounds of tests to determine the distribution of flow in trickling filters with small rock and marble media. From these experiments, the team noticed that there were significant portions of the media that never got wet and thus concluded that a substantial volume of the trickling filter was unused due to preferential flow. From these tests the team also showed that a uniform packing material is superior to an irregularly shaped material. In an effort to both maximize the surface area to volume ratio and to minimize the footprint of the system by not wasting space, the team shifted focus towards strings as a possible filter media. This concept led the team to start with very preliminary testing of a system that was essentially an overflowing basin with strings submerged at the top, inside the basin, and draped over the sides to guide water down to a collection bucket below (See **Figure 2.**, the same experimental set-up used in Spring 2018). In these initial tests, the team members observed that the water did in fact follow the along strings when it overflowed. From these observations, the String Digester team began to design more rigorous tests on the concept and planned to investigate whether using strings in a wastewater treatment system is truly viable.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Photos/Screen%20Shot%202018-10-24%20at%203.14.20%20PM.png?raw=true" />

**Figure 2**. Experimental Set-up with water basin from [Fall 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Fall%20'18/Final_Report_stringdigester.md) Section 1.2.2 Figure 2.
</center>

### Fall 2018
In Fall 2018, the team continued experimentation with the overflowing basin from the previous semester. The string yarn was abandoned due to its degradability. Nylon, polypropylene, and a stainless steel wire and cable were first tested on the same set-up from Spring 2018 with the overflowing basin. The plastics were chosen for their non-biodegradability; however, the stainless steel wires may be susceptible to corrosion. None of the preceding materials performed well on the basin set-up as the water did not follow the strands due to their hydrophobicity.

Next, two foams and two stainless steel chains were tested on the same basin in addition to a winged basin set up. These materials were able to retain water as it trickled down. The blue foam absorbed water especially well. The initial testing done on these materials suggests they could work in the proposed system and make the string digester technology possible. Further testing will be done on the chains as the foams are thought to easily clog; therefore, they are not confirmed to be a viable solution at this point. See [Fall 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Fall%20'18/Final_Report_stringdigester.md) for more information.

### Spring 2019

The Spring 2019 subteam focused its research on identifying a viable material for the string digester media based on its retention of water and ability to grow a biofilm. The subteam investigated several chains with different sized chain-links, before switching to more hydrophylic polymers: Dacron (polyethylene terephthalate) and Aramid strings. The subteam calculated the string length needed for a 15 minute residence time for each material, as well as the water retention of multiple chains in the same basin. The subteam identified the Dacron string as having the most potential for a string digester as water flowed down it relatively uniformly and it only required a height of 1.97 m for a 15 min residence time. The Dacron string was used to test whether capillary action could be implemented as a water distribution system. Finally, the subteam calculated the theoretical efficiency (BOD removal per unit area) of a string digester and found that it compared with or exceeded traditional low-rate and high-rate trickling filters. See [Spring 2019 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/String_Digester_Final_Report.md) for more information.

## Methods

The Summer 2019 subteam researched design parameters for the trickling filter and began building a prototype for initial testing. Two designs were considered as outlined in the [Introduction](#Introduction) section: a converging strings design, and a basin with holes design. Specifically, the subteam addressed the maximum angle needed to keep water on the loopy yarn, the minimum flow rate to produce a 'good' spray, and  the maximum string density possible. These design questions, among others, will be elaborated on in the following paragraphs.

### Design Parameters

####  Maximum angle needed to keep water on a string

The converging strings design requires water to drip down strings displaced at an angle from the vertical position. The subteam hypothesized that there is a maximum string angle beyond which the force of gravity overcomes the adhesion of water to the string, causing the water to fall off the string prematurely instead of flowing all of the way down to the end.

To investigate this property, approximately 2 feet of loopy yarn were hung in the air in a vertical position. The peristaltic pump was used with microtubing at 75.0 RPM to supply water to the top of the string. The flow of water was observed as the string was gradually pulled outwards at an angle from its original position. The angle was varied from 0 degrees to slightly less than 90 degrees (about 85 degrees).


#### Maximum flow rate on each string

In order to ensure proper microbe digestion by the biofilms, Dr. Weber-Shirk advised a residence time of 15 minutes on each string for the water. The residence time could be controlled by either altering the length of each string or the flowrate of water. Using increasingly longer strings to lengthen the residence time is problematic, because a taller filter requires more energy to transport the water to the top for cleaning. Therefore the residence time must be controlled primarily by flow rate.

Previous research conducted by members of CEE 4530 used flow rates ranging from 1.75 to 17.2 microliters/second to test the aeration of water on the loopy yarn.   **edit** was needed to achieve a residence time of 15 minutes on a **? m long** loopy yarn. This string height was deemed reasonable because...**edit**. Therefore, 10 microliters/second **edit units** was the maximum flowrate per string.

#### Number of Strings Needed to Support a Small Population

To investigate the feasibility of using strings as a filter media, the subteam calculated the number of strings needed to support the population of a small town of 10,000 people.

According to **edit**, the average human wastes water at a rate of 3 mL/s, or 3000 microliters/second. If the flowrate down each string is 10 microliters per second, each person would need 300 strings to keep up with their own wastewater production. Therefore a population of 10,000 people would need a trickling filter composed of 3 million strings.

### Number of Strings that Fit on 1 cm of a Rod

 It was found that at most 19 **edit (measure diameter of string) This goes in results!** passes of loopy yarn could fit on a length of rod 1 cm long. This number was acquired experimentally by tightly wrapping the loopy yarn around a thin rod until it covered 1 cm of its length. This number determined the maximum string packing density.

#### Minimum Spacing Between Strings

Several factors were considered when choosing the initial spacing between strings. Due to the vast number of strings required to support a small town, the subteam needed to pack the strings as densely as possible to improve space efficiency. However, if the strings were too close, water droplets could potentially switch from one string to another mid-flow, leading to preferential pathways. Several sources **edit** suggest that an average raindrop is usually between 0.5 and 3 mm in diameter. A raindrop was used in comparison to a drop of water sprayed on a string. Therefore a string spacing of 5 mm was chosen to avoid unwanted string-string interaction. **vague?**

#### Testing Deflector Plate Geometries

Several materials and geometries were tested for use as a deflecting plate. These included PVC pipes cut in half (producing semi-cylinders), PVC sheets of different thicknesses and widths, in addition to a bottle to test a cylindrical shape. For specific dimensions of these materials, please reference the [manual](#Deflector-Plate-Experiments) section. These materials were tested by placing them under running water from the sink and observing the quality of the spray. They were visually evaluated on spray uniformity and width.

#### Minimum Flow Rate Needed to Produce a 'Good' Spray

The subteam defined a good spray pattern as being composed of small droplets uniformly spaced over a large area.  

The subteam first used the laboratory sink to identify a baseline flow rate that would produce a 'good' spray. A flat sheet of plastic approximately 1 inch inches in width was held under the faucet as a deflector plate such that the water stream struck the middle of the plate. The same deflector plate was used for all experiments to follow. The strength of the faucet was adjusted until a wide, flat, and even spray was formed. The strength of the faucet was decreased gradually until the water spray could no longer be defined as 'good'. At this point, the deflector plate was removed and the flow rate of the sink was measured by timing how long it took to fill up a 3 liter container. The volume was divided by the time to obtain the flow rate in L/s. This measurement was repeated for a total of 3 times, and the trials were averaged.

With this baseline flowrate in mind, an apparatus was built to replicate the spray pattern using water flow due to gravity through an orifice. The end of a clear PVC tube was covered with a hard plastic sheet and glued to form a watertight seal. Four different diameter holes were drilled into the PVC sheet: 7/32" (5.56 mm), 15/64" (5.95 mm), 17/64" (6.75 mm), and 3/8" (9.53 mm). Any hole that was not being used for a particular trial was temporarily sealed with waterproof tape. The PVC tube, or 'water column' as it will now be referenced as, was measured and marked every centimeter along its length.

Using the 9.53 mm orifice, Equation 1 was used to calculate the height of water needed in the column to obtain the same flow rate that was used in the sink: 0.1160 L/s. The water column was filled beyond this height and centered over the deflector plate. The spray pattern was observed when the water level reached the calculated height of 28.9 cm.

##### Decreasing Flow Rate
The subteam wanted to know if a reasonable spray pattern could be produced with an even lower flow rate from the orifice. Decreasing the flowrate was desirable due to the limitation on the number of strings that could be packed into a finite space. With the current flow rate of 0.1160 L/s, a total of 11,600 strings would need to be used to achieve a maximum flow rate of 10 microliters/second per string. With 5 mm spacing between strings, this would cover a square area with 38.1 cm side lengths.

The remaining orifice sizes were tested with different flow rates and water heights. The combinations of orifice size, flow rate, and water column height tested are shown in Table **edit** below. Due to unnecessary rounding of orifice diameters when using Equation 1, errors existed when calculating the water height needed to achieve a particular flow rate. The last column of the table shows the corrected heights calculated after experimentation using more precise orifice measurements.**consider removing this part**

|Orifice Diameter [mm]|Flow Rate [L/s]|Water Height [cm]| Height Correction [cm]|
|:---:|:---:|:---:|:---:|
| 6.72  | 0.05798  | 35.5  | 34.9 |
| 6.72 | 0.03866  | 15.8 | correct  |
| 5.56   | 0.039374 |  35.0 |  correct |
| 5.95  | 0.030079  | 15.5  |  correct |

##### Varying water velocity

The minimum flow rate to produce a good spray was found to be approximately 0.035 +_ **edit** 0.005 L/s. However, these calculations neglected to consider the effect of velocity on spray pattern. The subteam hypothesized that the same quality of spray could be achieved at a lower flow rate by increasing the velocity of water hitting the deflector plate. The velocity of the water was increased by extending the time and distance that it fell from the orifice before hitting the deflecting plate. As the water velocity was more difficult to measure directly, an experiment was conducted to determine the ideal distance between the orifice and deflecting plate.

The spray pattern produced by the water column was video recorded as it was repeatedly filled and emptied, with different orifice-deflecting plate distances. Distances of 10, 20, 30, 40, and 50 cm were used with a constant orifice diameter of 5.95 mm. The water height was read off of the PVC tube while it was emptied so that the spray pattern in the video could be associated with a particular flow rate via Equation 1. A tape measure was laid down in the plane of water spray so that the size of the spray could be compared between trials. The videos were analyzed by identifying the water height at which the spray pattern could no longer be defined as 'good'. Python code incorporating Equation 1 was written to calculate the flow rate associated with these water heights.


### Experimental Apparatus

#### Converging Strings Design

In order to create a more efficient trickling filter, the subteam needed to design a matrix of strings that minimized preferential flow while packing the strings as densely as possible.

The subteam proposed a design in which the strings would be wrapped around a 'loom' of rods, using beads as a separator between strings on each rod. Each loop of string would be wrapped as compactly as possible around a large central rod where water would be sprayed.

Two rows of holes were drilled in a piece of plywood approximately 10 cm apart. Each row contained 16 holes with 5 mm spacing. Thin rods were inserted into each hole and threaded with 8 beads that were 5 mm in diameter. The top bead was glued in place. Two additional holes were drilled about 10 cm above the top row and another one about 10 cm below the bottom row as seen in image **edit** below. A **edit** rod was inserted into each hole and secured with a nut and washer on either side of the plywood. These rods were covered with 1/4" NPT **edit** hard plastic tubing to provide a smooth surface for the strings to rest on. The end of the loopy yarn was taped to the backside of the plywood and the rest of the string was wrapped around the system of rods according to diagram **edit** to form a matrix.

#### Basin with Holes Design



## Results and Analysis


### Maximum Angle to Keep Water on a String

Water did not fall off of the string for any angle between 0 and 85 degrees, and was observed dripping off of the end as desired. These results demonstrate that the string angle will not inhibit water from flowing down the strings. However, having strings at different angles from the vertical may lead to preferential flow, and this factor should be considered further in the design of the trickling filter.

### Initial String Matrix Testing

### Testing Water Flow Down Loopy Yarn

At the given flow rate, water successfully travelled down the entire length of the strings without falling off. However, it did not travel in distinct droplets. Rather, the water appeared to saturate the loops of the yarn, and flowed down uniformly around the entire string. The absence of large droplets suggests that the string spacing could actually be much smaller than 5 mm. This is because... **edit**. The subteam should consider, however, if tight string spacing could negatively affect the ability for the strings to reaerate.


## Conclusions
## Future Work

Future work includes

- determine the absolute minimum spacing between strings
- determine the extent of preferential flow in the existing design and find ways to minimize it

- determine if a biofilm will grow on the loopy yarn
- determine which microorganism cultures should be used for the string digesters
- assemble an apparatus to be used at the Ithaca wastewater plant


## Bibliography
## Manual
This manual is broken down into several different experimental methods, each with a list of materials, fabrication details, special components, and experimental procedure.

### Experimental Methods
---
#### Maximum String Angle Experiment
Determine the minimum angle that a string (specifically loopy yarn) can be displaced from the vertical position such that no water falls off of the string prematurely as it runs down.

##### Materials
- Loopy yarn
- Peristaltic pump with microtubing of ID = 0.05mm **units?**

##### Fabrication Details
Step 1. Cut a length (at least 20cm) of yarn and attach one end of yarn to object where the yarn can hang down and the angle between the length of yarn and the vertical can be varied from 0 to 90 degrees.

Step 2. Set up peristaltic pump to drip water onto the top of the string and pump at 75.0 rpm

##### Special Components
Loopy Yarn
**add image and details**

##### Experimental Procedure
Step 1. Gradually pull the bottom end of the string outwards, increasing the angle between the string and the vertical from 0 to just below 90 degrees.

Step 2. Observe the path the water travels as this angle is increased.

---
#### Converging Strings Experiment
Determine if water will distribute itself over several lines of string brought together, and if it will subsequently trickle down the strings without falling off. Consider whether the angle between two adjacent strings influences the ability of water to remain on the string.  

##### Materials
- Loopy yarn
- Tape

##### Fabrication Details
Step 1. Cut 20cm two cm lengths of loopy yarn and use tape to secure one end of each string to a single point 10cm above a table.

Step 2. Secure the other end of each string to points on the table so that the taught strings form a diagonal and are spaced 5mm apart.

##### Special Components
None

##### Experimental Procedure
Step 1. Use a pipette to drip water onto the point where the strings converge and observe the flow of water down the strings.

Step 2. Vary the angle between the strings by increasing or decreasing the distance between the strings on the table and observe the flow of water.

---
#### Basin With Holes Experiment
##### Materials
- Loopy yarn
- PVC **dimensions for basin and base for cuvettes**
- PCV glue
- Electrical drill with **drill bit size for holes** drill bit
- 13 cuvettes
- 13 hex nuts
- Permanent marker

##### Fabrication Details
- ###### Fabrication of Basin
  Step 1. Use PCV glue and **PVC dimensions** to form a basin with a **dimensions** base and height of **dimension**.

  Step 2. Mark a grid of points 2.5cm by 2.5cm on the bottom of the basin with points every 5mm in each direction.

  Step 3. Drill through selected points (see **image**) using specified drill bit size.

- ###### Experiment Set-up
  Step 1. Cut 13 20cm lengths of loopy yarn and thread one end of each string through a hole in the bottom of the basin, knotting twice to secure on inside of basin.

  Step 2. Tie a hex nut at the other end of each string as a weight to keep the strings taught.

  Step 3. Secure basin at a height so the strings  hang down.

  Step 4. Glue cuvettes to **dimensions** piece of PVC in the same pattern as the drilled holes so that each hex nut can be placed in a cuvette and the corresponding string will form a straight line from the basin to the cuvette.

  Step 5. Mark each cuvette 1-13 for reference.

##### Special Components
- Basin **image**

##### Experimental Procedure
Step 1. Ensure that the knots in the basin are directly over the drilled holes and that the strings are taught.

Step 2. Fill the basin with water and observe how long it takes to empty, the flow of water down each string, and the distribution of water collected in the cuvettes.

Step 3.Record data such as volume of water added to basin, time for basin to empty, and the height of water in each cuvette in a table. Calculate total flowrate and flowrate per string and record.   

Step 4. Take hexnuts and strings out of cuvettes to empty cuvettes then place the back to repeat experiment.

---
#### Deflector Plate Experiments
Determine a material and geometry that will produce an ideal spray pattern (a line of spray).

##### Materials
- Flat piece of plastic **dimensions**
- Flat rectangular piece of PVC **dimensions**
- Flat circular piece of PVC **dimensions**
- 1/2 pipe **dimensions**
- 1/4 pipe **dimensions**
- Plastic bottle **dimensions**
- Bandsaw
- Sink
- Permanent marker

##### Fabrication Details
- ###### Sprinkler deflector plate fabrication
 Step 1. Using bandsaw, cut off the bottom centimeter of the bottle.

  Step 2. Mark **number** 1cm lines uniformly spaced around the edge of the circle from the bottom of the bottle.

  Step 3. Use the band saw to cut 1cm slits around the bottom of the bottle.

##### Special Components
Sprinkler deflector plate (modeled from FSPS deflector, see Literature Review: Water Distribution)
**image**

##### Experimental Procedure
Step 1. In a sink, begin with a uniform flowrate and, one at a time, place each deflector in the flow to create a spray pattern.

Step 2. Observe spray pattern (droplet size, spray distance, ...) and any changes when the position (height or orientation) of the deflector is changed.

---
#### Spray Experiments
Determine the flow rate, orifice size, and water height that will produce the best jet spray. Ideally the jet spray would cover a wide surface area evenly with small water droplets.

##### Materials
- PVC tube **dimensions**
- PVC sheet **dimensions**
- PVC glue
- Tape measure
- Permanent marker
- Deflector plate (from above experiment)
- Sink
- Electric drill
- Drill bits: **sizes**
- 6L bucket
- Tape

##### Fabrication Details
- ###### Fabrication of water dispensing tube
  Step 1. Use PVC glue to attach PVC sheet to one end of the PVC tube with a watertight seal.

  Step 2. Mark and label heights every 5cm from the bottom of the tube (with the PVC sheet) to the top.

  Step 3. Drill one hole of each size in the bottom of the PVC sheet so that each is inside the circumference of the tube but not too close to each other.

##### Special Components
Water dispensing tube **image**

##### Experimental Procedure
Step 1. Tape over all but one hole on the bottom of the water dispensing tube ****

---
#### Current Model
- fabrication of plywood/bead/string set up
##### Materials
##### Fabrication Details
##### Special Components
##### Experimental Procedure

### Python Code
