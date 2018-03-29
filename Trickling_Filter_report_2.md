# Trickling Filter, Spring 2018
#### Jillian Whiting, Ben Gassaway, Rosie Krasnoff
#### March 9th, 2018

## Abstract

This was the first semester of a trickling filter subteam, therefore the direction of the team's research was derived independently. The goals for this semester were to identify problems with trickling filters in industry whilst developing robust kinematic models such to enable future subteams to employ novel trickling filter applications. This semester was expected to be driven primarily by literature research, but the team has begun construction for a benchtop experiment in preliminary hydraulic modeling through the filter media.

## Introduction

The creation of the trickling filter subteam was prompted by the need for further treatment of wastewater following UASB treatment. UASB treatment can do very well treating BOD, but there is a lot of nutrient pollution in the wastewater in Honduras. The overall objective is to first identify the primary issues in industrial-scale trickling filters. Using this information, the team aims to deploy both a disruptively efficient, non-mechanized trickling filter which can be adapted to serve the wastewater needs of a resource-scarce community. The team's primary aim is to assess the feasibility of the inclusion of a trickling filter in a future AguaClara wastewater treatment plant.

Trickling filter research was heavily researched in the 1970's and 1980's but this industry witnessed a dramatic decline in literature in the years following. The wastewater research switched to more active methods of treatment like activated sludge; however, passive treatments like trickling filters have low energy requirements, if any. A driving force behind the investigation of trickling filter research is to find ways that align with the mission of achieving hydraulically-driven systems which will be much more feasible in areas of the world in which capital expenditure is a major barrier for employing this technology.

In terms of nutrient pollution control there is little research on trickling filters as the interest in nutrient removal research peaked after interest in trickling filters. The team believes that there is still a lot of progress to be made in trickling filter research, especially in maximizing the utilization rates of the biofilm surface areas. The team strives to make significant technological improvements on industry-standard applications for the system.

## Literature Review

#### Trickling Filter Operational Difficulties
There is significant documentation of problems plant operators experienced when dealing with trickling filters. Some of the issues, while important to take into consideration when implementing trickling filters, may not offer much room in terms of what improvements the team can make. Problems include: the development of slug populations in the trickling filters, which can remove the layer of biofilm and harm the nitrifying bacteria population, thereby negatively impacting the systems performance and plug the channels of the system; filter flies, whose presence suggests a lack of moisture throughout the filter; and foul odors, which can indicate an increasing level of anaerobic reactions or accumulating sloughed-off biomass in the filter media.

Some of these previously mentioned problems (biomass sloughing and insect and slug presence in filters) contribute to clogging and ponding in filters. Current solutions include “flashing with low doses of chlorine to remove deposited solids and kill excess biomass” or periodic flooding. The team aims to address these issues by developing a new trickling media that has a lower tendency to experience clogging or ponding.

There can be issues with variations in temperature: biofilm thickness changes seasonally and can be low quality and uneven in cold temperatures. In freezing weather, formation of ice can cause clogging and therefore structural damage to the trickling media. These are probably not major concerns for plants in equatorial regions, and so while important to note, will not be a focus for the team at this point.

 Ali et al. states that the most common problem in trickling filters is uncontrolled sloughing, which is often caused by uneven hydraulic loading rates. This can be particularly problematic after storm events when flooding results in very high hydraulic loading. It can also be caused by clogging and uneven distribution of the influent [(Ali et al. 2017).](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf) There is potential for the development of a much-improved distribution system that could help to alleviate this problem.

 Proper distribution is crucial and can optimize efficiency of treatment. The most common method of distribution is rotating distributors, but after seeing the problems with them at the Cayuga Heights wastewater treatment plant (see Case Study section for details), the team was interested in learning more about other methods that might require less maintenance or be less prone to failure.

The less common method of distribution, the fixed distribution systems, utilizes lateral and main distribution pipes, which are placed just above the medium, spaced to give uniform distribution of water. They generally have nozzles with a circular hole and a deflector. They are more commonly used with intermittent dosing, and so flow from the system varies; it starts at a maximum and lowers as the tank empties. Currently, fixed distribution systems are mostly used in deep filter and biotowers.

Unfortunately, these systems are also prone to clogging or blockage issues and similarly challenged by inconsistency of hydraulic load on the surface of the trickling filter. This is another area where there is huge potential for the team to increase the productivity of trickling filters. [(Sperling 2007).](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402123.pdf)

### Kinetics
### BOD Kinetic Model
 The assumptions of the trickling filter team is that the majority of BOD will be removed by the UASB reactor. Therefore the trickling filter will be mostly removing nutrients (i.e. Nitrogen and Phosphorus). The team could not find consistent literature on a kinetic model for the removal of nitrogen or phosphorus. Therefore, we are using a common BOD kinetic model with the assumption that nutrient removal would be proportional to BOD removal. The most common kinetic model for trickling filters is the modified Velz Equation.

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

