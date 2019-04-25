# String Digester, Spring 2019
#### Kiki Lo, Antonio Martinez, Gaby Sibel, Zsofia Szegletes
#### April 16, 2019

**[Felix grading here. I liked your report. It was informative, well organized, and it looks like you guys made some solid progress this semester.]

**[After addressing any comments please write within the brackets "-Addressed __" with the individual's initials in the __ space. They will be deleted in the next report.]**

## Abstract
The objective of String Digester for the Spring 2019 semester was to continue research on revamping a wastewater treatment system to eliminate problems associated with current trickling filters. To improve consistency in wastewater treatment, experiments were conducted using metallic and plastic chains to optimize surface area. The long-term goal of this team is to create an efficient wastewater treatment system that will perform secondary and tertiary treatment on domestic wastewater. These tests will involve different chain types and materials, chain spacing, and biofilm growth to help define design parameters for the construction of a functioning string digester.

**[Write in past tense throughout report when talking about current semester or prior semester work.]**

**[The previous comment was still not addressed as of the April 16th version of this report. So this will be reflected on the style portion of your grade. For example, in the last sentence in the abstract it should be... "These tests involved" instead of "These tests will involve". Generally you should be writing as if someone a year or a couple years from now was reading this, thus everything would be in the past. ]**

## Introduction
The String Digester sub-team was created in response to the remaining need for secondary wastewater treatment after treatment from the Upflow Anaerobic Sludge Blanket (UASB) reactor. A trickling filter is a secondary wastewater treatment system that removes organic matter from the wastewater through biological means, and is crucial for the removal of harmful pathogens. Looking to improve on the traditional industrial-scale trickling filter design, previous work identified an issue with the process: there is a substantial amount of unused space in the trickling treatment unit due to the uneven flow of wastewater across the system (preferential flow). The primary objective of this sub-team is to continue to develop a novel design for a highly efficient trickling filter with a minimized footprint in terms of space. Following the conclusion from Fall 2018, that metal chains would be a viable trickling media due to their retention of water, the team decided to focus this semester's research on trying to determine what material and type of chain would work best in terms of water retention and biofilm growth and from there, determining the best matrix for these chains to be in to maximize water retention on chain media. With this work, the team will work towards assessing the feasibility of a modified trickling filter unit in future AguaClara treatment plants while striving to make significant technological improvements on industry-standard applications for the system.

Research dealing with trickling filter wastewater treatment was ubiquitous in the 1970's and 1980's, however, the research in this field has significantly declined in the following decades. Moreover, research involving string as a media in this method of treatment is almost nonexistent. Research on secondary wastewater treatment originally focused on performance of trickling filters, but now has shifted towards processes higher in energy consumption. The philosophy for AguaClara plants is to create a plant that is optimized for low cost and a high performance, and looking at the regions a future wastewater plant would serve, trickling filters are a promising technology due to their low-energy requirements. With work in reducing unused space in these plants, these treatment systems are ideal **[This sentence is unclear. Don't know what it is saying exactly.. Does it mean that AC does work in reducing unused space, making it ideal?]**. Maintaining these ideals will be a priority in the team's future design. With modification, the trickling filter treatment system carries much potential to be implemented in areas of the world in which capital expenditure is a major barrier for employing traditional secondary wastewater treatment (aeration tanks).


## Literature Review
### Trickling Filters
The filter media in a conventional trickling filter is usually a material such as rocks, gravel, shredded PVC bottles, or special pre-formed plastic filter media. Because all these materials are not regularly shaped and wastewater is not distributed exactly equally across the top of the media, the water follows the paths of least resistance and preferential flow occurs. Thus, there is wasted space in the filter that remains dry and unused. This leads to a less efficient treatment of organic matter than if all of the space in the filter were utilized. In their paper, Spuhler recommends using specially manufactured plastic media, like corrugated plastic sheets or even hollow plastic cylinders, to optimize surface area for biofilm formation & allow for free movement of air [(Spuhler 2018).](https://www.sswm.info/node/8215)

In addition to non-homogenous distribution of wastewater throughout the filter, there is significant documentation of other problems plant operators experience when dealing with trickling filters. Ali and co-authors state that one major problem is clogging and ponding occurring within the filter media due to high biomass sloughing rate. In the context of a trickling filter, sloughing refers to when a layer of the microbial growth loses the ability to stay attached and is shed from the filter media and washed away by water flow. If the layer of biofilm is not maintained at a desired thickness, treatment performance will decrease. Clogging results in a decreased efficiency of treatment and if it is not addressed, the quality of the effluent will suffer. Current solutions include flashing with low doses of chlorine to remove deposited solids and kill excess biomass or periodic flooding [(Ali et al. 2017)](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf). The team aims to avoid the problem altogether by using chains and having a media that will not clog up. It is still an important factor to consider in the design because any small slots or holes that the wastewater travels through in the system will likely clog up with biofilm growth.

Ali also states that the aforementioned sloughing and clogging is often caused by uneven hydraulic loading rates (HLR). Hydraulic loading rate is the amount of flow arriving at the treatment plant and going entering the treatment process at any given time. Uneven HLR is caused by clogging of the distribution arm and an uneven distribution of influent. Therefore, proper distribution of wastewater onto the filter media is crucial for optimizing efficiency of treatment. The most common method of influent distribution is rotating distributors. Rotating distributors consist of moving parts that require more maintenance and may be a burden in a plant to operators. Additionally, this system will not serve the chain-focused design.

The less common method of distribution, the fixed distribution system as seen below (**Figure 1.**), utilizes lateral and main distribution pipes, which are placed just above the medium   **[medium up to this point has not been mentioned. Does this refer to growth medium or media? If possible keep consistent]** and spaced to give uniform distribution of water. The pipes generally have nozzles with a circular hole and a deflector. This method is commonly used with intermittent dosing, meaning flow from the system varies; it starts at a maximum and lowers as the tank empties. Currently, fixed distribution systems are mostly used in deep filter and biotowers (i.e. very tall filters). Since this method is non-rotating, it may be more applicable for the proposed use of a chain media. However, Sperling and colleagues showed that both the fixed and rotating distribution systems have an inconsistent hydraulic load of the influent [(Sperling 2007)](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402123.pdf). Therefore, the distribution system is another area where there is huge potential for the team to increase the productivity of trickling filters.

<center>

![Fixed Distribution System](https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/Fixed%20Distribution%20Trickling%20Filter.gif?raw=true)

**Figure 2.** Trickling filter with a fixed distribution system.

</center>

Although there are multiple problems with trickling filters, one main advantage of trickling filters is that they have a relatively low residence time. This is a consideration which the team should plan to maintain in future designs. Hinton and Stensel measured residence time per unit length of between 30 and 40 sec/m with dye tests. Their predicted residence times, calculated from laminar flow theory, were closer to about 15 sec/m. The authors attributed this discretion **[discretion may not be the right word here.. difference/discrepancy?]** to "dye sorption and desorption by the biofilm." In either case, the residence time for a 5 meter deep trickling filter would be well under 5 minutes [(Hinton and Stensel 1991)](https://ac.els-cdn.com/0043135491901179/1-s2.0-0043135491901179-main.pdf?_tid=e8d2db22-8e0f-4d3c-a421-352ef74e6f5e&acdnat=1540500088_4808114af12660c061fbd139ac0fbd33). This short treatment time makes trickling filters an appealing wastewater treatment option if problems such as uneven HLR and clogging can be minimized.


### Biofilm
A component of the string digester that is crucial to its success is the growth of biofilm on the chains. "A biofilm is an assemblage of microbial cells that is irreversibly associated (not removed by gentle rinsing) with a surface and enclosed in a matrix of primarily polysaccharide material." [(Donlan 2002).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/) Biofilm attachment is a complex process regulated by diverse characteristics of the growth medium, substratum, and cell surface. ~~Biofilm~~ on trickling filters ~~are~~ **[, biofilm is]** composed of a variety of organisms and are typically enclosed in a polysaccharide. The biofilm matrix may also contain mineral crystals, corrosion particles, and clay or silt particles. Biofilms in wastewater systems are often highly complex [(Donlan 2002).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/) **[Last sentence is kind of just oddly placed. Maybe just start it off with "In conclusion,"]**

Some testing has been done of the growth of biofilm in different surfaces. One study compared growth on glossy electro-polished, bright annealed stainless steel to matte stainless steel and to PVC. The paper notes that stainless steel is hydrophilic and PVC is hydrophobic. In the last 45 days of the 167 day experiment, the matte steel had about 1.44 times more microorganisms than the electro-polished steel, and there was no significant difference between the PVC and polished steel. In discussion of why this occurs, Pedersen cites two reasons: "detachment due to shear forces from the flow will be reduced on the rougher surface since cells can be shielded from the bulk flow and more substratum surface area may be available for the biofilm" [(Pedersen 1990).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732559/) [Translate pedersen!]


In another experiment, three different types of plastic often used in pipe production were investigated for biofilm formation. These materials were PVC, PEX, and HDPE. After two years of system operation, which included weekly pipeline flushing, biofilm analyses were taken. It was found that the PEX pipe had the highest number of bacteria growing (1.15*10<sup>3</sup> $\frac{CFU}{cm^2}$; CFU: colony-forming unit), HDPE pipes had two times less the amount of bacteria (451 $\frac{CFU}{cm^2}$), and PVC surfaces had a significantly lower bacteria count (193 $\frac{CFU}{cm^2}$). However, the number of microorganisms found in the pipes was not related to the number of mineral deposits found, as HDPE pipes had the thickest biofilms with bacteria attached to mineral deposits or immersed in exopolymers. Bacteria did not form large aggregates on PEX surfaces, and PVC biofilm was only made of single cells and did not have any mineral deposits. It was concluded that the ranking of susceptibility to biofilm growth and colonization was HDPE, PEX, and PVC respectively. [(A. Rożej et al., 2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4282696/)


Studies have also been conducted about the bacteria that produce the biofilm on the stainless steel. Many of these studies involve curli-producing bacteria. Curli fibers "are the major proteinaceous component of a complex extracellular matrix produced by many Enterobacteriaceae" and "are involved in adhesion to surfaces, cell aggregation, and biofilm formation" [(Barnhart and Chapman).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2838481/) One such study focused on *Escherichia coli* O157:H7 bacteria with 6 individual strains, three of which produced curli and three which did not. The study found that the gene for curli production did not affect the attachment of the bacteria to the stainless steel, but it did affect the formation of biofilms. Only the curli producing strains were able to form biofilms [(Ryu et al. 2004).](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1472-765X.2004.01591.x) However, since *E. coli* are commonly found in wastewater, it is probable for biofilm to be able to grow on the stainless steel chains as long as some **[strains of E. coli]** ~~kind of bacteria~~ with the curli-producing gene is present in the wastewater and the flow rate is not too fast. So, assuming that the bacteria will most likely be present and once the biofilm is built up on each of the chains, the main issue then becomes preventing accumulated biofilm from falling off one chain and then, in a domino effect, dragging it off other chains as well.

## Previous Works
### Spring 2018
In Spring 2018, the Trickling Filter team spent a substantial amount of time doing research on the operational difficulties, the kinetics, and typical design parameters of trickling filters. The team aimed to address many of the issues plant operators encounter with trickling filters, like clogging and ponding, lack of moisture in parts of the filter, and general inefficiency of the filter. The two main areas for improvement the team identified were the filter media itself and the distribution system ([Spring 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Spring%20'18/TricklingFilter_Final_Report.md)).

The team fabricated a bench top model for flow mapping and conducted several rounds of tests to determine the distribution of flow in trickling filters with small rock and marble media. From these experiments, the team noticed that there were significant portions of the media that never got wet and thus concluded that a substantial volume of the trickling filter was unused due to preferential flow. From these tests the team also showed that a uniform packing material is superior to an irregularly shaped material. In an effort to both maximize the surface area to volume ratio and to minimize the footprint of the system by not wasting space, the team shifted focus towards strings as a possible filter media. This concept led the team to start with very preliminary testing of a system that was essentially an overflowing basin with strings submerged at the top, inside the basin, and draped over the sides to guide water down to a collection bucket below (See **Figure 3.**, the same experimental set-up used in Spring 2018). In these initial tests, the team members observed that the water did in fact follow the along strings when it overflowed. From these observations, the String Digester team began to design more rigorous tests on the concept and planned to investigate whether using strings in a wastewater treatment system is truly viable.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Photos/Screen%20Shot%202018-10-24%20at%203.14.20%20PM.png?raw=true" />

**Figure 3**. Experimental Set-up with water basin from [Fall 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Fall%20'18/Final_Report_stringdigester.md) Section 1.2.2 Figure 2.
</center>

### Fall 2018
In Fall 2018, the team continued experimentation with the overflowing basin from the previous semester. The string yarn was abandoned due to its degradability. Nylon, polypropylene, and a stainless steel wire and cable were first tested on the same set-up from Spring 2018 with the overflowing basin. The plastics were chosen for their non-biodegradability; however, the stainless steel wires may be susceptible to corrosion. All of the preceding materials did not perform well on the basin set-up as the water did not follow the strands due to their hydrophobicity.


Next, two foams and two stainless steel chains were tested on the same basin in addition to a winged basin set up. These materials were able to retain water as it trickled down. The blue foam worked exceptionally well as it absorbed water. The initial testing done on these materials suggests they could work in the proposed system and make the string digester technology possible. Further testing will be done on the chains as the foams are thought to easily clog; therefore, they are not confirmed to be a viable solution at this point. See [Fall 2018 Final Report](https://github.com/AguaClara/String-Digester/blob/master/Fall%20'18/Final_Report_stringdigester.md) for more information.

## Methods
### Single Chain Experiments
#### Objectives of Experiments
The objective of the initial experiment was to determine the peak amount of water that the chain could hold at a single point in time, the residence time for water on the chain at different flow rates, and the height needed for a 15 minute residence time at different flow rates.

#### Experimental Apparatus
A scale was secured approximately one meter above a lab bench resting on supports at each corner so that the bottom of the scale was left accessible. A 3-foot single chain was attached to the hook on the bottom of the scale and was allowed to hang down freely (see **Figure 4** below). The hook on the scale measured the weight of the chain. Reference the [Single Chain Experiment Manual](#Single-Chain-Experiment) section for a detailed explanation of the set-up.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/bvchain.jpg.jpg?raw=true" height=400>

**Figure 4.** Bottom view of scale resting on supports with chain hooked onto bottom.

</center>

#### Procedure
Reference the [Single Chain Experiments Manual](#Single-Chain-Experiment) section for a detailed procedure. The scale was zeroed with the chain hanging on the scale so that the scale would only measure the weight of the water on the chain. Narrow tubing (ID: 16) was connected to a peristaltic pump and water was pumped at a known rate. The end of the tube was directed onto the top of the chain hanging from the scale, in an attempt to allow water to flow onto and down the hanging chain.

The idea was to get water flowing onto the chain and then, while continuously pumping water onto the chain, measure the weight of the water on the chain at a moment in time. Because the scale reading often fluctuated, a range of weights was recorded. The weight of the water (in grams) on the chain was recorded for several different flow rates of water. The first two flow rates used were 1.5 mL/s and 3 mL/s and then every multiple of 5 from 5-80 mL/s was used after the initial two.

From these measurements, the team was able to quantify how much water the chain could hold per unit length. After, the team calculated the residence time by dividing the volume of water on the chain by flow rate. From this information, the team calculated the height of the chain needed for a residence time of 15 minutes.

**[Starting in procedure you start using a residence time of 15 minutes but I don't think you have ever justified why you do. Could you do that?]**

### Chain Matrix Experiment
#### Objective of Experiment
The objective of this chain matrix experiment was to identify and compare the water retention of multiple chains in the same basin of water.

#### Experimental Apparatus
Six evenly spaced holes were drilled into a basin. Six 3-foot chains were subsequently inserted into these holes and were left to hang freely from the other end (see **Figure 5**). The basin was placed on top of a rod that rested across from the four supports in the previous experiment (see **Figure 5.**) **[I believe you mean figure 6 here]**. Reference the [Chain Matrix Experiment](#Chain-Matrix-Experiment) Manual section for detailed information on the Experimental Apparatus.

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/bvchainmatrix.jpg.jpg?raw=true" height=400>

**Figure 5.** Bottom view of chains inserted in basin.

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/betterbvpicc.jpg?raw=true" height=400>

**Figure 6.** Bottom view of basin with chain matrix resting on rod.

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/zoomedout.jpg.jpg?raw=true" height=400>

**Figure 7.** View of entire set up, with basin, supports, and chain matrix.

</center>

#### Procedure
The narrow tubing (ID: 16) was connected to a peristaltic pump and was directed into the basin. The peristaltic pump was used to control the amount of water that flowed into the basin. The amount of water flowing onto each chain was analyzed and compared for retention.

### Single Dacron String Experiment
#### Objectives of Experiment
The objectives of the single Dacron string experiment were to determine how uniformly water flowed down the string and the length of a string needed for the  water to have a 15-minute residence time on the string.

#### Experimental Apparatus
A 30-inch wetted Dacron string was hooked onto the bottom of a scale and allowed to hang freely from the scale. The scale, which measured the weight of the string, was placed on top of two support beams above the lab bench. Orange-yellow color-coded micro-tubing (ID: 0.05) connected to the peristaltic pump was draped over the support beam and taped onto a flat rod between the two beams so that the tubing was allowed to just barely touch the side of the top part of the string. Reference the [Single Dacron String Experiment Manual](#Single-Dacron-Experiment-Manual)[space]for a detailed explanation of the set-up.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/zoomedoutdacron.jpeg?raw=true" height=400>

**Figure 8.** Zoomed out view of Dacron string, scale, and microtubing.

</center>

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/topview%20single%20dacron.jpeg?raw=true" height=400>

**Figure 9.** Bird's eye view of microtubing mounted on flat rod and directed under scale.

</center>

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/close%20up%20microtubing.jpeg?raw=true" height=400>

**Figure 10.** Zoomed in photo of the microtubing placement just next to the string, with water being released onto the string.

</center>

#### Procedure
Reference the [Single Dacron String Experiment Manual](#Single-Dacron-Experiment-Manual)[space]for a detailed explanation of the procedure.[space]The string was dipped in water prior to hanging on the scale in order to allow water to stay on the string more effectively. The scale was zeroed with the string hanging on the scale so that the scale would only measure the weight of the water flowing on the string. Water was pumped at a controlled flow rate through the tubing and onto the string. The idea was to allow the tubing to just barely touch the string so that it could release water directly onto the string without putting the string at an angle.

Once the scale began reading steady weights, a range of weights was recorded for an RPM(revolution/minute) starting at 77.8, then 70, followed by every 10 RPM after that (60, 50,...,10 RPM) and finally at 1.6 RPM(the smallest possible RPM), which correlated to flow rates starting at 0.0246 mL/s down to .0005 mL/s. Then, residence times on the string were calculated by dividing the total weight on the string by flow rate (in mL/s) for each RPM tested. Finally, the length of the string needed for the water to have a retention time of 15 minutes was calculated using the retention time per meter of string.

###Capillary Action Testing
####Objective of Experiments
The goal of this experiment was to determine if capillary action is possible using the 0.3 mm Dacron string.
####Experimental Apparatus
Ten 80 inch Dacron strings were used and were double backed so that each strand was 40 inches. The strands were wrapped around a tube in the bottom of the basin and emerged in a water and dye solution. The strings were then draped over a pipe about 5 cm above the surface of the solution and left to hang down over the other side. See **Figure 11.** for the set-up.
<center>
<img src = "https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/CapAct2.JPG?raw=true" height = 200>
<img src = "https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/CapAct.jpg?raw=true" height = 200>
</center>
**Figure 11.** (Left) Bird's eye view of the set-up. (Right) X-Y plane view of set-up

####Procedure
The set-up described in the experimental apparatus was used. A basin was placed on a scale at the bottom of the strings. A timer was started when the dye solution was added into the input basin. Results were noted qualitatively and quantitatively. The migration of the dye was assed with time and weight was to be recorded at the 20 min, 1 hour, and 2 hours marks in the lower basin where water was expected to flow to.

## Results and Analysis
### Single Chain Experiment
**[By simply measuring the mass and length of the chain at a controlled flow rate]** ~~The~~ **[the]** single chain experiment yielded  results of volume of water on the chain, residence time, and height needed for a 15 minute residence time ~~, by simply measuring the mass and length of the chain at a controlled flow rate~~. By dividing the mass on the chain by the density of water, which is 1 g/ml, the volume of water on the chain was obtained. When graphed against flow rate, this calculation yielded a curve best fit by a power series with an R<sup>2</sup> of .991. This is an appropriate result because power series are most often used for data that compares measurements that increase at a specific rate. The flow rate was increased in small increments and the volume of water on the chain would also increase at a specific rate until it reached a certain threshold, which can be seen towards the end of the line graph where the volume of water on the chain starts leveling out as expected.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/FRvsVWC.png?raw=true" width = 300/>

**Figure 12.** The volume of water on the chain when the pump is running at different flow rates (reference manual for code).
</center>

Furthermore, residence time was calculated by dividing the volume of water on the chain (ml) by the flow rate (ml/min) and then converting to seconds. Understanding the residence time of water at different flow rates is important because the optimal residence time is 15 minutes. Again, since the flow rate is increasing in small increments a power series is used for the line of best fit, this time with an R<sup>2</sup> value of .996. Since the residence time drastically decreases as the flow rate increases, it is understood that an actual string digester system made with chains would have to run at low flow rates with really long chains. For example, if it were run at 1.5 ml/min at least a 13.716-meter chain would be needed for the optimal 15-minute residence time, which might be unattainable in some circumstances and the issue of clogging of pipes and tubes comes into play because the flow rate is so low. Thus, other materials may be worth looking into as possible strings in the system that will have better residence time.

<center>
<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/FRvsRT.png?raw=true" width = 300/>

**Figure 13.** The residence time of water on the chain when the pump is running at different flow rates (reference manual for code)
</center>

Another result the experiment supplied was the height of the chain that would be needed for a 15 min residence time at each flow rate. The height needed was calculated by dividing 900 seconds (15 mins) by the residence time(s) by the length of the chain, in this case .9144 meters. Then as seen in **Figure 14.** another line with a power series best fit is yielded this time with a R<sup>2</sup> value of .996. Again, since the flow rate was increased at specific increments and the residence time greatly decreased as the flow rate increased initially and then leveled out **[,]** it follows that the line of best fit for the height needed for a residence time of 15 minutes should start off with a steeper slope and eventually start to become less steep. By running this experiment and calculating the values needed for residence time and height needed we were able to determine that chains may not be the best material to optimize the parameters we want. **[Why not? My guess is that it was what you had stated earlier that the flow is too low, and the length of chain needed is too long but that should be repeated here if that is the case. Also do not use personal pronouns!]

<center>
<img src ="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/FRvsHN.png?raw=true" width=300>

**Figure 14.** The height needed for the chain so that the residence time would be 15 minutes for each different flow rate (reference manual for code)
</center>

### Chain Matrix Experiment
The chain matrix experiment focused more on qualitative results rather than quantitative ones. As the experiment ran it was observed that not all of the chains hanging out of the basin in the matrix contained the same amount and flow rate of water. For this reason it was decided to design a different system to distribute water onto the string material.

### Single Dacron String Experiment
The single dacron string experiment yielded the volume of water on the string, the residence time of that volume of water on the string, and the height needed for a 15 minute residence time.

By dividing the mass on the string by the density of water, which is 1 g/ml, the volume of water on the string was obtained. The flow rate was increased in small increments and the volume of water on the string also increased at a specific rate until it reached a certain threshold. This can be seen on the graph in **Figure 15.** as the curve starts to level out as the change in the volume of water on the string decreases as the flow rate increases.
<center>
<img src ="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/DFRvsVWC.png?raw=true" width=300>

**Figure 15.** The volume of water on the string graphed against the different flow rates (reference manual for code)
</center>

Residence time was calculated by dividing the volume of water on the string (ml) by the flow rate (ml/min) and then converting to seconds. Understanding the residence time of the water on the string at different flow rates is important because time is a constraint in trickling filters. A string digester cannot take too long because it slows the rate of flow the water can come out of the plant at which affects how much wastewater the plant can take in. But, it also cannot run too fast because the bacteria on the string need the right amount of time to actually extract most of the nutrients out of the water. The residence time drastically decreases as the flow rate increases as seen in **Figure 16.**. Thus, it is understood that a string digester would have to run at low flow rates.
<center>
<img src ="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/DFRvsRT.png?raw=true" width=300>

**Figure 16.** The residence time graphed against the different flow rates (reference manual for code)
</center>

The last result the experiment supplied was the height of the string that would be needed for a 15 min residence time at each flow rate. The height needed was calculated by dividing the "optimal" residence time of 15 minutes by the residence time(s)and then  by the length of the chain, in this case .78 meters. **[As]** The flow rate was increased **[and leveled out]** at specific increments ~~and~~ **[,]** the residence time greatly decreased ~~as the flow rate increased initially and then leveled out~~, however the height needed for a 15 minute residence time is almost exactly linear (see **Figure 17.**). The length of string needed for a 15 minute residence time at the lowest flow rate of about .0005 mL/s would only be about 1.97 m. By running this experiment and calculating the values needed for residence time and height needed we were able to determine that strings may be a viable option to optimize the parameters we want. The next step would be to design a dispensing system that could actually deliver water onto the strings at such low flow rates.
<center>
<img src ="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/DFRvsHN.png?raw=true" width=300>

**Figure 17.** The height needed for a 15 minute residence time graphed against the different flow rates (reference manual for code)
</center>

### Capillary Action with Dacron String
This experiment did not go as expected. The red dye only traveled part of the way down the strings (**Figure 18**). No water made it to the end of the strings; therefore, the weight measurements were not useful as they were all constant. The team hypothesizes that this is because the solution of red dye and water had to travel too far and thus dried up too quickly.
<center>
<img src = "https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/capillary2.png?raw=true" height = 200>

**Figure 18.** Red dye on the strings after the test ran for a couple days.
</center>

## Conclusions

The team tested the weight of water on the jack chain at different flow rates using a single chain set-up. From these results, the team was able to determine the amount of water on the chain, the residence time on the chain, and the height needed for a 15 minute residence time. As flow rate increased, the volume of water on the chain and height of chain needed for a 15 minute residence time also increased. The residence time versus flow rate showed a negative correlation. These chains are not a viable option for an AguaClara wastewater treatment plant at this point **[for reasons explained below]**. At the lowest flow rate tested of 1.5 ml/min onto one single chain, the height needed for a 15 min residence time would be 13.7 m. This is about 4.5 stories. Since the goal of AguaClara is to be gravity powered, it would be quite difficult to get water 13.7 m high. In addition, the difficulty the operators would face should they need to fix something in a string digester this high is not realistic. This chain is also not feasible for an ideal string digester as the water flowing down it did not form a uniform sheath but instead flowed down in distinct droplets. This irregular ebb and flow along with a non-uniform sheath make for a system that does not use the entirety of the surface area of the chain. Since the goal of the string digester is to maximize surface area and therefore digestion efficiency, the inefficient spacial chain digester system is not a feasible option at this time.

  Creating a rapid but efficient string digester would be impactful for the future of AguaClara's involvement in wastewater treatment ~~.~~ **[because]** String digesters have the potential to greatly decrease the wastewater processing time and also decrease the organic solutes in the effluent. By maximizing potential surface area for the microbes to grow on using strings and sponges, thereby allowing for more microbial digestion of the water, some traditional trickling filter problems would be solved or minimized. Effluent from the UASB will require further treatment and the team believes that a string digester could provide the necessary treatment with minimal energy requirements.

## Future Work
In the following weeks, the team will test a 0.3mm Dacron string. The team will use micro-tubing with the peristaltic pump to test the same parameters as was tested for the chains. The micro-tubing will allow a much smaller flow rate necessary for the thinner string. In addition, the team will purchase several more strings that are synthetic hydrophilic materials. The team may also test the capillary action abilities of the strings to draw water up at an even slower rate. Further**[more]** , the rate of oxygen diffusion into the string will be calculated to assure that enough can diffuse into the surface of the string to reach the necessary biological oxygen demand (BOD). This BOD is necessary to perform as a successful alternative to a trickling filter and remove organic compounds **[It is necessary to perform BOD? I don't know what this sentence is saying...]** . The future of this team primary relies on finding an appropriate material that will allow for biofilm growth and not be susceptible to degrading.

The team is also looking into using synthetic waste water inoculated with an aerobic bacteria. The team would need to set-up a system of measuring how much organic nutrients the bacteria could remove over the length of the string digester and even just how feasible biofilm growth is on the strings.

## Bibliography
Ali et al. (2017). "Identification and Elucidation of the Designing and Operational Issues of Trickling Filter Systems for Wastewater Treatment." *Polish Journal of Environmental Studies.* 26(6), 2431-2444.

Barnhart, M. M., & Chapman, M. R. (2006). *Curli Biogenesis and Function.* Annual Review of Microbiology, 60(1), 131-147.

*Biofilm Process-2...* (n.d.). Retrieved March 17, 2019, from http://web.deu.edu.tr/atiksu/ana52/biofilm2.html

Donlan, Rodney. (2002). "Biofilms: Microbial Life on Surfaces." *Emerging Infectious Diseases.* Sept. 2002.

Hinton, Steven. David, Stensel. (1991). "Experimental observation of trickling filter hydraulics." *Water Research.* (pp. 1389-139).

Onodera et al. (2014). "Development of a sixth-generation down-flow hanging sponge (DHS) reactor using rigid sponge media for post-treatment of UASB treating municipal sewage." *Bioresource Technology.* 152, 93-100.

Pedersen, Karsten. (1990). "Biofilm development on stainless steel and PCV surfaces in drinking water" *Water Research.* (pp. 239-243).

Rozej et al. (2015). "Structure and microbial diversity of biofilms on different pipe materials of a model drinking water distribution systems." *World Journal of Microbiology and Biotechnology* 31: 37-47.

Ryu, J., Kim, H., Frank, J., & Beuchat, L. (2004). *Attachment and biofilm formation on stainless steel by Escherichia coli O157:H7 as affected by curli production.* Letters in Applied Microbiology, 39(4), 359-362.

Sperling, Marcos von (2007). *Activated Sludge and Aerobic Biofilm Reactors.* (pp. 271-283) London: IWA Publishing.

Spuhler, Dorothee; Eawag (Swiss Federal Institute of Aquatic Science and Technology). *Trickling Filter.*

Tandukar et al. (2005). "A low-cost municipal sewage treatment system with a combination of UASB and the "fourth-generation" downflow hanging sponge reactors." *Water Science Technology.* 52(1-2): 323-329.

# Manual
**[Should include materials list. PVC sheet also needs thickness]
## Fabrication Details
### Fabrication of Chain Matrix Basin
Step 1. Obtain sheets of PVC.
Step 2. Using electrical saw, cut pieces of PVC to desired lengths and widths.
* For longer sides of basin, cut the PVC sheet to 2.5 inches by 2.5 inches.
* For shorter sides of basin, cut the PVC sheet to 1.75 inches by 1.5 inches.

Step 3. Construct the basin in the form of a rectangular prism (no top/roof).
* Use PVC glue and other necessary items to fabricate the shape.

Step 4. Using an electrical drill with drill size 1/16th of an inch, drill 2 rows of 3 holes (6 holes total).
Step 5. Cut 6 desired lengths of jack chain for the basin using wire cutter.
Step 6. Pry open chain link on each chain using plyers and place into a basin hole.

###Fabrication of Capillary Action Basin
Step 1. Obtain sheets of PVC.
Step 2. Using electrical saw, cut pieces of PVC to desired lengths and widths.
* For longer sides of basin, cut the PVC sheet to 2.5 inches by 2.5 inches.
* For shorter sides of basin, cut the PVC sheet to 1.75 inches by 1.5 inches.

Step 3. Construct the basin in the form of a rectangular prism (no top/roof).
* Use PVC glue and other necessary items to fabricate the shape.

Step 4. Glue a PVC bar in the bottom of the center of the basin.
* Make sure it is well within the basin, but not touching the bottom of the basin.

Step 5. Cut 5 lengths of the Dacron string.
Step 6. Fold the lengths in half and then loop around the bar in basin.

## Special Components
### Chain
For the chain in the single-chain and chain-matrix experiments, a stainless steel, 50-foot, size-18, jack chain was used.

Purchasing Link: [Jack Chain](https://www.mcmaster.com/3617T2)

<center>
<img src = "https://github.com/AguaClara/String-Digester/blob/master/Photos/jackchain.jpg?raw=true" width = 300/>

**Figure 19.** The stainless steel jack chain used for the single-chain and chain-matrix experiments.
</center>

### Dacron
For the string used in the single string and capillary action experiments, a synthetic, braided 600-yard Dacron (polyethylene terephthalate) string was used.

Purchasing Link: [Dacron String](https://www.amazon.com/Tuf-Line-Dacron-600-Fishing/dp/B000ALCARK/ref=sr_1_5?keywords=fishing+line+dacron&qid=1555437543&s=gateway&sr=8-5)

<center>
<img src = "https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/Dacron_String_Closeup.jpeg?raw=true" width = 300/>

**Figure 20.** The braided Dacron string used for the single-string and capillary action experiments.
</center>

## Experimental Methods
### Single Chain Experiment
#### Set-up
Step 1. Suspend scale in air using rods for support.
Step 2. Hook the jack chain to the hook on the bottom of the scale.
* Record the length of the chain suspended in air.

Step 3. Place large bucket under the chain to catch dripping water.
Step 4. Balance/Zero the scale
* Make sure chain is as still as possible when zeroing.
* Make sure chain is dry.

Step 5. Set up peristaltic pump with orange/yellow tubing (Tubing ID: 0.05)
* Set desired pumping speed.

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Photos/scale%20string%20set%20up.png?raw=true" width = 300/>

**Figure 21.** Diagram of experimental apparatus for single chain experiment.

</center>

#### Experiment
Step 1. Start the peristaltic pump.
Step 2. Raise the tubing to the very top of the chain, just beneath the scale.
Step 3. Begin observing the scale and wait till scale reading begins to stabilize.
Step 4. Record the range at which the scale reading fluctuates.
Step 5. Repeat experiment as needed with desired pumping speed and desired jack chain length.

#### Cleaning Procedure
Step 1. Turn peristaltic pump off and let chain air-dry.
Step 2. Pour any excess water in bucket down the sink.
Step 3. Remove chain from the scale hook.
Step 4. Put items away as desired.

### Chain Matrix Experiment
#### Set-up
Step 1. Suspend basin in air using rods for support.
Step 2. Hook a jack chain through each hole on the bottom of the basin.
Step 3. Place large bucket under the chain to catch dripping water.
Step 4. Set up peristaltic pump with tubing (Tubing ID: 16)
* Set desired pumping speed.

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Photos/diagram%20for%20chain%20matrix.jpeg?raw=true" width = 300/>

**Figure 22.** Diagram of experimental apparatus for chain matrix experiment.

</center>

#### Experiment
Step 1. Start the peristaltic pump.
Step 2. Place the tubing into the basin.
Step 3. Begin observing the chains and their performance in water retention.
Step 4. Record the observations of the experiment.
Step 5. Repeat experiment as needed with desired pumping speed and desired jack chain length.

#### Cleaning Procedure
Step 1. Turn peristaltic pump off and let chains air-dry.
Step 2. Pour any excess water in bucket down the sink.
Step 3. Remove chains from the basin holes.
Step 4. Put items away as desired.

### Single Dacron String Experiment
#### Set-up
Step 1. Suspend scale in air using rods for support.
Step 2. Cut a length of the Dacron string.
Step 3. Form a loop on one end of the string through a knot.
Step 4. Submerge the string in water to pre-wet.
Step 5. Hook the Dacron string loop to the hook on the bottom of the scale.

* Record the length of the string suspended in air.

Step 6. Place large bucket under the chain to catch dripping water.
Step 7. Set up peristaltic pump with micro-tubing (Tubing: Orange/Yellow)
* Set desired pumping speed.
* Secure the tubing to set-up.

Step 8. Balance/Zero the scale.

* Make sure Dacron string is as still as possible when zeroing.
* Make sure string is pre-wet.

<center>

Refer to **Diagram 21** for experimental apparatus diagram.

</center>

#### Experiment
Step 1. Start the peristaltic pump.
Step 2. Begin observing the scale and wait till scale reading begins to stabilize.
Step 3. Record the range at which the scale reading fluctuates.
Step 4. Repeat experiment as needed with desired pumping speed and desired Dacron string length.

#### Cleaning Procedure
Step 1. Turn peristaltic pump off and let string air-dry.
Step 2. Pour any excess water in bucket down the sink.
Step 3. Remove string from the scale hook.
Step 4. Put items away as desired.

### Capillary Action Experiment
#### Set-up
Step 1. Suspend capillary action basin in air using rods for support.
Step 2. Saturate the Dacron Strings with water, and remove of any excess.
Step 3. Place a PVC pipe 5-10 centimeters to the left or right of the basin and 5-10 centimeters above.
Step 4. Place the strings of the basin over the PVC pipe.
Step 5. Place scale under the strings and zero the scale.
Step 6. Place a measuring cup under the strings and on top of the scale.
* Make sure Dacron string is as still as possible when zeroing.
* Make sure string is pre-wet.

<center>

<img src="https://github.com/AguaClara/String-Digester/blob/master/Spring%202019/Images/Capillary_Action_Diagram.jpeg?raw=true" width = 300/>

**Figure 23.** Diagram of experimental apparatus for capillary action experiment.

</center>

#### Experiment
Step 1. Record the weight on the scale with measuring cup.
Step 2. Place desired amount of water as well as desired amount of dye into the basin.
Step 3. Start a timer with desired unit of time.
Step 4. Monitor experiment as desired and record scale readings at specific times.

#### Cleaning Procedure
Step 1. Remove basin liquid and let strings air-dry.
Step 2. Pour basin liquid in bucket and basin down the sink.
Step 3. Put items away as desired.

## Python Code for Graphs

### Code for Figure 12
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

### Code for Figure 13
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

### Code for Figure 14
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
### Code for Figure 15
``` python
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
```

### Code for Figure 16
```python
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
```

### Code for Figure 17
```python
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
```
