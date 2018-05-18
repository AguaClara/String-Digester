# Trickling Filter, Spring 2018
#### Jillian Whiting, Ben Gassaway, Rosie Krasnoff
#### May 18th, 2018

## Abstract

The trickling filter subteam's objective for this semester was to identify problems with trickling filters and to provide possible solutions to these problems. The long term goal of the team is to create a novel design for a trickling filter that will perform secondary and tertiary treatment on domestic wastewater in a future AguaClara wastewater treatment plant. After an extensive literature review, two bench scale experiments were conducted. The first test aimed to characterize the hydraulic behavior of a trickling filter and the flow of water through its packing media. The team used this information to identify the areas within the system with the greatest potential for improvements. From this information, the first prototype was built using strings to control flow paths and create a high surface area to volume ratio. Preliminary tests were conducted on the prototype to determine flow dispersion, residence time, and optimal string spacing.


## Introduction

The creation of the trickling filter subteam was prompted by the need for further treatment of wastewater following upflow anaerobic sludge blanket (UASB) treatment. A UASB reactor consists of a suspended sludge blanket which settles and treat incoming wastewater. The wastewater enters the reactor from the bottom and flows upward through through the sludge blanket. UASB treatment efficiently treats the biochemical oxygen demand (BOD) of wastewater, but there are also high concentrations of nutrient loading in the domestic wastewater. Wastewater that is not treated can transmit diseases and add nutrients to water systems. Excessive nutrients in water systems can lead to a decrease in dissolved oxygen levels and also cause toxic algal blooms.

A trickling filter is a biological reactor used in secondary and tertiary wastewater treatment to remove BOD and nutrients. Settled wastewater is spread evenly by the distribution arm across the filter media, which can be rocks, gravel, or plastic media, among other things. The filter media is cultured with a productive biofilm which grows on the media and degrades the organic matter and nutrients that come into contact with it as the water trickles through. A conventional trickling filter with a rotating distributor arm can be seen in Figure 1 below.

