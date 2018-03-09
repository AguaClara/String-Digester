# Trickling Filter, Spring 2018
#### Jillian Whiting, Ben Gassaway, Rosie Krasnoff
#### March 9th, 2018

## Abstract
Briefly summarize your previous work, goals and objectives, what you have accomplished, and future work. (100 words max)

This was the first semester of a trickling filter subteam, therefore the direction of the team's research was derived independently. The goals for this semester were to identify problems with trickling filters in industry whilst developing robust kinematic models such to enable future subteams to employ novel trickling filter applications. This semester was expected to be driven primarily by literature research, but the team has begun construction for a benchtop experiment in preliminary hydraulic modeling through the filter media.

## Introduction
Explain how the completion of your challenge will affect AguaClara and the mission of providing safe drinking water (or sustainable wastewater treatment!). If this is a continuing team, how will your contribution build upon previous research? What needs to be further discovered or defined? If this is a new team, what prompted the inclusion of this team?

The overall objective of the team is to first identify the primary issues in industrial-scale trickling filters. Using this information, the team aims to deploy both a disruptively efficient, non-mechanized trickling filter which can be adapted to serve the wastewater needs of a resource-scarce community.

## Literature Review and Previous Work
Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.

-------

There is significant documentation of problems plant operators experienced when dealing with trickling filters. Some of the issues, while important to take into consideration when implementing trickling filters, may not offer much room in terms of what improvements the team can make. Problems include: the development of slug populations in the trickling filters, which can remove the layer of biofilm and harm the nitrifying bacteria population, thereby negatively impacting the systems performance and plug the channels of the system; filter flies, whose presence suggests a lack of moisture throughout the filter; and foul odors, which can indicate an increasing level of anaerobic reactions or accumulating sloughed-off biomass in the filter media.

Some of these previously mentioned problems (biomass sloughing and insect and slug presence in filters) contribute to clogging and ponding in filters. Current solutions include “flashing with low doses of chlorine to remove deposited solids and kill excess biomass” or periodic flooding. The team aims to address these issues by developing a new trickling media that has a lower tendency to experience clogging or ponding.

