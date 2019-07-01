# String Digester, Summer 2019 Subteam
#### Emily Wood, Madeline Garell
#### 28 June 2019

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

The String Digester sub-team was created in response to the need for additional wastewater treatment after treatment from the Upflow Anaerobic Sludge Blanket (UASB) reactor. A trickling filter is a secondary wastewater treatment system that removes organic matter from the wastewater through biological means, and is crucial for the removal of harmful pathogens. The goal of the String Digester subteam was to design a new trickling filter using strings as media that addresses the expensive nature and inefficiency of conventional designs. Current trickling filters utilize a large mechanical distributor arm to spray water onto filter media, which req costly distributor arms which clog easily and distribute water unevenly. are inefficient due to uneven distribution of water and preferential flow. Additionally, the clogging of distributor arms causes problems in daily operation.

 The subteam aimed to increase space efficiency by using a matrix of densely packed strings as the filter media. Additionally, the subteam began designing a

The subteam began designing a distribution system that would disperse water evenly to all strings and eliminate preferential pathways for water flow.


eliminating the need for a mechanical rotating arm,




High need to fit a lot of strings in a very small space.
The average human wastes water at a rate of **edit** mL/s. Therefore, a trickling filter would need to have 300 strings per person.

Like conventional trickling filters, the subteam's design incorporates a sprinkler system. This is advantageous because such a system could be accomplished without introducing a small hole into the system that could get clogged.







## Literature Review
### Trickling Filters
- copy from previous report

### Water Distribution
Uniform water distribution is essential for many applications such as irrigation and water treatment. One common method for distributing water over a relatively large area is using a spray. There are several different methods for creating a spray, two being the Fixed Spray Plate Sprinklers (FSPS) and Rotating Spray Plate Sprinklers (RSPS). A comparative study conducted by Faci et al. (2001) ([Comparison of Fixed and Rotating Spray Plate Sprinklers](https://ascelibrary.org/doi/pdf/10.1061/%28ASCE%290733-9437%282001%29127%3A4%28224%29)) found that both methods resulted in a highly uniform distribution, with RSPS slightly more uniform than FSPS (94.6% versus 93.7%). While the study also focused on the effect of wind and overlapping sprinkler arrays, the methods and materials of the sprinklers are more applicable to this report.

The FSPS design involves a water jet impinging on a fixed deflector plate, which then sprays water radially outward in the horizontal plane. The RSPS differs in that the deflector plate rotates when hit with the water jet. The nozzle diameters used in the study for both the FSPS and the RSPS were 3.8, 6.7, and 7.9 mm. The deflector plate is what creates the spray pattern, and different deflectors can result in sprays at different angles. For the FSPS, the deflector had 33 grooves which resulted in flow being divided into 33 streams for the 3.8 mm nozzle. One note from the study was that as the number of grooves in the deflector plate is increased, the drop size (for a set pressure and nozzle diameter) decreases (Kincaid et al. 1996).


- add info from previous subteam about inefficiency of distributor arm from ithaca wastewater plant
- evaluation of distribution uniformity - image
- plots of drop size distribution

### Biofilm Growth
-degradation of acrylic yarn?
### Orifice


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

### Testing Flow of Water Down Strings

####  Maximum Angle to Keep Water on a String

The converging strings design requires water to drip down strings displaced at an angle from the vertical position. The subteam hypothesized that there is a maximum string angle beyond which the force of gravity overcomes the adhesion of water to the string, causing the water to fall off the string prematurely instead of flowing all of the way down to the end.

Approximately 2 feet of loopy yarn was hung in the air in a vertical position. The peristaltic pump was used with microtubing at 75.0 RPM to supply water to the top of the string. The flow of water was observed as the string was gradually pulled outwards at an angle from its original position. The angle was varied from 0 degrees to slightly less than 90 degrees (about 85 degrees).

### Testing Water Spray
#### Testing Deflector Plate Geometries
#### Minimum Flow Rate Needed to Produce a 'Good' Spray




### Building a String Matrix

## Results and Analysis

### Testing Flow of Water Down Strings

####  Maximum Angle to Keep Water on a String

Water did not fall off of the string for any angle between 0 and 85 degrees, and was observed dripping off of the end as desired. These results demonstrate that the string angle will not inhibit water from flowing down the strings. However, having strings at different angles from the vertical may lead to strong preferential flow, and this factor should be considered further in the design of the trickling filter.


## Conclusions
## Future Work

Future work includes

- determine the extent of preferential flow in the existing design and find ways to minimize it

- determine if a biofilm will grow on the loopy yarn
- determine which microorganism cultures should be used for the string digesters
- assemble an apparatus to be used at the Ithaca wastewater plant


## Bibliography
## Manual