![Trickling Filter](http://4.bp.blogspot.com/-wG5NGChx52c/TfD3bhROrwI/AAAAAAAAAAY/F4WRhidlWSE/s320/img2-25.gif)

Figure 1: Cross sectional side view of a conventional trickling filter with stone media and a rotating distributor arm.


Trickling filters were heavily researched in the 1970's and 1980's but the industry witnessed a dramatic decline in literature in the years following. The wastewater research after 1980 switched to more energy intensive methods of treatment, like activated sludge, so recent progress in trickling filter technology has been limited in recent decades. These newer processes have a higher removal efficiency, but require massive amounts of energy. One aspects that is central to AguaClara's mission is to use little or no electricity. Therefore, using passive treatment methods that have low energy requirements is a priority, especially in regions where electricity is not available or consistent. The only part of the trickling filter treatment process that requires energy is pumping the wastewater to the top of the filter for distribution, which makes it an ideal technology for situations with limited energy availability.

 The team believes with modern technologies and new information, trickling filters can achieve a high performance level. This can be done by  maximizing the utilization rates of the biofilm surface areas and improving nutrient removal performance for the system. The team strives to make significant technological improvements on industry-standard applications for the system.

Implementation of a non-mechanized trickling filter system such as the one described above would be beneficial to a wastewater treatment plant in terms of economic and operational sustainability. Eliminating the need for any proprietary, mechanized components opens up an opportunity for cost savings and will ultimately extend the usable life of the plant. Any mechanical components added to the system present an additional point of failure. By removing these moving parts, the system will be able to operate for longer with a less-intensive maintenance schedule. This will save money and time in the long run for the plant operations.

The overall objective of this team with respect to the treatment capacity of the system, was to first identify the primary issues in industrial-scale trickling filters. Using this information, the team aims to eventually deploy an efficient, non-mechanized trickling filter which can be adapted to serve the wastewater needs of a resource-scarce community. The team's primary aim is to assess the feasibility of the inclusion of a trickling filter in a future AguaClara wastewater treatment plant.

## Literature Review

#### Trickling Filter Operational Difficulties
There is significant documentation of problems plant operators experience when dealing with trickling filters. Some of the issues, while important to take into consideration when implementing trickling filters, may not offer much room in terms of what improvements the team can make. Such problems include: the development of slug populations in the trickling filters, which can remove the layer of biofilm and harm the nitrifying bacteria population, thereby negatively impacting the systems performance and plug the channels of the system; filter flies, whose presence suggests a lack of moisture throughout the filter; and foul odors, which can indicate an increasing level of anaerobic reactions or accumulating sloughed-off biomass in the filter media. Addressing pest-control issues is not a priority for the team at this time, as there are greater improvements to be made elsewhere.

However, some of these previously mentioned problems (insect and slug presence in filters) as well as high biomass sloughing rate contribute to clogging and ponding in filters, which the team does aim to address. In the context of a trickling filter, sloughing refers to when a layer of the microbial growth loses the ability to stay attached and is shed from the filter media and washed away by water flow. If the layer of biofilm is not maintained at a desired thickness, treatment performance will decrease. Current solutions include flashing with low doses of chlorine to remove deposited solids and kill excess biomass or periodic flooding [(Ali et al. 2017)](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf). The team aims avoid the problem altogether by developing a new trickling media that has a lower tendency to experience clogging or ponding, so that periodic flooding or other solutions are not necessary.


There can be issues with variations in temperature: biofilm thickness changes seasonally and can be low quality and uneven in cold temperatures. In freezing weather, formation of ice can cause clogging and therefore structural damage to the trickling media. These are generally not major concerns for plants in equatorial regions, and so while important to note, will not be a focus for the team at this point.

 Ali et al. states that the most common problem in trickling filters is uncontrolled sloughing, which is often caused by uneven hydraulic loading rates. This can be particularly problematic after storm events when flooding results in very high hydraulic loading. It can also be caused by clogging of the distribution arm and uneven distribution of the influent [(Ali et al. 2017).](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf) There is potential for the development of a much-improved distribution system that could help to alleviate this problem.

 Proper distribution of wastewater onto the filter media is crucial for optimizing efficiency of treatment. The most common method of distribution is rotating distributors, but after seeing the problems with them at the Cayuga Heights wastewater treatment plant (see Case Study section for details), the team was interested in learning more about other methods that might require less maintenance or be less prone to failure.


The less common method of distribution, the fixed distribution system, utilizes lateral and main distribution pipes, which are placed just above the medium, spaced to give uniform distribution of water. They generally have nozzles with a circular hole and a deflector. They are more commonly used with intermittent dosing, so flow from the system varies; it starts at a maximum and lowers as the tank empties. Currently, fixed distribution systems are mostly used in deep filter and biotowers (i.e. very tall filters).


Unfortunately, these systems are also prone to clogging or blockage issues and similarly challenged by inconsistency of hydraulic load on the surface of the trickling filter. This is another area where there is huge potential for the team to increase the productivity of trickling filters. [(Sperling 2007).](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402123.pdf)

### Kinetics

Kinetics are used to model the removal efficiencies of biological plants. The team believes that the best way to improve filter performance is to improve the kinetics of the filter. Therefore below is a literature review of kinetic models and possible solutions to increase removal.

#### BOD Kinetic Model

The trickling filter team assumed that the majority of BOD will be removed by the UASB reactor. Therefore the purpose of the trickling filter will be primarily removing nutrients (i.e. nitrogen and phosphorus). Since there is not a common nutrient removal equation that many books cite, the common BOD model will be used and compared to one paper's nutrient removal equation. Therefore, the team is using the modified Velz BOD kinetic model with the assumption that nutrient removal factors would be similar to BOD removal factors because they are both biological processes. Nutrient removal equations discussed later validate this assumption. The most common kinetic model for trickling filters is the modified Velz Equation.

The modified Velz Equation from [Logan et. al. 1987](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true):

$C_{out} =\frac{C_{in}}{(R+1)e^{\frac{k_{20}A_{s}H\theta^{T-20}}{Q_{i}(R+1)^{n}}}- R}$

Where:
* $C_{out}=$ The $BOD_{5}$ leaving the filter
* $C_{in}=$ The $BOD_{5}$ entering the filter
* $R=$  The recycle ratio defined as the ratio of recirculation flow to the plant influent flow
* $k_{20}=$ The kinetic constant/treatability coefficient
* $A_{s}=$ The specific surface area
* $H=$ The filter height
* $\theta=$ an empirical correction factor typically set equal to 1.035
* $T=$ Temperature in degrees C
* $Q_{i}=$ The flow before recycle divided by filter cross sectional area

The team's preliminary design for the filter would not include any recycle, therefore the equation simplifies to:

$C_{out} ={C_{in}}{e^{\frac{-k_{20}A_{s}H\theta^{T-20}}{Q_{i}^{n}}}}$


The main points of improvement based on the kinetic model would be to change any of the variables in the equation to increase removal (i.e $C_{in} - C_{out}$). These points of improvement are to increase the height/depth of the filter, increase the surface area, increase temperature, or increase the $k_{20}$ value.


#### Increasing Temperature
The teams assumption is that the wastewater treatment plants would be built outside without heating or air conditioning. Since the pilot plant is expected to be installed in Honduras, temperature in the filter will be in the optimal range for bacterial growth. Although the kinetic model does not have a cap on temperature, the team does not want to raise the temperature too high as to kill the bacteria. The team did not investigate other heating mechanisms because heating large volumes usually requires a lot of energy, for little payoff.


#### Increasing Height of filter
The team is looking for a novel design that can make traditional filters more cost-effective. The team does not believe that there is a lot of room for improvement in just changing the height of the filter. This is because increasing height of the filter increases the cost of production exponentially. Therefore the team did not investigate this further.

#### Increasing the Specific Surface Area
Specific surface area is surface area per volume. In order to change the specific surface area of the filter the packing material must be changed. To increase specific surface area, the packing material must have more surface area for the same amount of volume. Many trickling filters in Honduras, the packing material is gravel or rocks. In the United States, there has been a lot of research and development of new higher specific surface area packing materials. These materials have a more honeycomb structure. Many of these materials are very expensive and would not fit with AguaClara low-cost model. Even though using these materials would not be feasible, the team can gain insight into how to make a more efficient filter and then make it low cost. Therefore the team thinks this is a good research area to produce an effective trickling filter.


##### Ideas for improvement
The team's idea for improvement of specific surface area would be a novel geometry and material combination. Possible ideas include using string, straws, sheets, BioBalls, and six-pack plastic holder recycling

#### Increasing the $k_{20}$ Value
The $k_{20}$ value is the reaction rate constant of degradation at 20 degrees Celsius. A higher value means that more nutrients or BOD is consumed per day. There is a very little available research on $k_{20}$ values of different trickling filters. Most research reports just state the value for the filters they were testing. A reasonable $k_{20}$ value for an aerobic sludge reactor would be 0.20. One of the factors that effects the value is the type of bacteria used and how they are suite to the environment.

##### Ideas for improvement
* Using different bacterial cultures that are more effective at removing nitrogen and phosphorus to grow on the filter. Most filters use natural inoculation (i.e. what grows when wastewater is run through the filter). Research would need to be conducted on if controlled inoculation could be done for a selected culture, and if it would be sustainable throughout the lifetime of the filter.
* Ensuring that aeration is uniform and effective at all points of the filter media, maintaining a high performance of microbial treatment

#### Flow Distributions
An assumption of the modified Velz model is that the entire volume of the trickling filter is being used. The team hypothesized that there might be unused volume in the trickling filter that does not receive any flow because the water would take another path with less resistance, and therefore the system would be failing to fully treat the water. Therefore the team conducted preliminary experiments to determine how flow is distributed. Using the information gathered from these tests, the team intends to eventually determine how to use a packing material and filter design that utilizes all of the available space.


### Nitrogen Kinetic Models
The EPA has complied information from many trickling filters across the US that are used for nitrification. They found that bacteria that preform nitrification, usually Nitrosomonas and Nitrobacter, cannot compete against the BOD removing heterotrophs when the BOD levels are high. The EPA suggests that BOD levels be below $20 \frac{mg}{L}$, with the optimal value of $10 \frac{mg}{L}$. The chemical reactions that the nitrifying bacteria are performing are:

$NH_{4}^{+}  + 1.5 O_{2} \rightarrow NO_{2}^{-} + 2H^{+} +  H_{2}O$

$NO_{2}^{-}  + 0.5 O_{2} \rightarrow NO_{3}^{-}$.

When the EPA report was written no kinetic model had been derived for nitrification in trickling filters. However, they found four main parameters that increased removal was based on: low organic loadings, high residence times, sufficient oxygen availability, and consistency in hydraulic, organic, and ammonia loadings [(US EPA, 1991)](https://nepis.epa.gov/Exe/ZyPDF.cgi/P1004T3S.PDF?Dockey=P1004T3S.PDF). [Duddles et. al., 1974](https://www.jstor.org/stable/pdf/25038735.pdf?refreqid=excelsior%3A134b4fcdcce29130f630db8059aa3119) found that nitrification rate is directly proportional to specific surface area. [Gullicks and Cleasby, 1986](http://www.jstor.org/stable/pdf/25042842.pdf?refreqid=excelsior%3Ad9da82b9b851c3d02a23339cd5f0f45d) found that the mass transfer rate of the biofilm can be increased in two ways: increasing temperature and increasing ammonia concentration. Based on these reports, the team's earlier assumption that parameters affecting BOD removal are similar to those affecting nitrification is valid. The team also found another factor that effected nitrification rate: oxygen availability [(Okey and Albertson 1989)](http://www.jstor.org/stable/25046965). There are two regimes of the nitrogen kinetic equation. When oxygen is limited, it is a zero-order kinetic model with respect to ammonia and half order with respect to oxygen. When oxygen is plentiful, it is a first order model with respect to ammonia. The removal equation found was as:


$\left(NH_{4}-N\right)_{R} = \frac{K_{ao}S_{o}^{0.5}A_{trans}}{Q} + \left(NH_{4}-N\right)_{trans}\left(1-e^{-K_{n}L}\right)$
* $\left(NH_{4}-N\right)_{R} = NH_{4}-N$ concentration removed, $\frac{g}{m^{3}}$
* $S_{o} =$ bulk phase oxygen concentration, $\frac{g}{m^{3}}$
* $K_{ao} =$ constant that contains diffusivity of and stoichiometric requirement for oxygen, $\frac{g^{0.5}d}{m^{0.5}}$
  - $K_{ao,max} = 3.8$
* $A_{trans} =$ Media surface to transition, $m^{2}$
* $Q =$ flow rate, $\frac{m^{3}}{d}$
* $\left(NH_{4}-N\right)_{trans} =$ The $NH_{4}-N$ concentration at the transition from oxygen control to $NH_{4}-N$ control, $\frac{g}{m^{3}}$
* $K_{n} =$ first-order constant, $m^{-1}$
* $L =$ first order depth term, $m$

Therefore, compared to the BOD kinetic model, the only additional parameter is oxygen concentration. Higher oxygen concentrations result in higher removals.


#### Ideas for improvements
The team incorporated the need for airflow into their brainstorming of a novel geometry. In developing this novel geometry, the spacing between each string should prevent any unwanted cohesive interactions between water particles to allow for sufficient biofilm aeration per string. To optimize this spacing between strings, each was modeled as a cylinder to account for the predicted surface tension effects that would be observed during treatment. Surface tension in a cylinder can be calculated using the following equation:

$F_{ST} = \pi\lambda D$

where $D$ is the diameter of the cylinder. Surface tension can be looked up in table for different materials, and the minimum diameter needed to overcome it would be when this force balances with gravitational force.


## Design Parameters

### Factors to Consider in Designing Physical Facilities

1. Type and physical characteristics of packing material
2. Dosing rate
3. Dosing characteristics for distribution system
4. Configuration of underdrain system
5. Ventilation through either natural or forced airflow
6. Settling tank designs for the effluent


### Packing Media

The ideal packing material for a trickling filter has a high surface area-to-volume ratio. Factors which add to the value of an ideal packing media are: its durability, its affordability, and its ability to both promote air circulation and prevent clogs in the system.

Plastic packing, for example, has the advantage over rock-based packing for its ability to operate at higher organic loading rates. Due to the characteristics of the media, the trickling filters can be much taller.

Table 1: Properties of various packing materials
| Material |Nominal Size (cm) |Surface Area (m^2/m^3)| Void Space (%) | Application |
| --- | --- | --- | --- | --- |--- | --- |
|  Rock (small)   |   2.5-7.5  |  60   |  50   |  N   |
|  Rock (large)  |  10-13   |   45  |  60   |   C, CN, N  |
|  Plastic -- Conventional   |   61 x 61 x 122  |   90  |  >95   |   C, CN, N  |
|  Plastic -- High Specific Surface Area  |  61 x 61 x 122   |   140  |   >94  |  N   |
|  Plastic random packing - conventional   |  Varies   |   98  |   80  |   C, CN, N  |
|  Plastic random packing - high specific surface area   |  Varies   |   150  |  70   |  N   |
######C = BOD Removal; N = Tertiary Nitrification; CN = Combined BOD and Nitrification

### Dosing Rate

The dosing rate of a trickling filter is defined as the depth of liquid discharged on top of the packing for each pass of the distributor (Tchobanoglous et. al. 2003, pp 898). To achieve the desired flow rate, plant operators can change a number of control points in the system. Firstly, the locations of some existing orifices can be reversed to the front of the distributor arm, which would slow the rotational velocity of the dosing arm by pushing against the propulsion jet from the rear orifices. An alternative to this would be to add reversed deflectors to existing orifice discharges. The most energy-intensive alternative to dosing control is to include a variable-speed electric driver to the rotating distributor arm.


If a high dosing rate is set in order to maintain a thick biofilm in the filter media, then the efficacy of treatment may see a sharp decrease in performance due to a reduction in contact time between the water flowing through the system and the packing media. The flow rate is unique to each packing media and geometry of the filter structure. This will be calculated on a case-by-case basis depending on the treatment regulatory requirements of the area and the size of the filter needed for a given community. A daily intermittent high-flow dose is applied to the system, known as the "flushing dose". The flushing dose is used to control the thickness of the biofilm and any remaining solids in the system.

$n = \frac{(1 + R)(q)(10^3 mm/m)}{(A)(DR)(60 min/h)}$

* $\small n$ = rotational speed, rev/min
* $\small q$ = influent applied hydraulic loading rate, $\scriptsize\textrm{m^3/m^2*h}$
* $\small R$ = recycle ratio
* $\small A$ = number of arms in rotary distributor assembly
* $\small DR$ = dosing rate, mm/pass of distributor arm

Table 2: Typical flushing and operating doses for various BOD loadings
| BOD Loading, kg/m^3 $\cdot$ d |Operating Dose, mm/pass |Flushing Dose, mm/pass|
| --- | --- | --- |
|0.25 |   10-30  |  	$\small\geq$ 200   |
|  0.5  |  15-45   |   $\small\geq$ 200  |
| 1.00   |   30-90  |  $\small\geq$ 300  |
|  2.00 |  40-120   |  $\small\geq$ 400  |
|  3.00   |  60-180   |  $\small\geq$ 600  |
|  4.00   |  80-240   |  $\small\geq$ 800  |


#### Ideas for Improvements

One of the primary failure modes of a trickling filter system involves complications with the mechanized components, especially those in the distribution system. The rotational velocity of the arms is usually driven by hydraulic propulsion, which may not apply the optimal dosing rate due to a lack of sub-metering in the distributor. In other words, the application of water across the media is largely left up to a rough approximation.

As the rotary arms dose water to the system, there is a non-uniform distribution across the filter media. This is an immediate source of efficiency losses since the biofilm can only treat the water in which it comes in contact with. Additionally, the dosing ports in the arms have a tendency to become clogged with miscellaneous debris which may have been missed by the primary clarification process. Most plants do not have sub-metering within the arms to measure the volumetric flow distribution of wastewater being dosed to the system.

An area for improvement is to completely forgo the mechanical distribution system, and to design a reliable distributor which can dose wastewater uniformly across the media. The most valuable modification to the distributor would be the ability to have full control over the dosing rates at any given moment.

### Ventilation and Aeration

#### Natural Draft
The driving force behind natural airflow is derived from a temperature gradient between the ambient air temperature and the temperature within the pores of the media material. An equation from (Schroeder and Tchobanoglous, 1976):

$D_{air} = 353(\frac{1}{T_c} - \frac{1}{T_h})Z$

* $\small D_{air}$ = natural air draft, mm of water
* $\small T_c$ = cold temperature, K
* $\small T_h$ = hot temperature, K
* $\small Z$ = height of filter, m

The team's trickling filter design will strive to employ a naturally aerated system. The industry-standard for natural aeration or "natural draft" is to use a temperature gradient between the filter media and the ambient air temperature to provide a flow of air. This will prevent the need to mechanically aerate with fans or other air pumps, to prevent excess use of electricity. To achieve natural draft, the following criteria are required (Tchobanoglous et. al. 2003, pp 903):

1. The drainage and collection channels must not flow any greater than halfway full in order to permit air flow throughout the system.
2. Access ports with adequate openings should be implemented at both tremendous.
3. Open areas of the underdrain blocks (top slots) should be no less than 15% of the overall cross-sectional area of the filter.
4. A ratio of 10 $\small ft^2$/250 $\small ft^2$ (open grating area/filter area) should be provided in the design.


## Case Study: Cayuga Heights Trickling Filter Observations
The team visited the Cayuga Heights wastewater treatment plant and observed a trickling filter first-hand. It was a very informative visit, and the team was dismayed at the state of the plant and the many issues it was experiencing, especially with the trickling filters. There were two trickling filters at the plant, both of which had substantial debris (clumps of organic material, trash) on top of filter (see Figure 2). The plant manager suggested that this was likely due to the failure of the bar screen that should have removed such debris immediately when the water initially entered the plant. The team also noticed issues with the settling tanks, which the wastewater travels through immediately before the trickling filters. It's possible that the inefficiency of the settling tanks resulted in waste that should have settled out continuing through the system to the trickling filters.

![Figure 2](https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/CHFT%20filter%20surface.jpg?raw=true)
Figure 2: The surface of the trickling filter with significant debris and discoloration.


The team also observed that the distribution arms were failing to cover the surface of the filter with wastewater. Because of this, there was a significant portion of the tank's surface that was getting little to no water on it (see Figure 3). The regions that were most noticeably dry were the edges of the tank and an area a couple feet from the center of the base of the distributor arms. There was also a pattern of discoloration on the top of the filter, which seemed to be caused by the substantial organic matter coming through with the wastewater. This discoloration suggests that even the portion of the filter’s surface that was getting watered was not getting watered equally, and that there was build up of the organic matter on top of the filter where the flow rate was higher (see Figure 2).


![Figure 3](https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/CHTF%20distribution%20arm.png?raw=true)
Figure 3: Distribution arms failed to entirely cover the surface of the trickling filter and there was leakage from the base in the center.

There was leakage from the base of the distributor arm on both trickling filters. One had very substantial leakage and a significant fraction of the wastewater was just spraying out of the center to only a foot or two away. The plant manager said that the seal connecting the pipe and distributor arm had broken and was going to be replaced. The two filters operating in parallel made it possible for the plant to still operate while under maintenance, but it isn't always true that a system uses two filters, and often plants use recycle flow instead of having multiple filters. Due to the major leak, the volume of water going through the filter in the area around the base of the distributor arm was extremely high. Because of that high hydraulic loading, the team would expect that the level of treatment for that wastewater is very low, if not non-existent. This is obviously a big concern and emphasizes the importance of having a robust distribution system that will keep flow even across the filter surface and has safeguards against failure.

The team’s visit to the wastewater treatment plant was  valuable in that it confirmed several of the potential issues documented in the literature. It also made it clear that there is tremendous room for innovation and improvement of trickling filter technology.


## Methods

### Benchtop Experiment: Mapping Flow Through Packing Media

In order to understand the flow patterns in a trickling filter, the team set up a benchtop model to run clean water through. The bench top model was constructed with a 6 inch inner diameter acrylic PVC pipe, as shown in the schematic below (Figure 4).

<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/flow_schematic_front.png?raw=true" height=400 width=250>

Figure 4: This is a schematic of the testing structure. It is an acrylic PVC pipe with holes drills at distances of 5,10,20,40,60, and 80 cm from the top. These holes represent the depths of the filter media that we will be testing. Rods are inserted at the depth of testing to support a mesh which holds the filter media. Water flows from the dosing point through the filter media to the collection unit. The collection unit is held in place by a PVC pipe.


The PVC pipe could be filled to different heights of gravel to test how flow disperses as a function of depth. The team's hypothesis is that the flow will spread out as depth increases.

<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/Gravel_support_top view.png?raw=true" height=300 width=250>

Figure 5: This schematic shows the top view of the support structure for the filter media. There is a mesh which is held up by two rods. The rods go through the PVC pipe and are tightened in place by bolts.

<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/Collection_basin_top.png?raw=true" height=300 width=300>

Figure 6: This schematic shows the top view of the collection unit for the team's experiments.The squares represent cuvettes which are held in by velcro to a PVC sheet. The amount of water collected in each cuvette is recorded to determine how much water is flowing where.


This is the collection basin which will be used to map where the water is exiting the model filter. A photograph of the apparatus can be seen in Figure 7. The water will flow in from a dosing point at the top of the filter and if it spreads out as it travels down the system it will flow into many different cuvettes. This can be then used to create heat map, or more accurately a flow map, to determine what areas are being utilized.

After a few experiments, the team found that water was dripping only from the rods and down the side of the PVC. Therefore they removed the rods and placed the mesh directly on top of the collection basin.

The procedure for a test was to first wet the surface of the rocks. This meant flowing water through at a high rate and not draining the bottom until the entire column was wet. The water was then drained to gravity potential. Once the gravel was wet, a short pulse of 50 mL of water was added. For cuvettes that had water in them, the depth of water in millimeters was measured by inserting a marked straw, so water depth is relative and has no units. However, in many of the preliminary tests until the correct amount of water was determined, the cuvettes overflowed and the data was compromised. For tests where the water overflowed, the team still recorded whether a cuvette had been "hit", i.e. had water in it.


The team also varied the packing material, also performing tests using marbles. The team choose marbles because they are only slightly larger than the pea gravel, but are uniform in size.

Table 3: Summary of Benchtop Experiment Trials
| Trial | Packing Material | Depth |
|:----- |:---------------- | ----- |
| 1     | Wet Rocks        | 10    |
| 2     | Wet Rocks        | 100   |
| 3     | Marbles          | 15    |
| 4     | Dry Rocks        | 15    |
| 5     | Wetted Rocks     | 15    |



## Results and Analysis

In the first test, the team ran the pulse of water from the center of the column through the 5 cm rock depth. The team hypothesized that since this was such a thin layer, the water would exit nearly exactly where it came in. The team actually observed that almost all the water ended up on the walls of the apparatuses and only 4 cuvettes had water in them. There could be multiple reasons for this result:
1. Since the rocks are multiple sizes they fit together in a such a way that the water would prefer to flow sideways instead of down. Then, when the water came in contact with the wall it became attached and never came unattached.
2. The water hit the mesh at the bottom of the apparatus and it was angled so that water flowed to the edges on the mesh before falling into the collection basin. The team conducted this test multiple times at multiple depths to reveal the same results.


<img src="https://user-images.githubusercontent.com/35943730/38639368-ea56bc0a-3d9e-11e8-998e-6c4cebaf9ec2.JPG">
Figure 7: An example of a test run through 60 cm of pea gravel. The image shows that a few of the cuvettes were "hit" and contain water, but most are empty and the vast majority of the water ended up outside the cuvettes, in the bottom of the collection unit.


The team then compared how packing material affects flow. One parameter that was tested was the randomness of the media, marbles of all the same size make a predictable matrix, whereas rocks can form many arrangements. Another parameter that was tested was if wetness of the surface affected flow. Water is very cohesive. In a dry rock, the first path that becomes wet could "pull in" more flow. In a wet rocks all of the rocks have water so there is no preferential flow do to cohesion. From water volume data from each test a heat map was made. Since the measurement was in height of water based on markings, the exact values in the heat maps do not have a physical meeting, but the scale represents differences between cuvettes. All tests were dosed in the middle of the apparatus.

![Marbles](https://github.com/AguaClara/Trickling-Filter/blob/master/marbles.png?raw=true)

Figure 8: The flow of water through marbles is very consistent. The water was dosed in the middle and the highest values are in the middle. Then some flow was diverted to the outside where the depth of water recorded decreases with distance to the center.

![Wet Rocks](https://github.com/AguaClara/Trickling-Filter/blob/master/rocks_wet.png?raw=true)

Figure 9: In the experiment with wet rocks, a somewhat random dispersion is recorded. The highest volume areas are not grouped together.

![Dry Rocks](https://github.com/AguaClara/Trickling-Filter/blob/master/rocks_dry.png?raw=true)

Figure 10: The dry rocks show almost no dispersion with the center cell having double the water volume of any other cells. The rest of the flow was uniform and more similar to the marbles than wet rocks.

Table 4: Total water volume from bench-scale experiment
| Trial     | Total Water Depth Captured |
|:--------- |:-------------------------- |
| Marbles   | 144                        |
| Wet Rocks | 100.35                     |
| Dry Rocks | 70.75                      |

These experiments show the differences in flow that can exist in a trickling filter.  Marbles had the most predictable flow and almost all of the flow ended up in the basin. There is a large difference in water captured by the wet rocks and dry rocks, this is most likely because some water attached to the dry rocks and did not make it out the bottom. The difference between the wet rocks and marble is due to water that made it to the side of the container and ran down the outside. The dry rocks followed the earlier hypothesis that the first path that was wetted would be the preferential flow path. One reason the wet rocks preformed so randomly is that the rocks lock together to form almost a sheet which spread the water over the whole area. This is good to make sure that all areas of the filter are being used and increases retention time. However, this layer that is hard for water to pass through can creating pooling on top of it in the filter which less to anoxic conditions. This experiment highlighted for the team some of the intricacies of packing material selection. The mesh at the bottom of the apparatus that held up the packing materials could have impacted the results if water ran along it.


### Benchtop Experiment: Testing Unconventional Filter Media--Strings Applications

The team decided to pursue an entirely novel preliminary design for a trickling filter in order to investigate options to optimize the surface area to volume ratio of the packing media to both improve the overall treatment efficiency of the system and to decrease the physical footprint of the filter. The first innovation to improve trickling filter media was the use of strings as the packing media and an overflowing basin to wick the water across the length of the string as it was treated.

<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/StringApparatus.png?raw=true" height=550 width=600>
Figure 11: Schematic of experimental apparatus used to flow water across strings during proof-of-concept trials


<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/string%20filter%20set%20up.png?raw=true" height=711 width=400>

Figure 12: Set up of string filter, with holding basin at the top (currently being dosed from above) and yarn/string wrapped around the top of the basin to the bar below. In this picture the system has 46 strings coming from the basin (string was wrapped around 46 times).



The team's initial goal was simply to test if the system would behave as expected: will the water flow over the edges of the basin and flow along the strings until the flow reaches the bottom? The stipulation of this question that would indicate success in the experiment was whether or not the water would consistently prefer the strings as opposed to dripping along the wall of the basin or elsewhere. Several trials were conducted simply dosing the basin with a low flow rate and observing. With the strings packed tightly as shown in the initial set up above in Figure 12, the water that overflowed from the basin followed the string all the way down. This provided confirmation that the concept of using strings as the tickling media has the potential to be successful. Next, the team began testing to target various parameters of the design.

## Results and Analysis
The first set of tests conducted aimed to identify whether residence time of the water on the string depends on the flow rate being pumped into the basin. This test was conducted by starting with red dye in the basin so that the speed of the water moving down the string could be observed visually and timed. One team member began dosing the basin with clean water, and another team member watched the strings and began timing when the water first started to overflow from the basin. The timer was stopped when the first drops of dyed water reached the bottom of the strings. The table below presents the data gathered in these tests.

Table 5: Residence time of water on the string for varying flow rates. All tests conducted with size 17 tubing.
| Flow rate (rpm) | Length of Trial 1 (secs)   | Length of Trial 2 (secs)    | Length of Trial 3 (secs)    | Average Trial Length (secs) |
|:------: |:-------: |:--------: |:--------: |:-------: |
| 25 | 27 | 42 | 47  | 38.67    |
| 50 | 28 | 31 | 29  | 29.33    |
| 75 | 21 | 23 | 24  | 22.67    |

Based on these tests, the team is able to conclude that the residence time of water does depend on the flow rate, and that as the dosing rate is increased, the residence time decreases. Therefore, in order to maximize the amount of time wastewater spends on the string to allow for as much treatment as possible, the design would require a very low dosing rate.

The next parameter the team aimed to test was string spacing. Specifically, the team wanted to know how far apart the strings could be placed before the system fails and water no longer follows along the string, therefore not being treated. The same process of running water through the system was repeated, but with each trial the spacing between the strings was increased by reducing the number of strings coming from the basin. See figure Y below for an example of a test with increased spacing.


<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/10%20strings%20spacing.png?raw=true" height=711 width=400>

Figure 13: String filter set up with 10 strings to test effects of increased spacing.

Tests were conducted at 35 rpm, and the number of strings was gradually reduced from 46, to 20, then to 15, 10, 8, 6, 5, 3, and finally 1 (tests were conducted both with the one string in the center of the basin and at one end). For all tests, the flow of water followed the string and did not flow freely down the side of the basin or fall off the string. Only when the flow rate was increased to 60 rpm with one string did the system begin to fail and water dripped down the side of the basin. From this series of tests, the team can conclude that spacing is not a limiting factor on design and therefore the number of strings in the filter will be determined by other factors like maximizing treatment and allowing for sufficient aeration.

Finally, the team wanted to test the feasibility of an idea of having some strings anchored at an angle away from basin, not straight below it like previous set-ups. To model this, every other string was hung across a thin bar, which separated half the strings outward, thus creating two layers of strings cascading from either side of the basin (see figure 14). The team conducted the same procedure of injecting red dye and observing the flow. For the alternative anchoring set up, the flow was much less uniform than in previous tests. A higher flow of water was observed on the strings that were anchored so that they rested against the side of the basin. Also, some of the water that flowed along the outer set of strings would stay on the thin bar and drip off instead of following the strings all the way down.

<img src="https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/split%20anchoring.png?raw=true" height=400 width=400>

Figure 14: String filter with alternating strings anchored away from the wall of the basin.

Based on these preliminary tests, the team concludes that the benefits of additional anchoring points (a potential to pack more strings into the filter without causing aerobic conditions) do not outweigh the various complications that this additional parameter would introduce. Therefore, the team would suggest focusing on other ways to maximize treatment in the future and stay with one anchoring point directly under the edge of the basin.


## Conclusion

In the team’s initial research, extensive information has been gathered on the operational difficulties, the kinetics, and typical design parameters of trickling filters. Many of the issues plant operators encounter with trickling filters, like clogging and ponding, lack of moisture in parts of the filter, and generally inefficiency of the filter can be addressed by improving two aspects of the filter: the filter media itself and the distribution system. The BOD kinetic model also supports improving the filter media to increase the specific surface area, using alternative materials instead of the traditional rocks or gravel. The team’s research on nitrogen kinetics adds a need for proper aeration of the filter to the list of considerations when designing a new filter media.

The lack of available information and limited research on some aspects of the kinetic model, $k_{20}$ values for example, motivate the team to potentially do lab tests and calculate $k_{20}$ values for various media and try to find a more standardized model than what is found in the existing literature. Similarly, the team flow mapping test attempted to address and challenge the assumption made by the current kinetic model that the entire volume of the filter is being used by looking at the flow distribution.

Preliminary research was driven primarily by industry research, however, it is expected than many of the established parameters will be subject to change as a result of independent research efforts. The findings of the team's experiments are intended to characterize a trickling filter system absent of mechanical components and with higher filter media utilization. By the conclusion of this team's work, a vast majority of the gaps in literature should be filled with conclusive empirical data to serve as a model for wastewater plants in resource-scarce locations in addition to modifying the faults in industry around the world.

The team fabricated the bench top model for flow mapping and conducted tests to determine the distribution of flow in trickling filters with small rock and marble media. The preliminary results from these tests were confusing, as almost all water was running down the side of the tube instead of through the media. The second phase of testing yielded usable results. From this experiment, the team believes that a uniform packing material is better than a random material. It yields consistent results and since it is easy to determine the dispersion and location of the flow the filter can be designed to maximize removal based on that flow. The random filter does spread out the water well; however, it is nearly impossible to model and can create anoxic zones which would limit nutrient removal.

## Future Work
This semesters accomplishments were mostly in the hydraulics of the system. Tasks for future teams should include two main components: biological growth and scaling. The current prototype is very different from traditional filters and it is unknown how a biofilm will grow on it. One important parameter about growth to consider in this design is sloughing. One possible issue is the biofilm that sloughs off also takes all the biofilm on the string below it off. Another task is to determine if the biofilm should be grown just based on what is in the wastewater or if it should be seeded. If it is to be seeded, the future team should determine what the best culture is for nutrient removal. Once the team has both a proof of hydraulic concept and biological concept, they can move on to scaling.  The team must consider how this will be assembled at a large scale. Each side where there is overflow must be completely level. To scale up to a plant size this would cover about an entire classroom. This is a lot of strings and assembly could prove too difficult. Once a scaled design is complete, a small-scale test at the Ithaca WWTP can prove that is can remove nutrients before it is deployed in Honduras.


## Bibliography
Ali et al. (2017). Identification and Elucidation of the Designing and Operational Issues of Trickling Filter Systems for Wastewater Treatment. *Polish Journal of Environmental Studies.* 26(6), 2431-2444.

Duddles, G. A., Richardson, S. E., & Barth, E. F. (1974). *Plastic-Medium Trickling Filters for Biological Nitrogen Control*. Journal (Water Pollution Control Federation), 46(5), 937–946.

Gullicks, H. A., & Cleasby, J. L. (1986). *Design of Trickling Filter Nitrification Towers*. Journal (Water Pollution Control Federation), 58(1), 60–67.

Logan, B. E., Hermanowicz, S. W., & Parker, D. S. (1987). *A Fundamental Model for Trickling Filter Process Design*. Journal (Water Pollution Control Federation), 59(12), 1029–1042.

Okey, R. W., & Albertson, O. E. (1989). *Diffusion’s Role in Regulating Rate and Masking Temperature Effects in Fixed-Film Nitrification*. Journal (Water Pollution Control Federation), 61(4), 500–509.

Sperling, Marcos von (2007). *Activated Sludge and Aerobic Biofilm Reactors.* (pp. 271-283) London: IWA Publishing.

Tchobanoglous, G., F. Burton, H. D. Stensel (2003). *Wastewater Engineering: Treatment and Reuse*. New York, NY: McGraw-Hill.

United States Environmental Protection Agency. (1991, May). *Assessment of Single-Stage Trickling Filter Nitrification*. Office of Water.


```python
# To convert the document from markdown to pdf
pandoc Name_of_this_file.md -o TeamName_Research_Report.pdf
```