The main points of improvement based on the kinetic model would be to increase the height/depth of the filter, increase the surface area, increase temperature, or increase the $k_{20}$ value.

#### Increasing Temperature
The teams assumption is that the wastewater treatment plants would be built outside without heating or air conditioning. Separately using an anaerobic digester to digest sludge and heat the filter would be an option that future teams could look into.

#### Increasing Height/Depth of filter
This is an area that could improve the performance of the trickling filter. The team is looking for a novel design that can make traditional filters more cost-effective. The team does not believe that there is a lot of room for improvement in just changing the height of the filter.

#### Increasing the specific surface area
Specific surface area is surface area per volume. In order to change the specific surface area of the filter the packing material must be changed. To increase specific surface area, the packing material must have more surface area for the same amount of volume. In many trickling filters in Honduras, the packing material is gravel or rocks. This leaves a lot of room for improvement of surface area. In the US, there has been a lot of research and development of new higher specific surface area packing materials. Many of these materials are very expensive and would not fit with AguaClara low-cost model. From these materials though the team can learn what properties improve filter performance and mimic them in a more cost effective material.  
##### Ideas for improvement
The team's idea for improvement of specific surface are would be a novel geometry and material combination.
* Strings
* Straws
* Sheets
* BioBalls
* Six-pack plastic holder recycling

#### Increasing the $k_{20}$ Value
There is a very little available research on $k_{20}$ values of different trickling filters. Most research reports just state the value for the filters they were testing.
##### Ideas for improvement
* Using different cultures that are more effective at removing nitrogen and Phosphorus
* Ensuring that aeration reaches all areas of the filter, therefore keeping the bacteria functioning at a high rate


#### Flow Distributions
An assumption of this model is that the entire volume of the trickling filter is being used. The team would also like to research whether this assumption is valid. The team believes that there may be unused volume for the trickling filter that is not getting any flow because the water takes another path with less resistance. Therefore the team will also conduct experiments to determine how flow is distributed. After these tests, the team determined how to use a packing material and filter design that utilizes all of the available space.  

### Nitrogen Kinetic Models
The EPA has complied information from many trickling filters across the US that are used for nitrification. They found that bacteria that preform nitrification, usually Nitrosomonas and Nitrobacter, cannot compete against the BOD removing heterotrophs when the BOD levels are high. The EPA suggests that BOD levels be below $20 \frac{mg}{L}$, with the optimal value of $10 \frac{mg}{L}$. The chemical reactions that the nitrifying bacteria are performing are:

$NH_{4}^{+}  + 1.5 O_{2} \rightarrow NO_{2}^{-} + 2H^{+} +  H_{2}O$

$NO_{2}^{-}  + 0.5 O_{2} \rightarrow NO_{3}^{-}$.