There can be issues with variations in temperature: biofilm thickness changes seasonally and can be low quality and uneven in cold temperatures. In freezing weather, formation of ice can cause clogging and therefore structural damage to the trickling media. These are probably not major concerns for plants in equatorial regions, and so while important to note, will not be a focus for the team at this point.

 Ali et al. states that the most common problem in trickling filters is uncontrolled sloughing, which is often caused by uneven hydraulic loading rates. This can be particularly problematic after storm events when flooding results in very high hydraulic loading. It can also be caused by clogging and uneven distribution of the influent. [(Ali et al. 2017)](http://www.pjoes.com/pdf/26.6/Pol.J.Environ.Stud.Vol.26.No.6.2431-2444.pdf) There is potential for the development of a much-improved distribution system that could help to alleviate this problem.

 Proper distribution is crucial and can optimize efficiency of treatment. The most common method of distribution is rotating distributors, but after seeing the problems with them at the Cayuga Heights wastewater treatment plant (see following section for details), the team was interested in learning more about other methods that might require less maintenance or be less prone to failure.

The less common method of distribution, the fixed distribution systems, utilizes lateral and main distribution pipes, which are placed just above the medium, spaced to give uniform distribution of water. They generally have nozzles with a circular hole and a deflector. They are more commonly used with intermittent dosing, and so flow from the system varies; it starts at a maximum and lowers as the tank empties. Currently, fixed distribution systems are mostly used in deep filter and biotowers.

Unfortunately, these systems are also prone to clogging or blockage issues and similarly challenged by inconsistency of hydraulic load on the surface of the trickling filter. This is another area where there is huge potential for the team to increase the productivity of trickling filters. [(Sperling 2007)](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402123.pdf)

## Kinetics
### BOD Kinetic Model
The trickling filter will be used as the second treatment in series with a UASB reactor. The assumptions of the trickling filter team is that the majority of BOD will be removed by the UASB reactor. Therefore the trickling filter will be mostly removing nutrients (i.e. Nitrogen and Phosphorus). The team could not find consistent literature on a kinetic model for the removal of nitrogen or phosphorus. Therefore, we are using a BOD kinetic model with the assumption that nutrient removal would be proportional to BOD removal. The most common kinetic model for trickling filters is the modified Velz Equation.

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
* Strings
* Straws
* Sheets (Cross-flow)
* BioBalls
* Six-pack plastic things

#### Increasing the $k_{20}$ Value
There is a very little available research on $k_{20}$ values of different trickling filters. Most research reports just state the value for the filters they were testing.
##### Ideas for improvement
* Using different cultures that are more effective at removing nitrogen and Phosphorus
* Ensuring that aeration reaches all areas of the filter, therefore keeping the bacteria functioning at a high rate


#### Flow Distributions
An assumption of this model is that the entire volume of the trickling filter is being used. The team would also like to research whether this assumption is valid. The team believes that there may be unused volume fo the trickling filter that is not getting any flow because the water takes another path with less resistance. Therefore the team also conducted experiments to determine how flow is distributed. After these tests, the team determined how to use a packing material and filter design that utilizes all of the available space.  


## Case Study: Cayuga Heights Trickling Filter Observations
The team had the opportunity to visit the Cayuga Heights wastewater treatment plant and observe a trickling filter first-hand. It was a very informative visit, and the team was dismayed at the state of the plant and the many issues it was experiencing, especially with the trickling filters. There were two trickling filters at the plant, both of which had substantial debris (clumps of organic material, trash) on top of filter; the plant manager stated that the cause was likely a failure of the bar screen that should have removed such debris when the water initially enters the plant the plant and the inefficiency of the settling tanks, which the wastewater travels through immediately before the trickling filters.

The team also observed that the distribution arms were failing to cover the surface of the filter with water and there was a significant portion of the tank surface that was getting little to no water on it. The regions that were most noticeably dry were the edges of the tank and an area a couple feet from the center of the base of the distributor arms. There was also a pattern of discoloration on the top of the filter, which seemed to be caused by the substantial organic matter coming through, that suggested that even the portion of the filter’s surface that was getting watered was not getting watered equally, and that there was build up of the organic matter that was getting more water.

There was leakage from the base of the distributor arm on both trickling filters. One had very substantial leakage and a large fraction of the water was just spraying out of the center to only a foot or two away. The plant manager said that the seal connecting the pipe and distributor arm had broken and was going to be replaced. The volume of water going through the filter in the area around the base of the distributor arm was very high and the team would expect that the level of treatment for that wastewater is very low, if not non-existent, because of how high the hydraulic loading must be.

The team’s visit to the wastewater treatment plant made obvious that there is tremendous room for innovation and improvement of trickling filter technology.

### Nitrogen Kinetic Models
The EPA has complied information from many trickling filters across the US that are used for nitrification. They found that bacteria that preform nitrification, usually Nitrosomonas and Nitrobacter, cannot compete against the BOD removing heterotrophs when the BOD levels are high. The EPA suggests that BOD levels be below $20 \frac{mg}{L}$, with the optimal value of $10 \frac{mg}{L}$. The chemical reactions that the nitrifying bacteria are performing are:

$NH_{4}^{+}  + 1.5 O_{2} \rightarrow NO_{2}^{-} + 2H^{+} +  H_{2}O$

$NO_{2}^{-}  + 0.5 O_{2} \rightarrow NO_{3}^{-}$.

When the EPA report was written no kinetic model had been derived for nitrification in trickling filters; however, they found four main parameters that removal was based on: low organic loadings, high residence times, sufficient oxygen availability, and consistency in hydraulic, organic, and ammonia loadings. Duddles et. al. 19074 found that nitrification rate is directly proportional to specific surface area.


## Methods
Explain the techniques you have used to acquire additional data and insights. Reserve fine detail for the Manual at the end of the report, but use this section to give an overview with enough detail for the reader to understand your Results and Analysis. Describe your apparatus, and have a justification for every decision you made and every parameter you chose in the design of the apparatus. Be especially careful to detail the conditions your experiments were conducted under, as this information is especially important for interpreting your results

Below, some example sections are given. Sectioning the report is meant to keep similar information together.  Continue making sections as necessary, or delete sections if you do not need them. Feel free to add subsubsections to further delineate the information. For example, under the Experimental Apparatus section below, the EStaRS team might consider having sections such as "Filter Design" and "Filter Fabrication".

### Experimental Apparatus
Explain your apparatus setup using enough detail such that future teams can recreate your apparatus. Make sure to explain why you built it this way.
* Design (calculations, constraints)

  $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
* Schematic (label parts)

  <img src="https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/IMG_0009.jpg?raw=true" height=250 width=200>

* Image (from lab; label parts)
* Materials (dimensions, materials)
* Complications in construction
* If already constructed: write a brief summary of important constraints, include any revisions to apparatus, also reference the prior report where construction is described

### Procedure
Discuss your experimental procedure. How did you run your experiment? What were you testing? What were the values of relevant parameters?

## Results and Analysis
Present an observation (results), then explain what happened (analysis).  Each paragraph should focus on one aspect of your results. In that same paragraph, you should interpret that result.  
In other words, there should not be two distinct paragraphs, but instead one paragraph containing one result and the interpretation and analysis of this result. Here are some guiding questions for results and analysis:

When describing your results, present your data, using the guidelines below:
* What happened? What did you find?
* Show your experimental data in a professional way.
```python
from aide_design.play import*
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
plt.figure('ax',(10,8))
plt.plot(x,y,'*')
plt.savefig('/Users/jillianwhiting/github/Jillian-Whiting/Images/linear')
plt.show()
```
![linear](https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/linear.png?raw=true)
Figure 1: Captions are very important for figures. Captions go below figures.

After describing a particular result, within a paragraph, go on to connect your work to fundamental physics/chemistry/statics/fluid mechanics, or whatever field is appropriate. Analyze your results and compare with theoretical expectations; or, if you have not yet done the experiments, describe your expectations based on established knowledge. Include implications of your results. How will your results influence the design of AguaClara plants? If possible provide clear recommendations for design changes that should be adopted. Show your experimental data in a professional way using the following guidelines:
* Why did you get those results/data?
* Did these results line up with expectations?
* What went wrong?
* If the data do not support your hypothesis, is there another hypothesis that describes your new data?

## Conclusions
Explain what you have learned and how that influences your next steps. Why does what you discovered matter to AguaClara?

Make sure that you defend your conclusions with facts and results.

## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.

Tchobanoglous, G., F. Burton, H. D. Stensel (2003) *Wastewater Engineering: Treatment and Reuse*. New York, NY: McGraw-Hill


# Manual
The goal of this section is to provide all of the guidance that would be necessary for a future team to pick up your work where you left off. Please try to be thorough and put yourselves in the shoes of a newcomer to the project. Below are some recommended sections, but the manual will likely take a slightly different form for each team.

## Fabrication Details
Include any information related to the fabrication of equipment, experimental apparatuses, or technologies. Include the purpose of each step and the fabrication methods used. Reference appropriate safety precautions.

## Special Components
If your subteam uses a particular part that is unique and you could foresee a future subteam needing to order it or learn more about it, please include basic information like the vendor where it was purchased, catalog/item number, and a link to any documentation.

## Experimental Methods
### Set-up
Step 1.
* Put tasks in a sequential order.
* It is okay to have sub-lists.
  - Like this.

### Experiment
Step 1.

### Cleaning Procedure
Step 1.

## Experimental Checklist
Another potential section could include a list of things that you need to check before running an experiment.

## ProCoDA Method File
Use this section to explain your method file. This could be broken up into several components as shown below:

### States
Here, you should describe the function of each state in your method file, both in terms of its overall purpose and also in terms of the details that make it distinct from other states. For example:
\begin{itemize}
\item \underline{OFF} - Resting state of ProCoDA. All sensors, relays, and pumps are turned off.
\end{itemize}

### Set Points
Here, you should list the set points used in your method file and explain their use as well as how each was calculated.

## Python Code

### Variables
$g$: gravity
$\sigma$: dispersion
$a$: amplitude
$h$: water depth
$H$: distance from wave crest to trough (2$a$)
$T$: wave period
$\lambda$: wavelength
$k$: wavenumber
$c_p$: celerity (wave phase speed)
$P$: pressure
$F$: force
$u$, $w$: x-velocity, z-velocity components

```python
# Comment
```

# Add/Delete/Change this Template as you see Fit
When using this template keep in mind that this serves three purposes. The first is to provide your team feedback on your progress, assumptions, and conclusions. The second is to keep your team focused on what you are learning and doing for AguaClara. Another is to educate future teams on what you've learned and done. This document should be comprehensive, consistent, and well-written. With that in mind, add, subtract, or move sections. Reach out to the RAs and graders for help with figuring out what should or shouldn't include. Focus on how wonderful a reference you are making through this and work hard on communicating amongst yourselves and with future teammates. (Delete this section before submitting)

```python
# To convert the document from markdown to pdf
pandoc Name_of_this_file.md -o TeamName_Research_Report.pdf
```