When the EPA report was written no kinetic model had been derived for nitrification in trickling filters; however, they found four main parameters that removal was based on: low organic loadings, high residence times, sufficient oxygen availability, and consistency in hydraulic, organic, and ammonia loadings [(US EPA, 1991)](https://nepis.epa.gov/Exe/ZyPDF.cgi/P1004T3S.PDF?Dockey=P1004T3S.PDF). [Duddles et. al., 1974](https://www.jstor.org/stable/pdf/25038735.pdf?refreqid=excelsior%3A134b4fcdcce29130f630db8059aa3119) found that nitrification rate is directly proportional to specific surface area. [Gullicks and Cleasby, 1986](http://www.jstor.org/stable/pdf/25042842.pdf?refreqid=excelsior%3Ad9da82b9b851c3d02a23339cd5f0f45d) found that the mass transfer rate of the biofilm can be increased in two ways: increasing temperature and increasing ammonia concentration. From theses reports the team's earlier assumption the parameters affecting BOD removal are similar to those affecting nitrification is valid.
The team also found another factor that effected nitrification rate which is oxygen availability [(Okey and Albertson 1989)](http://www.jstor.org/stable/25046965). There are two regimes of the nitrogen kinetic equation. When oxygen is limited, it is a zero-order kinetic model with respect to ammonia and half order with respect to oxygen. When oxygen is plentiful, it is a first order model with respect to ammonia. The removal equation found was as:

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

Therefore compared to the team's improvement based on the BOD kinetic model, an additional parameter is oxygen concentration.

#### Ideas for improvements
The team incorporated the need for airflow into their brainstorming of a novel geometry. In developing this novel geometry, the spacing between our media for the biofilm to grow on should be greater than adhesion and cohesion of water particles can withstand.



## Design Parameters

### Factors to Consider in Designing Physical Facilities

1. Type and physical characteristics of packing material
2. Dosing rate
3. Dosing characteristics for distribution system
4. Configuration of underdrain system
5. Ventilation through either natural or forced airflow
6. Settling tank designs for the effluent

### Packing Material properties

| Material |Nominal Size (cm) |Surface Area (m^2/m^3)| Void Space (%) | Application |
| --- | --- | --- | --- | --- |--- | --- |
|  Rock (small)   |   2.5-7.5  |  60   |  50   |  N   |
|  Rock (large)  |  10-13   |   45  |  60   |   C, CN, N  |
|  Plastic -- Conventional   |   61 x 61 x 122  |   90  |  >95   |   C, CN, N  |
|  Plastic -- High Specific Surface Area  |  61 x 61 x 122   |   140  |   >94  |  N   |
|  Rock (small)   |  Varies   |   98  |   80  |   C, CN, N  |
|  Rock (small)   |  Varies   |   150  |  70   |  N   |

### Dosing Rate

The dosing rate of on a trickling filter is the depth of liquid discharged on top of the packing for each pass of the distributor (Tchobanoglous et. al. 2003, pp 898).

$n = \frac{(1 + R)(q)(10^3 mm/m)}{(A)(DR)(60 min/h)}$

* $\small n$ = rotational speed, rev/min
* $\small q$ = influent applied hydraulic loading rate, $\scriptsize\textrm{m^3/m^2*h}$
* $\small R$ = recycle ratio
* $\small A$ = number of arms in rotary distributor assembly
* $\small DR$ = dosing rate, mm/pass of distributor arm


| BOD Loading, kg/m^3 $\cdot$ d |Operating Dose, mm/pass |Flushing Dose, mm/pass|
| --- | --- | --- |
|0.25 |   10-30  |  	$\small\geq$ 200   |
|  0.5  |  15-45   |   $\small\geq$ 200  |
| 1.00   |   30-90  |  $\small\geq$ 300  |  
|  2.00 |  40-120   |  $\small\geq$ 400  |
|  3.00   |  60-180   |  $\small\geq$ 600  |
|  4.00   |  80-240   |  $\small\geq$ 800  |


#### Ideas for Improvements

One of the primary failure modes of a trickling filter system involves complications with the mechanized distribution system in industrial plants. The rotational velocity of the arms is usually driven by the hydraulic propulsion, which may not be the optimal dosing rate, and thus will detrimentally effect the efficiency of the overall treatment train.

As the rotary arms dose water to the system, there is a non-uniform distribution across the filter media. This is an immediate source of efficiency losses since the biofilm can only treat the water in which it comes in contact with. Additionally, the dosing ports in the arms have a tendency to become clogged with miscellaneous debris which may have been missed by the primary clarification process. Most plants do not have sub-metering within the arms to measure the volumetric flow distribution of wastewater being dosed to the system.  

An area for improvement is to completely forgo the mechanical distribution system, and to design a reliable distributor which can dose wastewater uniformly across the media and is adjustable to accommodate the wastewater treatment needs of a community.

### Underdrain Systems
The underdrains capture the filtered wastewater and effluent solids, and serves as the intermediate transfer into the sedimentation tanks (Tchobanoglous et. al. 2003, pp 901). Typical drainage channel slopes range from a 1 to 5 percent grade, and are sized to accommodate a minimum velocity of 2 ft/s.

###Ventilation and Aeration
####Natural Draft
The driving force behind natural airflow is derived from a temperature gradient between the ambient air temperature and the temperature within the pores of the media material. An equation from (Schroeder and Tchobanoglous, 1976):

$D_{air} = 353(\frac{1}{T_c} - \frac{1}{T_h})Z$

* $\small D_{air}$ = natural air draft, mm of water
* $\small T_c$ = cold temperature, K
* $\small T_h$ = hot temperature, K
* $\small Z$ = height of filter, m

The most likely means of aeration in the trickling filter design for this team is a natural draft, which requires the following criteria for it to be implemented successfully:

1. The drainage and collection channels must not flow any greater than halfway full in order to permit air flow throughout the system.
2. Access ports with adequate openings should be implemented at both tremendous.
3. Open areas of the underdrain blocks (top slots) should be no less than 15% of the overall cross-sectional area of the filter.
4. A ratio of 10 $\small ft^2$/250 $\small ft^2$ (open grating area/filter area) should be provided in the design.
(Tchobanoglous et. al. 2003, pp 903)

## Case Study: Cayuga Heights Trickling Filter Observations
The team had the opportunity to visit the Cayuga Heights wastewater treatment plant and observe a trickling filter first-hand. It was a very informative visit, and the team was dismayed at the state of the plant and the many issues it was experiencing, especially with the trickling filters. There were two trickling filters at the plant, both of which had substantial debris (clumps of organic material, trash) on top of filter (see Figure 1); the plant manager stated that the cause was likely a failure of the bar screen that should have removed such debris when the water initially enters the plant the plant and the inefficiency of the settling tanks, which the wastewater travels through immediately before the trickling filters.

The team also observed that the distribution arms were failing to cover the surface of the filter with water and there was a significant portion of the tank surface that was getting little to no water on it (see Figure 2). The regions that were most noticeably dry were the edges of the tank and an area a couple feet from the center of the base of the distributor arms. There was also a pattern of discoloration on the top of the filter, which seemed to be caused by the substantial organic matter coming through, that suggested that even the portion of the filter’s surface that was getting watered was not getting watered equally, and that there was build up of the organic matter that was getting more water (see Figure 1).

There was leakage from the base of the distributor arm on both trickling filters. One had very substantial leakage and a large fraction of the water was just spraying out of the center to only a foot or two away. The plant manager said that the seal connecting the pipe and distributor arm had broken and was going to be replaced. The volume of water going through the filter in the area around the base of the distributor arm was very high and the team would expect that the level of treatment for that wastewater is very low, if not non-existent, because of how high the hydraulic loading must be.

The team’s visit to the wastewater treatment plant was very valuable in that it confirmed that the potential issues documented in the literature can be a reality and it made obvious the fact that there is tremendous room for innovation and improvement of trickling filter technology.


![Figure 1](https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/CHFT%20filter%20surface.jpg?raw=true)
Figure 1: The surface of the trickling filter with significant debris and discoloration.

![Figure 2](https://github.com/AguaClara/Trickling-Filter/blob/master/pictures/CHTF%20distribution%20arm.png?raw=true)
Figure 2: Distribution arms failed to entirely cover the surface of the trickling filter and there was leakage from the base in the center.



## Methods

### Procedure
The benchtop experiment for the team is still under development, however, the means with which the experiment will be conducted is backed through verbal and written consensus within the team. The primary objective of the team's first experiment is to gather a hydraulic model for the preferential flow tendencies within the filter media. It is hypothesized that much of the porosity in the filter media is unutilized, and will remain dry due to flaws in the distribution system as well as the geometric structure of the filter.

Water will be dispensed by pipetting a designated volume into the media at a specified point at the surface of the filter. This point will be marked off by drilling and annotating holes on a cap covering the entry point of the filter. The distribution of water will vary both across the distribution grid and by varying the depth of gravel. After a trial is conducted, a collection module of cuvettes will be weight in order to capture the exit point of the water under a given distribution and media depth.  

Hydraulic fingering through the media will be represented through a three-dimensional heat map. This experiment can be characterized by the underlying principal of a CAT-scan: the data will provide insight into the cross sectional behavior within the trickling filter media which has not been greatly understood in literature. As more data is collected across varying points in the horizontal plane from the entry grid, and then in the vertical plane by adding or subtracting gravel (packing material), a more robust representation of the hydraulic behavior can be characterized; this level of detail depends on the granularity of the trials and the level of consistency between them.


## Conclusion

In the team’s initial research, extensive information has been gathered on the operational difficulties, the kinetics, and typical design parameters of trickling filters. Many of the issues plant operators encounter with trickling filters, like clogging and ponding, lack of moisture in parts of the filter, and generally inefficiency of the filter can be addressed by improving two aspects of the filter: the filter media itself and the distribution system. The BOD kinetic model also supports improving the filter media to increase the specific surface area, using alternative materials instead of the traditional rocks or gravel. The team’s research on nitrogen kinetics adds a need for proper aeration of the filter to the list of considerations when designing a new filter media.

The lack of available information and limited research on some aspects of the kinetic model, $k_{20}$ values for example, motivate the team to potentially do lab tests and calculate $k_{20}$ values for various media and try to find a more standardized model than what is found in the existing literature. Similarly, the team is working on a test to address the assumption made by the current kinetic model that the entire volume of the filter is being used by looking at the flow distribution.

Preliminary research was driven primarily by industry research, however, it is expected than many of the established parameters will be subject to change as a result of independent research efforts. The findings of the team's experiments will be intended to characterize a trickling filter system absent of mechanical components and with higher filter media utilization. By the conclusion of this team's work, a vast majority of the gaps in literature will be filled with conclusive empirical data to serve as a model for wastewater plants in resource-scarce locations in addition to modifying the faults in industry around the world.

## Future Work

In the coming weeks, the team will be conducting its preliminary tests to determine the distribution of flow in trickling filters. The team believes that their literature review period is almost over and hopes to move almost all their time to bench-top testing. In addition to flow mapping, the team will also work on designing novel geometries for testing. This will include building models of the team's current ideas. A future goal that will not be done this semester is to create a bench top model so that nitrogen and phosphorus removal can be measured. The team believes there is many different areas for improvement in the trickling filter and research should continue to explore the possibilities.

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
