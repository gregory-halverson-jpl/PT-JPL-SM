# SMAP soil moisture improves global evapotranspiration

**Journal:** Remote Sensing of Environment 219 (2018) 1–14

## Authors

- Adam J. Purdy<sup>a,b,⁎</sup>
- Joshua B. Fisher<sup>b</sup>
- Michael L. Goulden<sup>a</sup>
- Andreas Colliander<sup>b</sup>
- Gregory Halverson<sup>b</sup>
- Kevin Tu<sup>c</sup>
- James S. Famiglietti<sup>a,b</sup>

### Affiliations

<sup>a</sup> Department of Earth System Science, University of California, Irvine, CA 92697, USA  
<sup>b</sup> Jet Propulsion Laboratory, California Institute of Technology, Pasadena, CA 91109, USA  
<sup>c</sup> Dupont Pioneer, IA, USA

⁎ Corresponding author: ajpurdy@uci.edu

## Keywords

- Evapotranspiration
- Soil moisture
- Hydrology
- Evaporation
- Transpiration
- SMAP
- MODIS

## Abstract

Accurate estimation of global evapotranspiration (ET) is essential to understand water cycle and land-atmosphere feedbacks in the Earth system. Satellite-driven ET models provide global estimates, but many of the ET
algorithms have been designed independently of soil moisture observations. As water for ET is sourced from the
soil, incorporating soil moisture into global remote sensing algorithms of ET should, in theory, improve performance, especially in water-limited regions. This paper presents an update to the widely-used Priestley TaylorJet Propulsion Laboratory (PT-JPL) ET algorithm to incorporate spatially explicit daily surface soil moisture
control on soil evaporation and canopy transpiration. The updated algorithm is evaluated using 14 AmeriFlux
eddy covariance towers co-located with COsmic-ray Soil Moisture Observing System (COSMOS) soil moisture
observations. The new PT-JPLSM model shows reduced errors and increased explanation of variance, with the
greatest improvements in water-limited regions. Soil moisture incorporation into soil evaporation improves ET
estimates by reducing bias and RMSE by 29.9% and 22.7% respectively, while soil moisture incorporation into
transpiration improves ET estimates by reducing bias by 30.2%, RMSE by 16.9%. We apply the algorithm
globally using soil moisture observations from the Soil Moisture Active Passive Mission (SMAP). These new
global estimates of ET show reduced error at ﬁner spatial resolutions and provide a rich dataset to evaluate land
surface and climate models, vegetation response to changes in water availability and environmental conditions,
and anthropogenic perturbations to the water cycle.

## 1. Introduction
Water movement from land to the atmosphere, or evapotranspiration (ET), is an integral part of earth's ecological and climate systems.
This process links the water, carbon, and energy cycles in the earth
system. Therefore, accurate observations of ET facilitate detection of
the human ﬁngerprint on the water cycle and surface energy budget (Lo
and Famiglietti, 2013; Sorooshian et al., 2011), studies on land-atmosphere feedbacks related to heat wave intensity (Miralles et al., 2014),
quantiﬁcation of agricultural and ecosystem water use (Allen et al.,
2007; Anderson et al., 2011; Goulden et al., 2012; Goulden and Bales,
2014), identiﬁcation of droughts where plants may become vulnerable
to other biotic stressors and potential mortality (Anderson et al., 2013;
McDowell, 2011; Mu et al., 2013), and provide benchmarks to evaluate
and improve parameterizations in land surface models (Mueller et al.,
2013; Rodell et al., 2011). With increasing global temperatures and the
subsequent greater atmospheric capacity for water vapor, ET may accelerate with the water cycle and alter global water distribution making
⁎

certain regions drier (Syed et al., 2010; Huntington, 2006). As land begins to dry, (Greve and Seneviratne, 2015; Jung et al., 2010) quantifying where and to what degree reductions in water availability limits
ET becomes increasingly important.
Remote sensing algorithms are an eﬀective way to derive observationally-constrained ET estimates at the necessary spatiotemporal
resolutions to support earth observations (Fisher et al., 2017, 2008;
Miralles et al., 2011; Mu et al., 2011; Su, 2002). Multiple manuscripts
have reviewed the state and needs for ET remote sensing (Fisher et al.,
2017; Wang and Dickinson, 2012) and one common theme across many
of these remote sensing approaches is a limited or absent representation
of soil moisture. Of the ET remote sensing algorithms, few approaches
remain both physically defensible and globally applicable without reliance on data assimilation and prognostic land surface models. One
model that lacks soil moisture representation and ﬁts the aforementioned description is the Priestley-Taylor Jet Propulsion Laboratory (PTJPL) ET model.
The PT-JPL ET model, a widely used remote sensing retrieval

Corresponding author at: Department of Earth System Science, University of California, Irvine, CA 92697, USA.
E-mail address: ajpurdy@uci.edu (A.J. Purdy).

https://doi.org/10.1016/j.rse.2018.09.023
Received 8 December 2017; Received in revised form 20 September 2018; Accepted 25 September 2018
Available online 09 October 2018
0034-4257/ © 2018 Elsevier Inc. All rights reserved.

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

on sub-optimal environmental limitations (Fisher et al., 2008; Jin et al.,
2011; Miralles et al., 2011). However, plant access to soil moisture
varies with rooting depth and much uncertainty exists with the role
deep roots play in mitigating limitations from soil water availability
during drought (Schenk and Jackson, 2002). Plant type, canopy height
and aboveground biomass provide indicators of rooting depth and the
potential to access to deeper soil water (Canadell et al., 1996; Fan et al.,
2017; Jackson et al., 1999). Miralles et al. (2011) postulate taller vegetation is less sensitive to soil water deﬁcits compared to shorter canopy plants due to deep rooting potential to alleviate plants from seasonal drought conditions (i.e., when precipitation occurs outside of the
of summer maximum atmospheric demand). Recent global observations
of canopy height create an opportunity to further inform plant sensitivity to environmental conditions (Simard et al., 2011).
We present an update to the PT-JPL algorithm by incorporating
explicit surface soil moisture constraint from SMAP to model ET globally. To address previous model parameterization limitations, we use
integrated in situ observations of soil moisture and ET to implement soil
moisture control within the PT-JPL model. Then, we apply the new PTJPLSM model globally using soil moisture data from the Soil Moisture
Active Passive mission (SMAP). The following sections will provide: (1)
a description of the PT-JPL algorithm with updates detailing soil
moisture constraints on evaporation and transpiration, (2) details on
the datasets used in this study, (3) results evaluating the updated PTJPLSM model compared to the original PT-JPL model using eddy covariance towers from Ameriﬂux and globally using satellite datasets, and
(4) discussion on the implications of soil moisture on global ET quantiﬁcation improvement.

algorithm, has outperformed many models for the majority of globally
distributed eddy covariance towers within model inter-comparison
studies achieving both high explanation of variance and low error
(Ershadi et al., 2014; Michel et al., 2016; Vinukollu et al., 2011). Despite a strong performance in these studies, the PT-JPL algorithm lacks
soil moisture control and is restricted by its dependence on a combination of atmospheric conditions and vegetation characteristics to represent surface conditions. These limitations become especially evident
in regions where the coarse near surface air temperature and water
vapor pressure deviate from the underlying surface soil water availability at ﬁne temporal frequencies, in areas with highly heterogeneous
land covers, in areas of active land management, or in regions prone to
atmospheric advection conditions. Therefore, incorporating soil
moisture observations has great potential to address these limitations
and improve global ET estimates but large challenges exist.
There are two main challenges to improve global estimates of ET
using soil moisture: 1) observing accurate integrated values of soil
moisture; and, 2) appropriately modeling how limitations from soil
moisture interact with other environmental constraints to quantify ET.
The launch of the Soil Moisture Active Passive (SMAP) satellite
(2015) addresses the ﬁrst challenge through providing global soil
moisture observations (Entekhabi et al., 2010). The SMAP mission has
leveraged lessons from other global soil moisture observing satellites,
such as the Advanced Microwave Scanning Radiometer- EOS (Njoku
et al., 2003) and the Soil Moisture Ocean Salinity (Kerr et al., 2016)
satellites to detect and mitigate potential radio frequency interference
and provide observations at relatively high spatio-temporal [9–36 km,
3-daily] resolutions at a depth [5-cm] applicable to improve modeled
ET (Johnson et al., 2016; Mohammed et al., 2016; Oliva et al., 2012;
Piepmeier et al., 2014). These observations have been extensively
evaluated as part of a rigorous calibration and validation campaign and
shown to be within mission accuracy requirements (unbiased
RMSE < 0.04 cm3 cm−3) and thus capable of supporting improvements
to global ET quantiﬁcation (Colliander et al., 2017). Additionally, despite only providing surface soil moisture observations, recent in situ
analyses have shown that surface soil moisture provides similar
amounts of predictive information as rooting depth soil moisture for
latent heat quantiﬁcation (Qiu et al., 2016).
To address the second challenge, model testing and updates needs to
be done with coterminous observations of meteorological conditions,
soil moisture, and ET. Observations of soil moisture and ET are made
globally in distributed networks of eddy covariance (EC) towers as part
of FLUXNET and AmeriFlux networks (Baldocchi et al., 2001). However, sites often include measurements of soil moisture at only 1–4
points and these points may misrepresent actual land surface conditions
within the EC footprint making model parameterization and calibration
diﬃcult. Fortunately, a new observation network from the COsmic-ray
Soil Moisture Observing System (COSMOS) provides integrated observations at similar scales to EC tower footprints (Zreda et al., 2012).
EC observations of water and energy exchange at the earth's surface colocated with integrated soil moisture observations provide a valuable
dataset to compliment satellite observations of environmental variables
necessary to test and evaluate ET models (Baldocchi et al., 2001).
Generally, land surface and remote sensing models relate the
amount of ET to water availability and the atmospheric demand for ET,
but vary to what degree and at what point water availability limits and
eventually prevents ET. Various adaptations of soil moisture normalized by soil properties to compute the relative extractable water (REW)
have been applied to limit transpiration [Fig. S1, Table S1]. Yet, soil
moisture is just one of many environmental variables that limits the
maximum stomatal conductance, as temperature and vapor pressure
extremes have been found to regulate transpiration (Fisher et al., 2008;
Jarvis and Mcnaughton, 1986; Monteith, 1965; Mu et al., 2011; Novick
et al., 2016). Therefore, modeling approaches that have adopted REWbased stressors are often applied in series with other scalar stressors,
such as temperature and vapor pressure, to reduce potential ET based

## 2. PT-JPL algorithm
### 2.1. PT-JPL ET algorithm
The Priestley Taylor-Jet Propulsion Laboratory (PT-JPL) ET algorithm applies ecophysiological constraints to model reductions of ET
from the atmospheric potential ET due to sub-optimal environmental
conditions (Fisher et al., 2008). The model incorporates a variety of
data sources from satellite observations and reanalysis datasets [Fig. 1;
Table 1]. Potential ET, or latent energy LE, is computed using the
Priestley-Taylor model:

PET = α

∆
(RN − G )
λ (∆ + γ )

(1)

where PET [mm day−1] is the potential ET based on temperature and
radiation, α is the Priestley-Taylor coeﬃcient that is set to 1.26, Δ is the
slope of the saturated vapor-pressure relationship [kPa °C−1], and γ is
the psychrometric constant [kPa °C−1], and RN is the net radiation
[W m−2], G is the ground heat ﬂux [W m−2], and λ is the latent heat of
vaporization [MJ kg−1] (Priestley and Taylor, 1972). The water cycle
and energy cycle are linked through ET and latent heat LE such that the
latent heat of vaporization ET λ = LE. The PT-JPL algorithm is a three
source ET model where each component of ET is used to calculate the
total ﬂux:

LE = LEI + LET + LES

(2)

where LEI is evaporation from plant intercepted water, LET is transpiration from vegetation, and LES is soil evaporation. Ecophysiological
f-functions, scalars between 0 and 1, limit each component from the
potential rate.
Canopy interception is computed as:

LEI = fWET α

∆
RN C
(∆ + γ )

(3)

where fWET is the fraction of saturated soil computed as fWET = RH4,
where RH is the relative humidity of air, RN C is the canopy net radiation
calculated as RNC = RN − RNS. RNS is the net radiation at the soil surface
2

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Fig. 1. Flow chart showing data processing stream for the PT-JPLSM model.

where fSM is the soil moisture constraint computed as fSM = RHVPD, VPD
is the vapor pressure deﬁcit. For further detail reference Fisher et al.,
2008.
Soil water control on evaporation is implicitly represented through
fSM = RHVPD, where fSM is the soil moisture constraint on ES, RH is the
relative humidity, and VPD is the vapor pressure deﬁcit. This equation
is formed from Bouchet's theory of land atmosphere equilibrium.
However, the assumption that land and atmosphere are in equilibrium
at the ﬁne spatial resolutions and acute temporal scales fails for certain
regions. Similarly, plant water availability is implicitly represented by
observations based on plant greenness and therefore phenological
changes from peak greenness potentially introduces latent vegetation
response to water limitations and overestimates transpiration.

computed as RN S = RN e (−k Rn LAI ) where kRn = 0.60 and LAI is the leaf
area index.
Canopy transpiration is computed as:

LET = (1 − fWET ) fG fT fM α

∆
RN C
(∆ + γ )

(4)
f

where fG is the fractional canopy greenness computed as fG = fAPAR
IPAR
where fAPAR is the fraction of absorbed photosynthetically active radiation (PAR) and fIPAR is the fraction of intercepted PAR; fT is the sub⎛− T − Topt
⎜
Topt
optimal temperature constraint computed as fT = e⎝

(

2

) ⎞⎠ where T
⎟

is the maximum daily air temperature and TOPT is the optimum temperature computed as Topt = Tmax at max

{

PARf APAR Tmax
VPD

} which computes

when maximum plant activity is likely to occur; and fM is the vegetation
f
moisture constraint computed as fM = f APAR where fAPARmax is the
annual maximum fAPAR.
Soil evaporation is computed as:

LES = [fWET + fSM (1 − fWET )] α

### 2.2. Updates to the PT-JPL model

APAR max

∆
(RN s − G )
(∆ + γ )

We update the original model, here-after called PT-JPLSM, to incorporate explicit soil water availability control on evaporation and
transpiration. Because we now model ET at sub-monthly time scales, we
also integrate a new G parameterization.

(5)

Table 1
Global gridded forcing dataset characteristics.
Variable

Product name

Time available

Frequency

Spatial resolution

Reference

Net radiation
Temperature
Vapor pressure
NDVI
Soil moisture

MERRA2 M2T1NXLND
MERRA2 M2I1NXASM
MERRA2 M2I1NXASM
MOD13A2 MYD13A2
SPL3SMP_E v1 SPL3SMP v4

1979–present
1979–present
1979–present
2000–present
4-2015–present

Hourly
Hourly
Hourly
8-daily
3-daily

Soil properties
Canopy height

SPL4SMLM
NA

NA
NA

NA
NA

0.5° × 0.5°
0.5° × 0.5°
0.5° × 0.5°
5 km × 5 km
9 km × 9 km
36 km × 36 km
9 km × 9 km
1 km × 1 km

GMAO, 2015a
GMAO, 2015b
GMAO, 2015b
Didan 2015a, 2015b
O'Neill et al., 2016
O'Neill et al., 2016
Das, 2013
Simard et al., 2011

3

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

2.2.1. Soil moisture control on evaporation
Surface soil moisture and soil properties control the rate of evaporation. As such we employ the available water content to scale the
rate of evaporation. The relative extractable water is a commonly used
stressor that normalizes the impact from soil properties. The original
model employs the fSM scalar to limit the rate of evaporation from the
soil surface. This scalar was formulated to represent relative extractable
water through the Bouchet's theory of where the land surface and near
surface atmosphere are in equilibrium across certain space and time
scales. Here we update the model to represent true relative extractable
water using:

fREW =

p=

θWPCH =

where θobs is the soil moisture observation, θWP is the soil-plant wilting
point, and θFC is the soil ﬁeld capacity. We replace fSM with fREW in the
new evaporation algorithms.

∆
(RN s − G )
(∆ + γ )

(7)

This method has been implemented in other remote sensing ET algorithms that use ET to model surface and root zone soil moisture
(Anderson et al., 2007; Martens et al., 2017).
2.2.2. Soil moisture control on transpiration
In the original PT-JPL formulation plant moisture stress is inferred
from the deviation from maximum greenness (fM). As the model was
originally developed for application at monthly or longer timescales,
the latent responses from vegetation to moisture deﬁcits did not impact
quantiﬁcation of ET, as it does at higher temporal frequencies, i.e. daily
calculations. Therefore, we formulate and include a new soil water
availability constraint on transpiration. Since shorter vegetation responds more quickly than compared to taller vegetation to precipitation
deﬁcits, above ground observations may provide insight into plant resiliency to a limited moisture supply (Knoop and Walker, 1985). Plant
access to deeper water has been shown to increase resilience and survival probability to prolonged drought (Canadell et al., 1996; Giardina
et al., 2017; Nepstad et al., 1994; Padilla and Pugnaire, 2007). Unfortunately, the science communities understanding of rooting depth,
density and access to the water table has limited previous attempts to
implement soil moisture limitations within ET models (Kelliher et al.,
1993). Therefore, we implicitly represent plant resilience to soil water
deﬁcits through above ground satellite observable canopy characteristics. Previous studies have applied canopy characteristics to infer
sensitivity to soil water availability (Dewaele et al., 2017; Martens
et al., 2017). We acknowledge at aggregated scales a robust direct relationship between above ground biomass or canopy and resilience to
drought depends on other factors such as functional rooting depth,
species composition, water table depth, geology, and plant age (Fan
et al., 2017; Giardina et al., 2017). However, for the purposes of this
study, we apply canopy height as one variable to infer plant sensitivity
to surface soil water availability. We posit that canopy height is related
to the rooting depth and potential to access water from deeper sources.
Therefore, canopy height data facilitate a continuous quantiﬁcation of
plant sensitivity to surface soil water conditions (Canadell et al., 1996;
Jackson et al., 1999; Martens et al., 2017; Nepstad et al., 1994). We
calculate the new transpiration constraint as:

LET = (1 − fWET ) fTRM fG fT α

(12)

∆
RN C
(∆ + γ )

(13)

## 3. Datasets and data processing
3.1. Global and in situ model forcing datasets
We combine satellite observations of vegetation and surface soil
moisture with meteorological data from a reanalysis dataset to model
ET globally. We evaluate the model using both in situ and gridded
forcing datasets. In situ meteorological (RNET, TAIR, eA), soil moisture
(θ), and latent heat observations at integrated spatial scales from these
two networks facilitate updates to the PT-JPL algorithm. Gridded forcing data from MERRA, the MODerate resolution Imaging Spectrometer
(MODIS), ICESat/GLAS, and SMAP provide spatially continuous data
sources to model ET globally. All datasets are open access and available
from: the NASA Land Process Distributed Archive Center (https://
e4ftl01.cr.usgs.gov/; http://daac.ornl.gov/MODIS/), the Goddard
Earth Sciences Data and Information Services Center (https://goldsmr4.
gesdisc.eosdis.nasa.gov:443), the National Snow and Ice Data Center
(https://n5eil01u.ecs.nsidc.org), the COsmic-ray Soil Moisture
Observing System (COSMOS) (http://cosmos.hwr.arizona.edu), the
Lawrence Berkley Livermore National Laboratory's Ameriﬂux

(8)

where θCR is the critical soil moisture at which soil water availability
limits ET, CHscalar = CH is a canopy height (CH) scalar that impacts
the sensitivity to soil water availability, set to range from 1 to 5.

θCR = (1 − p)(θFC − θwpCH ) + θwpCH

(11)

2.2.3. Ground heat ﬂux
Previously, since PT-JPL was implemented at monthly time resolution G was estimated to be 0. For daily ET calculation, we derive G as
described in Allen et al. (2007), but update the parameterizations based
on tall and short canopies. The updated model parameters were calibrated to a G evaluation dataset (Purdy, 2018; Purdy et al., 2016). Both
PT-JPL and PT-JPLSM are updated to include G. The equations used to
model G and the updated parameterizations are presented in the supplemental material.

CHscalar

θ − θobs ⎞
fTREW = 1 − ⎜⎛ CR
⎟
− θwpCH ⎠
θ
CR
⎝

θWP
CHscalar

where p is a parameter dependent on both PET [mm/day] and CH [m]
that quantiﬁes at which point soil water availability begins to limit
transpiration below the potential rate, a is a parameter set to 0.1 represents the weight of inﬂuence CH imposes on θCR, and θwpCH is the
canopy height adjusted surface soil moisture wilting point. Eq. (8) was
formed from the inﬂuence of Martens et al. (2017), but adjusted to
incorporate the atmospheric demand and canopy height as continuous
scalars to avoid dependence on land classiﬁcation datasets. Eqs. (9) and
(10) were amended from van Diepen et al. (1989), to account for the
inﬂuences of plant access to deeper water reserves and atmospheric
demand intensifying or mitigating vegetation sensitivity to water
availability(van Diepen et al., 1989). The shape of this response curve
illustrates how canopy height, the potential ET rate, and soil water
availability impact the transpiration rate [Fig. S2]. Additionally, we
apply a weighting scheme using 30-day mean relative humidity and soil
moisture to determine when fM or fTREW are the dominant control on
transpiration globally [Fig. S3]. This approach conserves the intent of
the original model while leveraging the strength of soil moisture information. By weighting the inﬂuence of each scalar, we maintain or
improve transpiration estimates across dry and wet ecohydrological
regimes. The parameters in Eqs. (8), (9), (10), (11), and (12) were not
optimized to the evaluation dataset to maintain model ability to represent ET and soil water limiting conditions globally. The new ecophysiological scalar fTRM in Eq. (12) is combined in series with the
combined stresses from fG and fT.

(6)

LES = [fWET + fREW (1 − fWET )] α

(10)

fTRM = (1 − RH 4(1 − VWC )(1 − RH ) ) fM + (RH 4(1 − VWC )(1 − RH ) ) fTREW

θobs − θwp
θFC − θwp

1
1
−a
1 + PET
1 + CH

(9)
4

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Table 2
Eddy covariance tower characteristics. COSMOS soil moisture observations are taken at or near each of the towers used for in situ forcing evaluation or both. The
towers used for gridded forcing evaluation contain data after 4/2015 and are ordered based on the aridity index calculated as annual potential evapotranspiration
divided by precipitation.
Site

Latitude (°N)

Longitude (°W)

PFT

Time span

Precip (mm)

Temp (°C)

Elevation (m)

Aridity index

Tower use

PI/citation

US-SCs
US-Whs
US-SCg
US-SRM
US-Wkg
US-SCc
US-Ton
US-SRG
US-Var
US-Me2
US-CZ2
US-UMB
US-MOz
US-MMS
US-CZ3
US-Ro1
US-PFa
US-Ho1
US-GLE

33.734
31.743
33.737
31.821
31.736
33.610
38.431
31.789
38.407
44.452
37.031
45.559
38.744
39.323
37.067
44.714
45.945
45.204
41.364

−117.696
−110.052
−117.695
−110.866
−109.941
−116.450
−120.966
−110.828
−120.951
−121.557
−119.256
−84.713
−92.200
−86.413
−119.195
−93.089
−90.2723
−68.740
−106.239

OSH
OSH
GRA
WSA
GRA
OSH
WSA
GRA
GRA
ENF
MF
DBF
DBF
DBF
ENF
CRO
MF
ENF
ENF

2011–2012
2015
2012–2015
2015
2012–2015
2012–2014
2015
2015
2015
2012–2014
2012–2015
2012–2014
2013–2015
2012–2013
2012–2015
2012
2015
2012–2013
2012–2013

375.44
338.54
378.83
409.04
380.01
371.39
610.68
513.79
608.35
555
883.31
770.29
1089.87
1148.53
1033.73
823.02
823
1143.42
953.06

18.545
17.135
18.565
18.445
16.51
15.045
16.39
17.935
16.4
7.215
13.785
6.01
12.8
12.02
9.225
7.535
4.33
5.84
0.245

475
1370
470
1120
1531
1280
177
1291
129
1253
1160
234
219.4
275
2014
260
470
60
3197

3.29
3.08
2.81
2.71
2.43
2.18
1.95
1.87
1.86
1.54
1.29
0.95
0.88
0.83
0.82
0.81
0.77
0.63
0.59

In situ
Grid
In situ
Grid
Both
In situ
Both
Grid
Grid
In situ
In situ
In situ
Both
In situ
In situ
In situ
Grid
In situ
In situ

Goulden, 2017
Scott, 2017a
Goulden, 2017
Scott, 2017b
Scott, 2017c
Goulden, 2017
Baldocchi, 2017a
Scott, 2017d
Baldocchi, 2017b
Law, 2017
Goulden, 2017
Gough et al., 2017
Wood & Gu, 2017
Novick & Phillips, 2017
Goulden, 2017
Baker et al., 2017
Desai, 2017
Hollinger, 2017
Massman, 2017

2016; Oliva et al., 2012).
Soil moisture data are ﬁltered for high-quality data which prevents
using SMAP observations in urban areas, areas with high fractions of
surface water, areas impacted by radio frequencies in the same microwave wavelengths as SMAP, and densely forested or highly productive
agricultural regions where vegetation water content is high. The densely forested and agriculture regions that have high vegetation water
content suﬀer from degraded surface soil moisture retrieval accuracy
from space. However, many of these areas exist in regions with abundant water availability and high humidity, which mitigates potential
issues of data value for ET modeling globally.

repository (http://ameriﬂux.lbl.gov) and the FLUXNET data center
(http://ﬂuxnet.ﬂuxdata.org). Table 1 describes the spatial extent and
frequency characteristics of each dataset used in this study. Table 2
details the eddy covariance towers from Ameriﬂux used in this analysis
including site locations, plant functional types, and climate and terrain
sampled for the areas used to support this analysis.
3.1.1. Modis NDVI (MOD13A2 & MYD13A2)
The normalized diﬀerence vegetation index (NDVI) facilitates
monitoring vegetation green up and senescence. The MOD13C21 and
MYD13C1 data products from MODIS, when combined, provide NDVI
observations at 8-day and 0.05° from the Terra and Aqua satellites from
2000 to present for global estimates (Didan, 2015a; Didan, 2015b). For
in situ model runs, we use the Oak Ridge National Laboratory MODIS
land product subset tool to extract higher spatial resolution (250 m)
NDVI observations from MOD13A1 and MYD13A1 for each eddy covariance tower location, or tower principal investigator suggested representative pixel (http://daac.ornl.gov/MODIS/). All NDVI data are
ﬁltered for only high-quality observations and linearly interpolated for
daily application.

3.1.4. Soil properties
The soil properties used in this study are from the SMAP L4RZ dataset and sourced from the Harmonized World Soil Database version
1.2.1 (HWSD1.21) and the State Soil Geographic project (STATSGO2).
These data have been re-gridded to the EASE-2 grid to maintain consistency with the SMAP Level 2 retrieval algorithms (Das et al., 2013).
For the 36-km runs, we use the nested mean of the 9-km soil properties.
Soil properties extracted from this dataset include the porosity and the
wilting point.

3.1.2. Canopy height (ICESat/GLAS)
Global observations of canopy height (1-km2) are used to model
plant sensitivity to surface soil moisture. This canopy height dataset
was generated with observations spanning 2003 to 2009 from the
Geoscience Laser Altimeter System (GLAS) on the Ice, Cloud, and land
Elevation Satellite (Simard et al., 2011). We spatially average this dataset to each of the EASE grids used in this study to model vegetation
sensitivity to surface soil moisture.

3.1.5. MERRA2: net radiation, temperature, vapor pressure
Net radiation, air temperature, and vapor pressure data from
MERRA2 reanalysis datasets M2T1NXLND and M2T1NXASM were used
in this study. The MERRA2 reanalysis data provides 3-hourly data at a
0.5° latitude × 0.625° longitude global grid. We take a daily average air
temperature, water vapor pressure, and net radiation, daytime maximum temperature and net radiation, and daytime minimum water
vapor pressure and resample these data to the EASE grid resolutions (9km and 36-km) to complete this study. Resampling meteorological data
to ﬁner spatial resolutions introduces uncertainty but is required due to
the lack of continuous global datasets. Global ET quantiﬁcation continues to rely on continuous forcing datasets from reanalysis datasets
(Anderson et al., 2011; Martens et al., 2017; Mu et al., 2011). Therefore, the quality of the computed ET ultimately is dependent on the
accuracy of each reanalysis variable and the subsequent potential biases
including the density of observation networks in North America and
Europe (Badgley et al., 2015).

3.1.3. SMAP surface soil moisture (SPL3SMP & SPL3SMP_E)
We use two SMAP soil moisture data products: SMAP_L3_SM_P and
SMAP_L3_SM_P_E. The SMAP Level 3 Radiometer Global Daily 36 km
EASE-Grid Soil Moisture Version 4 and the SMAP Enhanced Level 3
Radiometer Global Daily 9 km EASE-Grid Soil Moisture Version 1 datasets were used to compare with in situ observations and model ET
globally for this study (O'Neill et al., 2016a; O'Neill et al., 2016b). Each
dataset provides global coverage every 3 days. The SMAP mission leveraged lessons from previous soil moisture observing satellites such as
the Soil Moisture and Ocean Salinity (SMOS) to incorporate radio frequency interference detection and mitigation to provide more continuous high quality global coverage of soil moisture (Mohammed et al.,
5

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Fig. 2. In situ model performance across 14 Ameriﬂux eddy covariance sites distributed across the US. The PT-JPLSM model is shown with orange and the original
model is shown in blue. Sites are ordered based on their aridity index from top (more dry) to bottom (more wet) [Table 2]. PT-JPLSM better estimates ET at more arid
locations compared to PT-JPL [Table 3].

integrated observations of soil moisture, ET, and meteorological data
from EC towers facilitates model updates and evaluation.
We use observations from 14 EC sites that cover 7 plant functional
types and varying climatic conditions. Half of the 14 sites are classiﬁed
as water limited based on the Budyko Classiﬁcation where the aridity
index, calculated as the mean annual potential evapotranspiration divided by the mean annual precipitation, is > 1. We supplement the
meteorological observations of FLUXNET and soil moisture observations from COSMOS with satellite observations of vegetation characteristics. Vegetation observations of CH and NDVI are extracted from
satellite sources at 1-km resolution (http://daac.ornl.gov/MODIS/).
Table 2 provides the site locations, plant functional types, terrain,
and climate sampled of the locations. We indicate whether the site was
used to evaluate model updates using in situ evaluation, gridded forcing
variables, or both in situ and gridded forcing variables. In situ LE evaluations were only performed for sites with high quality meteorology,
soil moisture, and LE observations with at least 1 year of data. Gridded
forcing assessments were performed for sites with LE observations since

3.2. Ameriﬂux and COSMOS: in situ evaluation datasets
Eddy covariance observations of LE with coincident integrated
measures of soil moisture are used for model evaluation [Table 2].
Many EC towers that are part of these networks measure soil moisture
with 1 to 4 dielectric sensors. With limited observations, the inherent
variability in soil moisture adds observational uncertainty with potential to confound model formulation and parameterizations (Ryu and
Famiglietti, 2005). Soil moisture variability increases with spatial extent and during the transition from saturated to dry conditions, conditions critical for the success of modeling soil water control on ET
(Famiglietti et al., 2008). The COsmic-ray Soil Moisture Observing
System (COSMOS) overcomes issues of spatial representativeness by
using observations of cosxmic-ray neutrons to measure soil moisture at
integrated scales similar to the footprints of ET measurements from EC
towers (Köhli et al., 2015; Zreda et al., 2012, 2008). Additionally, these
observations have been used to validate SMAP observations within
expected mission error limits (Montzka et al., 2017). Coincident
6

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

both PT-JPL and PT-JPLSM shows strong agreement with observations
[Fig. 2, Table 3]. Fig. 2 compares one year of mid-day modeled LE with
in situ observations from 14 EC towers. Sites are ordered from dry (top)
to wet (bottom) based on the aridity index, a ratio of annual precipitation to PET. The PT-JPLSM model demonstrates greater skill than
PT-JPL model at water limited sites [Table 3]. On average the PT-JPLSM
shows a decrease in BIAS (PT-JPL: 70.7 Wm−2, PT-JPLSM: 23.8 Wm−2),
a large decrease in RMSE (PT-JPL: 87.8 Wm−2, PT-JPLSM: 40.9 Wm−2)
and an increase in explanation of variance (PT-JPL: 0.59, PT-JPLSM:
0.75) when compared to the PT-JPL. Mean annual BIAS, RMSE, and
explanation of variance improved across all water limited sites. The
greatest overall statistical improvement was observed at US-SCs and
US-SCg. Both of these sites have very dry conditions and a large fraction
of LE comes from soil evaporation. Additionally, the years examined for
these sites were part of the multi-year California drought, which exacerbated the importance of soil moisture to model LE. In addition to
US-SCs and US-SCg, the largest improvements in explanation of variance occurred US-Ton, US-Me2, and US-CZ2. At the US- Ton, US-Me2,
and US-CZ2 the PT-JPLSM model demonstrates improvements to model
estimation of LE during the seasonal dry down. Lastly, at US-SCc and
US-Wkg LE response to short interval precipitation events is best
modeled by PT-JPLSM where increases and subsequent dry down of soil
moisture control LE [Fig. S4].
For the mesic to wet sites (US-UMB, US-Moz, US-MMS, US-CZ3, USRo1, US-Ho1, US-GLE) the PT-JPLSM shows, on average, a small decrease in BIAS (PT-JPL: 34.3 Wm−2, PT-JPLSM: 33.7 Wm−2), a small
decrease in RMSE (PT-JPL: 53.6 Wm−2, PT-JPLSM: 53.4 Wm−2), and a
small decrease in explanation of variance (PT-JPL: 0.86, PT-JPLSM 0.81)
when compared to PT-JPL. For very wet regions, we posit transpiration
from vegetation at these EC tower locations is more sensitive to atmospheric conditions and phenological changes than ﬂuctuations in
surface soil water availability. For these locations, the model weighting
scheme places more importance on fM as a control on transpiration. The
PT-JPLSM model shows reduced errors at US-CZ3 with soil moisture
limitations. This site was in the midst of a multi-year drought with the
forest moving towards water-limiting conditions providing support for
use of soil moisture for water limiting regimes. For wet forested sites
(US-MMS and US-Ho1), we ﬁnd changes to the model resulted in an
increase in error for mid-day LE estimates. However, the increased errors (15% and 10% LE) still fall within mid-day LE observational uncertainty for these sites (Hollinger and Richardson, 2005; Oliphant
et al., 2004). The results from these sites demonstrate soil moisture has
no added value in areas of high soil water availability. Overall, the new
algorithm results in an improvement of model skill for mesic to wet
sites.
We ﬁnd site-wide average improvement in BIAS, RMSE, and R2 as a
result of model improvements. Additionally, incorporating explicit soil
moisture improved estimates of mean monthly LE [Fig. 3]. The PTJPLSM model shows greater explanation of variance (PT-JPL: 0.70, PTJPLSM: 0.78) and a slope (PT-JPL: 1.26, PT-JPLSM: 1.07) closer to 1.0
compared to the PT-JPL model. Observations between 0 and 150 Wm−2
are better represented by the new model with a scatter closer to the 1:1
line from reduced overestimation in LE. Since the algorithm models
each component separately, we quantify the added value from incorporating soil moisture into soil evaporation and canopy transpiration separately. We ﬁnd by only replacing LES, BIAS is reduced by 30%,
RMSE is reduced by 23%, and explanation of variance improves by
4.7%. By only replacing LET, BIAS is reduced by 30%, RMSE is reduced
by 17%, and explanation of variance is reduced by 0.9%. The results of
modeling LE using in situ forcing data demonstrates value in surface soil
moisture observations for modeling ET. Next, we evaluate PT-JPLSM
with gridded meteorology and surface soil moisture observations from
SMAP with in situ LE observations and compared to the original model.

Table 3
PT-JPL and PT-JPLSM performance as indicated by BIAS, RMSE, and R2.
Site

US-SCs
US-SCg
US-Wkg
US-SCc
US-Ton
US-Me2
US-CZ2
US-UMB
US-Moz
US-MMS
US-CZ3
US-Ro1
US-Ho1
US-GLE
AI > 1
AI < 1
All sites

PT-JPL

PT-JPLSM
2

BIAS

RMSE

R2

51.9
4.6
6.9
16.2
20.0
6.4
60.7
19.3
41.8
65.7
9.0
22.4
62.6
14.8
23.8
33.7
28.7

60.90
38.40
24.30
21.60
33.20
33.40
74.90
54.50
48.60
70.50
35.60
37.10
79.50
48.20
40.96
53.43
47.19

0.64
0.36
0.96
0.78
0.88
0.82
0.79
0.85
0.97
0.96
0.63
0.96
0.85
0.48
0.75
0.81
0.78

BIAS

RMSE

R

137.8
105.5
21.4
54.0
67.3
21.1
87.9
29.4
43.3
52.5
33.7
19.1
46.4
15.4
70.7
34.3
52.5

145.10
137.90
27.60
56.30
75.90
65.20
106.60
50.30
49.40
57.60
60.20
40.00
62.00
55.90
87.80
53.63
70.71

0.37
0.01
0.94
0.76
0.79
0.65
0.63
0.90
0.97
0.97
0.62
0.90
0.88
0.79
0.59
0.86
0.73

Fig. 3. Monthly scatter plot of ET model without (blue) and with (orange) soil
moisture.

March 31, 2015, the start date of SMAP observations. Data availability
from Ameriﬂux in situ observations during this time period and the
SMAP recommended quality ﬂag limit the number of sites used in this
analysis. These constraints limited the available tower observations to 8
locations distributed across the continental United States. Numerous
studies have examined the impact on eddy covariance tower footprint
to gridded forcing data mismatches, but this type of analysis is outside
of the scope of the current study (Amiro, 1998; Chen et al., 2009). Since
eddy covariance observations of LE suﬀer from energy closure imbalance, we force energy balance closure daily (Foken et al., 2011;
Twine et al., 2000).

4. Results
4.1. Model evaluation with in situ forcing
The PT-JPL and PT-JPLSM models were executed daily for in situ
evaluation and global analyses with SMAP. The in situ modeled LE from
7

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Fig. 4. Model evaluation at 6 Ameriﬂux EC towers with gridded forcing data. A 3-day moving average is applied to all datasets. Observations are shown in black, ET
modeled with PT-JPLSM using SMAP_L3_P_E shown in blue, and PT-JPLSM using SMAP_L3_P shown in red. The PT-JPL model is shown in cyan (9-km) and green (36km).

(blue) with the PT-JPL model at 9 km (cyan) and 36 km (green) and the
site observations from 4/1/2015 to 12/31/2016. Both the PT-JPLSM
and PT-JPL models capture the seasonal cycle of LE for each EC tower
[Fig. 4]. Table 4 provides summary statistics for each location.
Similar to the in situ analysis, PT-JPLSM demonstrates improved
seasonal dry down and response to precipitation events with both 9-km
and 36-km products. For two sites that experience a Mediterranean
climate (US-Ton & US-Var), where winter precipitation precedes spring
warm up, PT-JPLSM shows an earlier decrease in modeled LE during
seasonal dry downs when using SMAP data. These improvements are
reﬂected in lower error and higher explanation of variance for PT-JPLSM
when compared to PT-JPL at both US-Ton and US-Var [Table 4]. At USWhs, US-Wkg, US-SRG, US-Ton, and US-Var we ﬁnd PT-JPLSM model
evaluated at 9-km shows better agreement with observations compared
to the 36-km data [Table 4]. Poor model performance is observed for
PT-JPLSM and PT-JPL at US-SRM. We posit that underestimation of
modeled LE using SMAP data at the US-SRM might be due in situ LE
observations not being representative over the heterogeneous area, a
result from non-representative soil properties controlling the point at
which soil moisture limits ET (e.g. wilting point), or an underestimation
of soil moisture from SMAP. For the more humid sites, US-PFa and USMOz, where soil water availability is non-limiting, the PT-JPLSM model
shifts the transpiration weight towards the original model formulation
which is more reliant on atmospheric conditions and phenological
change. For these sites, similar to the in situ analysis we see similar
model errors and explanation of variance for both the 9 km and 36 km
results, but higher estimates of LE from the PT-JPLSM algorithm resulting in greater error at US-Pfa and slightly greater LE error within the
range of observational uncertainty at US-MOz. Site-wide mean statistics
indicate that when compared to PT-JPL, PT-JPLSM reduces error by 2%
and 2% for both 9 km and 36 km estimates and increases explanation of

Table 4
PT-JPL and PT-JPLSM model performance evaluation for both 9 km and 36 km
resolutions compared with 8 sites from Fig. 4.
Site

9 km

36 km

PT-JPL

US-Whs
US-SRM
US-Wkg
US-Ton
US-SRG
US-Var
US-Pfa
US-MOz
All site mean

PT-JPL

PT-JPLSM

PT-JPLSM

RMSE

R2

RMSE

R2

RMSE

R2

RMSE

R2

15.1
25.4
21.7
17.7
22.2
21.8
32.9
22.4
22.4

0.16
0.34
0.29
0.36
0.40
0.11
0.51
0.75
0.36

12.4
33.9
20.6
14.2
20.9
11.9
38.8
23.4
22.0

0.38
0.39
0.43
0.29
0.58
0.48
0.51
0.73
0.47

15.0
27.1
25.0
29.8
28.7
34.7
32.0
22.1
26.8

0.17
0.39
0.26
0.18
0.36
0.03
0.52
0.73
0.33

20.2
27.7
32.1
19.3
26.2
21.9
39.4
23.7
26.3

0.37
0.44
0.33
0.19
0.57
0.18
0.52
0.72
0.41

4.2. Model evaluation of global PT-JPLSM using SMAP soil moisture
The PT-JPL and PT-JPLSM algorithms were successfully applied
globally using the SMAP SM_L3_P and SM_L3_P_E data. We only evaluate the gridded PT-JPL and PT-JPLSM for times when SMAP observations are available (e.g. we mask out days in PT-JPL for when SMAP
data do not exist). We avoid temporal interpolation in the evaluation to
prevent erroneous results. For example, interpolation during dry down
events is predictable, but considerable error might be introduced interpolating before and after precipitation would lead to underestimation of total LE. Therefore we evaluate the modeled LE forced by
the two SMAP soil moisture data products and at eight EC validation
sites that meet SMAP QA/QC for 2015 [Table 2]. Fig. 4 compares the
PT-JPLSM model using soil moisture from SM_L3_P (red) and SM_L3_P_E
8

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

surrounding the tropical belt compared to PT-JPL. These regions are
dominated by transpiration and we posit that weighting moisture stress
based on a ‘greenness’ index equally with soil moisture lessened phenological control on LEC [Fig. 5]. EC observations were not available in
these regions for this study to determine if the diﬀerences result in
model improvement or degradation. The largest decreases of LE from
PT-JPLSM compared to PT-JPL occur in regions, where soil evaporation
makes up the largest fraction of ET. These areas include the Southwest
United States and Northern Mexico, the East Coast of Brazil, Northern
Africa, Southern Africa, The Horn of Africa, western Asia and Central
Australia [Fig. 5]. The largest decreases from PT-JPLSM occur in
summer months for each respective region [Fig. S5]. These diﬀerences
highlight the limited ability of fSM to represent relative extractable
water for daily ET modeling and highlight the value in calculating REW
from using SMAP observations. Based on the results of the in situ evaluation and the gridded evaluation [Section 4.1], we ﬁnd support that
the reduced soil evaporation better reﬂects true ET magnitudes for
these regions.
5. Discussion
5.1. Inter-annual variability of ET for 2015–2017
Global LE datasets provide a valuable tool to quantify hydrological
and ecological responses to climate perturbations. We analyze interannual variability of LE during the peak months of the 2015–2016 El
Niño intensity and compare the data to the following year [Fig. 6].
Previous studies have used LE to measure global hydrological response
to El Niño. During El Niño years, global average negative LE anomalies
occur relative to average LE (Miralles et al., 2014). We ﬁnd that PTJPLSM mean global LE for the 2015–2016 El Niño was 1.7% less than
the following year. Fig. 7 shows the change in mean annual LE for both
PT-JPL and PT-JPLSM. For areas identiﬁed as having warmer or drier
than average conditions during El Niño Years, such as Australia, Indonesia, Southeastern Africa, we ﬁnd negative anomalies, e.g. lower LE
when compared with the subsequent La Niña year (Vecchi and
Wittenberg, 2010). In water-limited regions expected to experience
more precipitation during El Niño, such as Argentina and the South
West USA, we ﬁnd positive LE anomalies. Similar response patterns
prevail across both PT-JPL and PT-JPLSM. However, we ﬁnd subtle
changes in areas such as Australia, India, and Eastern Brazil. These
areas show similar signs of change, but transitional boundaries are
changes which reﬂect changes in soil water availability. Interestingly
we ﬁnd increases in LE across the tropics, which contrast patterns of
decreases in LE found by Miralles et al. (2014). Despite these regions
experiencing decreases in precipitation, increased incoming radiation
produced greater LE than the following year. As these regions are regions known as being energy-limited, contrasting LE datasets and
models create an opportunity for future exploration into the controlling
mechanisms of LE across these regions (Nemani et al., 2003). The PTJPLSM LE data show the potential ability to distinguish explicit interannual changes in LE as a result of soil water limitation and serve as a
tool to identify vegetation stress and drought intensity. Overall, PTJPLSM demonstrates the value of using soil moisture within LE models
for capturing seasonal changes, especially in drier regions where soil
moisture exerts greater control on inter-annual variation.

Fig. 5. Mean annual PT-JPLSM ET for 2016 using SMAP_L3_P_E (top), mean
annual PT-JPL ET for 2016 (middle) and PT-JPLSM-PT-JPL diﬀerence (bottom).
ET data are evaluated on the 9-km EASE 2.0 Grid.

variance by 30.1% and 18.1% for the 9 km and 36 km forcing datasets
respectively. Additionally, Table 4 shows PT-JPLSM LE modeled at 9 km
results in lower error and higher explanation of variance compared to
LE modeled at 36 km. Despite the soil moisture from SM_L3_P_E (9 km)
being inﬂuenced by L-band microwave radiation from a larger area, the
observed soil moisture data are more centered on tower locations
compared to coarser the SM_L3_P (36-km) demonstrating added value
for ET quantiﬁcation. The limited number of validation sites prevented
a robust global evaluation. Therefore, we perform a global inter-comparison between LE generated from the original PT-JPL model and new
PT-JPLSM model. Using this analysis, we demonstrate when and where
soil water-limiting conditions create the greatest disparity for global LE
quantiﬁcation, how soil moisture impacts LE partitioning, and how LE
modeled with soil moisture impacts inter-annual variability.
4.3. Changes in global ET patterns from SMAP data

5.2. ET partitioning
We compare the PT-JPL and PT-JPLSM for 2016 modeled on the 9km grid surface. Fig. 5 shows ET from each model for 2016 and the
diﬀerence between the models. Both PT-JPL and PT-JPLSM show expected global patterns of ET. Globally, ET is greatest in the tropics
lowest at mid-latitudes. Model diﬀerences are evaluated spatially to
determine where PT-JPLSM LE is greater than or less than the PT-JPL LE.
PT-JPLSM modeled LE increases compared to PT-JPL in Boreal Canada,
Northern and Eastern India, South America and Africa in areas

Appropriate partitioning of ET into transpiration, canopy interception, and soil evaporation is an overlooked area of ET science, yet
greatly important to appropriately model these mechanistic responses
to environmental conditions. Fig. 7 shows the fraction of transpiration,
interception, and soil evaporation globally and each components contribution to mean annual LE. The top map illustrates the percent contribution from each component and reveals expected global patterns of
9

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Fig. 6. Inter-annual variation in PT-JPL (left) and PT-JPLSM (right) LE. Top) 2015–2016 mean LE during El Niño. Middle) 2016–2017 mean LE. Bottom) Diﬀerence in
LE.

water retention curve is less steep than sandy and loamy soils where the
slope of the soil water retention curve is much greater (Hillel, 2013).
Further in depths studies should focus on the mechanisms controlling
transpiration and interception as well. Transpiration and the impact
from deﬁcits of soil water availability continues to be a great area of
need for further analyses (Talsma et al., 2018). For transpiration, uncertainty of rooting depth and density limits applications of processbased modeling of water movement from soil through plants to the
atmosphere (Schenk and Jackson, 2002). Balancing large scale changes
with plant-speciﬁc resiliency depends on the underlying covariation in
soil moisture and root distributions. Future observations of soil
moisture and canopy transpiration as well as synthesized datasets oﬀer
a path towards model improvement (e.g. SAPFLUX, eddy covariance
observations, & COSMOS) (Poyatos et al., 2016). Additionally, leveraging isotope observations may serve as a boundary to further guide
development of model partitioning. Only when each component of ET
partitioning is measured separately with low uncertainty will satellitedriven ET model partitioned components begin to be properly constrained.

dominant ET components (e.g. soil evaporation is greatest in deserts,
transpiration is dominant in forested regions, and interception is a large
fraction in rainforests). Previous ET model partitioning estimates estimate transpiration to be between 25% and 65% (Wang and Dickinson,
2012) and recent remote sensing algorithms estimate transpiration to
be as high as 80% of ET globally (Miralles et al., 2011). We estimate soil
evaporation, canopy transpiration, and evaporation from interception
to be 23 ± 1.7%, 54 ± 1.6%, and 21 ± 0.8% of total ET annually respectively. The PT-JPLSM fraction of soil evaporation and canopy interception are greater than similarly reported fractions from GLEAM
model 7–15% and 11–12% respectively (Martens et al., 2017; Miralles
et al., 2011). Additionally, we calculate a lower fraction of canopy
transpiration 54% compared to GLEAM (74–80%). The large disparity
in soil evaporation and canopy transpiration can be traced to the radiation partitioning and the forcing datasets that inﬂuence RNC and RNS
and the environmental stress imparted on the transpiration rate. We
posit that the diﬀerence in canopy intercepted evaporation occurs as a
result of the model's dependence on RH to calculate fWET. Coarse resolution meteorological forcing resampled to ﬁner spatial resolutions
introduces larger fractions of wet surface area, especially in coastal and
tropical regions where regions are more inﬂuenced by water vapor
pressure. Despite these diﬀerences in ET partitioning, we ﬁnd the global
patterns to be similar. These large diﬀerences warrant further investigation into appropriate partitioning methodology across biomes
and climates. More ground-based observations of each component at
scales relevant for modeling and remote-sensing comparison are needed
to reign in this large uncertainty.
The assumptions built into the models might over/under-estimate
certain variables (e.g. temperature, water availability) impact on ET and
each of its components. With regard to soil evaporation, we use the
wilting point instead of the hygroscopic point to limit soil evaporation.
By using the wilting point instead of the hygroscopic point, this might
introduce a possible overestimation of soil moisture limitation on soil
evaporation for clay and peat soils (e.g. clay and peat) where the soil

6. Conclusion
We present an update to the widely used PT-JPL ET model to address one of the model's main gaps: the implicit representation of soil
water control. We incorporate soil moisture constraints on evaporation
and transpiration. In situ analyses demonstrate the largest improvements for ET estimates in dry regions. We apply SMAP soil moisture
observations to model ET globally using PT-JPLSM. The PT-JPLSM model
shows improved model performance when compared to ground observations. Finer spatial resolution soil moisture observations at 9 km
from the SMAP Level 3 Passive Enhanced product resulted in reduced
LE error and increased explanation of variance compared LE forced
with the 36 km SMAP Level 3 Passive product. The soil moisture constraint resulted in lower global estimates of evaporation and
10

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

Fig. 7. Evapotranspiration components as expressed as a percentage of total ET. Red indicates more soil evaporation, blue indicates more transpiration, yellow
indicates more canopy interception evaporation. Below, total contribution to annual ET from transpiration, soil evaporation, and interception.

et al., 2014, 2012; Poulter et al., 2014). The lower estimates provide a
more accurate dataset to quantify water use eﬃciency and track impacts from drought and climate perturbations such as El Niño events.
The updated PT-JPLSM ET model shows expected patterns of changes in
ET for El-Niño and La Niña years. Based on the results in this study we
conclude that modiﬁcations to the PT-JPL algorithm to include soil

transpiration for water-limited regions. These lower ET estimates have
implications for feedbacks between the water cycle and the carbon
cycle. Arid and semi-arid regions have been identiﬁed as a major contributor to the inter-annual variability in CO2 uptake and are key areas
to better understand how strong coupling between land-atmosphere
moisture exchange impacts carbon uptake (Levine et al., 2016; Miralles
11

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

moisture produce more realistic ET estimates globally. This dataset
provides the opportunity to identify vegetation vulnerable to drought
and water limiting conditions.

modelling vs. sequential data assimilation. Hydrol. Earth Syst. Sci. 21, 4861–4878.
https://doi.org/10.5194/hess-21-4861-2017.
Didan, K., 2015a. MOD13C1 MODIS/Terra Vegetation Indices 16-Day L3 Global 0.05Deg
CMG V006 [Data set]. NASA EOSDIS LP DAAChttps://doi.org/10.5067/MODIS/
MOD13C1.006.
Didan, K., 2015b. MYD13C1 MODIS/Aqua Vegetation Indices 16-Day L3 Global 0.05Deg
CMG V006 [Data set]. NASA EOSDIS LP DAAChttps://doi.org/10.5067/MODIS/
MYD13C1.006.
Entekhabi, D., Njoku, E.G., O'Neill, P.E., Kellogg, K.H., Crow, W.T., Edelstein, W.N.,
Entin, J.K., Goodman, S.D., Jackson, T.J., Johnson, J., Kimball, J., Piepmeier, J.R.,
Koster, R.D., Martin, N., McDonald, K.C., Moghaddam, M., Moran, S., Reichle, R., Shi,
J.C., Spencer, M.W., Thurman, S.W., Tsang, L., Van Zyl, J., 2010. The soil moisture
active passive (SMAP) mission. Proc. IEEE 98, 704–716. https://doi.org/10.1109/
JPROC.2010.2043918.
Ershadi, A., McCabe, M.F., Evans, J.P., Chaney, N.W., Wood, E.F., 2014. Multi-site evaluation of terrestrial evaporation models using FLUXNET data. Agric. For. Meteorol.
187, 46–61. https://doi.org/10.1016/j.agrformet.2013.11.008.
Famiglietti, J.S., Ryu, D., Berg, A.A., Rodell, M., Jackson, T.J., 2008. Field observations of
soil moisture variability across scales. Water Resour. Res. 44. https://doi.org/10.
1029/2006WR005804.
Fan, Y., Miguez-Macho, G., Jobbágy, E.G., Jackson, R.B., Otero-Casal, C., 2017.
Hydrologic regulation of plant rooting depth. Proc. Natl. Acad. Sci. 201712381.
https://doi.org/10.1073/pnas.1712381114.
Fisher, J.B., Tu, K.P., Baldocchi, D.D., 2008. Global estimates of the land-atmosphere
water ﬂux based on monthly AVHRR and ISLSCP-II data, validated at 16 FLUXNET
sites. Remote Sens. Environ. 112, 901–919. https://doi.org/10.1016/j.rse.2007.06.
025.
Fisher, J.B., Melton, F., Middleton, E., Hain, C., Anderson, M., Allen, R., McCabe, M.F.,
Hook, S., Baldocchi, D., Townsend, P.A., Kilic, A., Tu, K., Miralles, D.D., Perret, J.,
Lagouarde, J.-P., Waliser, D., Purdy, A.J., French, A., Schimel, D., Famiglietti, J.S.,
Stephens, G., Wood, E.F., 2017. The future of evapotranspiration: global requirements for ecosystem functioning, carbon and climate feedbacks, agricultural management, and water resources. Water Resour. Res. 53, 2618–2626. https://doi.org/
10.1002/2016WR020175.
Foken, T., Aubinet, M., Finnigan, J.J., Leclerc, M.Y., Mauder, M., Paw U, K.T., 2011.
Results of a panel discussion about the energy balance closure correction for trace
gases. Bull. Am. Meteorol. Soc. https://doi.org/10.1175/2011BAMS3130.1.
Giardina, F., Konings, A.G., Uriarte, M., Oliveira, R.S., Gentine, P., 2017. Tall Amazonian
forests are more resistant to precipitation variability. Nat. Geosci. https://doi.org/10.
1038/s41561-018-0133-5. in review.
GMAO, 2015a. MERRA-2 tavg1_2d_ﬂx_Nx: 2d, 1-hourly, time-averaged, single-level, assimilation, surface ﬂux diagnostics V5.12.4. Goddard Earth Sciences Data and
Information Services Center (GES DISC)https://doi.org/10.5067/7MCPBJ41Y0K6 ,
Accessed date: 1 May 2016.
GMAO, 2015b. MERRA-2 inst1_2d_lfo_Nx: 2d, 1-hourly, instantaneous, single-level, assimilation, land surface forcings v5.12.4. Goddard Earth Sciences Data and
Information Services Center (GES DISC)https://doi.org/10.5067/RCMZA6TL70BG ,
Accessed date: 1 May 2016.
Gough, Christopher, Bohrer, Gil, Curtis, Peter, 2017. AmeriFlux US-UMB Univ. of Mich.
Biological Station. https://doi.org/10.17190/AMF/1246107.
Goulden Lab, 2017. http://www.ess.uci.edu/~california.
Goulden, M.L., Bales, R.C., 2014. Mountain runoﬀ vulnerability to increased evapotranspiration with vegetation expansion. Proc. Natl. Acad. Sci. 111, 14071–14075.
https://doi.org/10.1073/pnas.1319316111.
Goulden, M.L., Anderson, R.G., Bales, R.C., Kelly, a.E., Meadows, M., Winston, G.C., 2012.
Evapotranspiration along an elevation gradient in California's Sierra Nevada. J.
Geophys. Res. 117, G03028. https://doi.org/10.1029/2012JG002027.
Greve, P., Seneviratne, S.I., 2015. Assessment of future changes in water availability and
aridity. Geophys. Res. Lett. 42, 5493–5499. https://doi.org/10.1002/
2015GL064127.
Hillel, D., 2013. Fundamentals of soil physics. In: Fundamentals of Soil Physics, https://
doi.org/10.1016/C2009-0-03109-2.
Hollinger, David, 2017. AmeriFlux US-Ho1 Howland Forest (main tower). https://doi.
org/10.17190/AMF/1246061.
Hollinger, D.Y., Richardson, A.D., 2005. Uncertainty in eddy covariance measurements
and its application to physiological models. Tree Physiol. 873–885. https://doi.org/
10.1093/treephys/25.7.873.
Huntington, T.G., 2006. Evidence for intensiﬁcation of the global water cycle: Review and
synthesis. J. Hydrol. https://doi.org/10.1016/j.jhydrol.2005.07.003.
Jackson, R.B., Moore, L.A., Hoﬀmann, W.A., Pockman, W.T., Linder, C.R., 1999.
Ecosystem rooting depth determined with caves and DNA. Proc. Natl. Acad. Sci. U. S.
A. 96, 11387–11392. https://doi.org/10.1073/pnas.96.20.11387.
Jarvis, P.G., Mcnaughton, K.G., 1986. Stomatal control of transpiration: scaling up from
leaf to region. Adv. Ecol. Res. 15, 1–49. https://doi.org/10.1016/S0065-2504(08)
60119-1.
Jin, Y., Randerson, J.T., Goulden, M.L., 2011. Continental-scale net radiation and evapotranspiration estimated using MODIS satellite observations. Remote Sens. Environ.
115, 2302–2319. https://doi.org/10.1016/j.rse.2011.04.031.
Johnson, J.T., Mohammed, P.N., Piepmeier, J.R., Bringer, A., Aksoy, M., 2016. Soil
moisture active passive (SMAP) microwave radiometer radio-frequency interference
(RFI) mitigation: algorithm updates and performance assessment. In: International
Geoscience and Remote Sensing Symposium (IGARSS), pp. 123–124. https://doi.org/
10.1109/IGARSS.2016.7729022.
Jung, M., Reichstein, M., Ciais, P., Seneviratne, S.I., Sheﬃeld, J., Goulden, M.L., Bonan,
G., Cescatti, A., Chen, J., de Jeu, R., Dolman, A.J., Eugster, W., Gerten, D., Gianelle,
D., Gobron, N., Heinke, J., Kimball, J., Law, B.E., Montagnani, L., Mu, Q., Mueller, B.,

Acknowledgements
AJP was supported by the NASA Earth and Space Science Fellowship
17-EARTH17R-0062 and the SUSMAP and INCA programs. JBF contributed to this research from the Jet Propulsion Laboratory, California
Institute of Technology, under a contract with the National Aeronautics
and Space Administration. California Institute of Technology.
Government sponsorship acknowledged. JBF was supported in part by
NASA's SUSMAP, INCA, IDS, GRACE, and ECOSTRESS programs.
Copyright 2018. All rights reserved. We thank an anonymous reviewer
and Brecht Martens for critiques beneﬁcial to the advancement of this
manuscript.
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://
doi.org/10.1016/j.rse.2018.09.023.
References
Allen, R.G., Tasumi, M., Trezza, R., 2007. Satellite-Based Energy Balance for Mapping
Evapotranspiration With Internalized Calibration, METRIC…— Model 380–395.
Amiro, B.D., 1998. Footprint climatologies for evapotranspiration in a boreal catchment.
Agric. For. Meteorol. 90, 195–201. https://doi.org/10.1016/S0168-1923(97)
00096-8.
Anderson, M.C., Norman, J.M., Mecikalski, J.R., Otkin, J.A., Kustas, W.P., 2007. A climatological study of evapotranspiration and moisture stress across the continental
United States based on thermal remote sensing: 1. Model formulation. J. Geophys.
Res. Atmos. 112. https://doi.org/10.1029/2006JD007506.
Anderson, R.G., Canadell, J.G., Randerson, J.T., Jackson, R.B., Hungate, B. a, Baldocchi,
D.D., Ban-Weiss, G. a, Bonan, G.B., Caldeira, K., Cao, L., Diﬀenbaugh, N.S., Gurney,
K.R., Kueppers, L.M., Law, B.E., Luyssaert, S., O'Halloran, T.L., 2011. Biophysical
considerations in forestry for climate protection. Front. Ecol. Environ. 9, 174–182.
https://doi.org/10.1890/090179.
Anderson, M.C., Hain, C., Otkin, J., Zhan, X., Mo, K., Svoboda, M., Wardlow, B., Pimstein,
A., 2013. An intercomparison of drought indicators based on thermal remote sensing
and NLDAS-2 simulations with U.S. drought monitor classiﬁcations. J.
Hydrometeorol. 14, 1035–1056. https://doi.org/10.1175/JHM-D-12-0140.1.
Badgley, G., Fisher, J.B., Jiménez, C., Tu, K.P., Vinukollu, R., 2015. On uncertainty in
global terrestrial evapotranspiration estimates from choice of input forcing datasets*.
J. Hydrometeorol. 16, 1449–1455. https://doi.org/10.1175/JHM-D-14-0040.1.
Baker, John, Griﬃs, Tim, Griﬃs, Timothy, 2017. AmeriFlux US-Ro1 Rosemount- G21.
https://doi.org/10.17190/AMF/1246092.
Baldocchi, Dennis, 2017a. AmeriFlux US-Ton Tonzi Ranch. https://doi.org/10.17190/
AMF/1245971.
Baldocchi, Dennis, 2017b. AmeriFlux US-Var Vaira Ranch- Ione. https://doi.org/10.
17190/AMF/1245984.
Baldocchi, D., Falge, E., Gu, L., Olson, R., Hollinger, D., Running, S., Anthoni, P.,
Bernhofer, C., Davis, K., Evans, R., Fuentes, J., Goldstein, A., Katul, G., Law, B., Lee,
X., Malhi, Y., Meyers, T., Munger, W., Oechel, W., Paw, U.K.T., Pilegaard, K., Schmid,
H.P., Valentini, R., Verma, S., Vesala, T., Wilson, K., Wofsy, S., 2001. FLUXNET: a
new tool to study the temporal and spatial variability of ecosystem-scale carbon dioxide, water vapor, and energy ﬂux densities. Bull. Am. Meteorol. Soc. 82,
2415–2434. https://doi.org/10.1175/1520-0477(2001)082<2415:FANTTS>2.3.
CO;2.
Canadell, J., Jackson, R.B., Ehleringer, J.B., Mooney, H.A., Sala, O.E., Schulze, E.-D.,
1996. Maximum rooting depth of vegetation types at the global scale. Oecologia 108,
583–595. https://doi.org/10.1007/BF00329030.
Chen, B., Black, T.A., Coops, N.C., Hilker, T., Trofymow, J.A., Morgenstern, K., 2009.
Assessing tower ﬂux footprint climatology and scaling between remotely sensed and
eddy covariance measurements. Bound.-Layer Meteorol. 130, 137–167. https://doi.
org/10.1007/s10546-008-9339-1.
Colliander, A., Cosh, M.H., Misra, S., Jackson, T.J., Crow, W.T., Chan, S., Bindlish, R.,
Chae, C., Holiﬁeld Collins, C., Yueh, S.H., 2017. Validation and scaling of soil
moisture in a semi-arid environment: SMAP validation experiment 2015
(SMAPVEX15). Remote Sens. Environ. 196, 101–112. https://doi.org/10.1016/j.rse.
2017.04.022.
Das, N., 2013. Soil Moisture Active Passive (SMAP) Ancillary Data Report Soil Attributes.
SMAP science document no. 044. Jet Propulsion Laboratory. California Institute of
Technology.
Desai, A., 2017. AmeriFlux US-PFa Park Falls/WLEF. https://doi.org/10.17190/AMF/
1246090.
Dewaele, H., Munier, S., Albergel, C., Planque, C., Laanaia, N., Carrer, D., Calvet, J.C.,
2017. Parameter optimisation for a better representation of drought by LSMs: inverse

12

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

O'Neill, P.E., Chan, S., Njoku, E.G., Jackson, T., Bindlish, R., 2016a. SMAP Enhanced L3
Radiometer Global Daily 9 km EASE-Grid Soil Moisture. [Indicate subset used].
NASA National Snow and Ice Data Center Distributed Active Archive Center, Boulder,
Colorado USA. https://doi.org/10.5067/ZRO7EXJ8O3XI. [1/7/2017]. Version 1.
O'Neill, P.E., Chan, S., Njoku, E.G., Jackson, T., Bindlish, R., 2016b. SMAP L3 Radiometer
Global Daily 36 km EASE-Grid Soil Moisture, Version 4. [Indicate subset used].
Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active
Archive Center. doi: http://dx.doi.org/10.5067/OBBHQ5W22HME. [1/7/2017].
[Indicate subset used] In: SMAP L3 Radiometer Global Daily 36 km EASE-Grid Soil
Moisture. NASA National Snow and Ice Data Center Distributed Active Archive
Center, Boulder, Colorado USA. https://doi.org/10.5067/OBBHQ5W22HME. [1/7/
2017] Version 4.
Oliphant, A.J., Grimmond, C.S.B., Zutter, H.N., Schmid, H.P., Su, H.-B., Scott, S.L.,
Oﬀerle, B., Randolph, J.C., Ehman, J., 2004. Heat storage and energy balance ﬂuxes
for a temperate deciduous forest. Agric. For. Meteorol. 126, 185–201. https://doi.
org/10.1016/j.agrformet.2004.07.003.
Oliva, R., Daganzo-Eusebio, E., Kerr, Y.H., Mecklenburg, S., Nieto, S., Richaume, P.,
Gruhier, C., 2012. SMOS radio frequency interference scenario: status and actions
taken to improve the RFI environment in the 1400-1427-MHZ passive band. IEEE
Trans. Geosci. Remote Sens. 50, 1427–1439. https://doi.org/10.1109/TGRS.2012.
2182775.
Padilla, F.M., Pugnaire, F.I., 2007. Rooting depth and soil moisture control Mediterranean
woody seedling survival during drought. Funct. Ecol. 21, 489–495. https://doi.org/
10.1111/j.1365-2435.2007.01267.x.
Piepmeier, J.R., Johnson, J.T., Mohammed, P.N., Bradley, D., Ruf, C., Aksoy, M., Garcia,
R., Hudson, D., Miles, L., Wong, M., 2014. Radio-frequency interference mitigation
for the soil moisture active passive microwave radiometer. IEEE Trans. Geosci.
Remote Sens. 52, 761–775. https://doi.org/10.1109/TGRS.2013.2281266.
Poulter, B., Frank, D., Ciais, P., Myneni, R.B., Andela, N., Bi, J., Broquet, G., Canadell,
J.G., Chevallier, F., Liu, Y.Y., Running, S.W., Sitch, S., van der Werf, G.R., 2014.
Contribution of semi-arid ecosystems to interannual variability of the global carbon
cycle. Nature 509, 600–603. https://doi.org/10.1038/nature13376.
Poyatos, R., Granda, V., Molowny-Horas, R., Mencuccini, M., Steppe, K., Martínez-Vilalta,
J., 2016. SAPFLUXNET: towards a global database of sap ﬂow measurements. Tree
Physiol. 36, 1449–1455. https://doi.org/10.1093/treephys/tpw110.
Priestley, C., Taylor, R., 1972. On the assessment of surface heat ﬂux and evaporation
using large-scale parameters. Mon. Weather Rev. 81–92. https://doi.org/10.1175/
1520- 0493.
Purdy, A.J., 2018. Improvements to and Applications of Remotely Sensed
Evapotranspiration. Univ. California, Irvine.
Purdy, A.J., Fisher, J.B., Goulden, M.L., Famiglietti, J.S., 2016. Ground heat ﬂux: an
analytical review of 6 models evaluated at 88 sites and globally. J. Geophys. Res.
Biogeosci. 121, 3045–3059. https://doi.org/10.1002/2016JG003591.
Qiu, J., Crow, W.T., Nearing, G.S., 2016. The impact of vertical measurement depth on
the information content of soil moisture for latent heat ﬂux estimation. J.
Hydrometeorol. 17, 2419–2430. https://doi.org/10.1175/JHM-D-16-0044.1.
Rodell, M., McWilliams, E.B., Famiglietti, J.S., Beaudoing, H.K., Nigro, J., 2011.
Estimating evapotranspiration using an observation based terrestrial water budget.
Hydrol. Process. 25, 4082–4092. https://doi.org/10.1002/hyp.8369.
Ryu, D., Famiglietti, J.S., 2005. Characterization of footprint-scale surface soil moisture
variability using Gaussian and beta distribution functions during the Southern Great
Plains 1997 (SGP97) hydrology experiment. Water Resour. Res. 41, 1–13. https://
doi.org/10.1029/2004WR003835.
Schenk, H.J., Jackson, R.B., 2002. Rooting depths, lateral root spreads and belowground
aboveground allometries of plants in water limited ecosystems. J. Ecol. 480–494.
https://doi.org/10.1046/j.1365-2745.2002.00682.x.
Scott, Russell, 2017a. AmeriFlux US-SRG Santa Rita Grassland. https://doi.org/10.
17190/AMF/1246154.
Scott, Russell, 2017b. AmeriFlux US-SRM Santa Rita Mesquite. https://doi.org/10.
17190/AMF/1246104.
Scott, Russell, 2017c. AmeriFlux US-Wkg Walnut Gulch Kendall Grasslands. https://doi.
org/10.17190/AMF/1246112.
Scott, Russell, 2017d. AmeriFlux US-Whs Walnut Gulch Lucky Hills Shrub. https://doi.
org/10.17190/AMF/1246113.
Simard, M., Pinto, N., Fisher, J.B., Baccini, A., 2011. Mapping forest canopy height
globally with spaceborne lidar. J. Geophys. Res. Biogeosci. 116. https://doi.org/10.
1029/2011JG001708.
Sorooshian, S., Li, J., Hsu, K.L., Gao, X., 2011. How signiﬁcant is the impact of irrigation
on the local hydroclimate in Californias Central Valley? Comparison of model results
with ground and remote-sensing data. J. Geophys. Res. Atmos. 116. https://doi.org/
10.1029/2010JD014775.
Su, Z., 2002. The surface energy balance system (SEBS) for estimation of turbulent heat
ﬂuxes. Hydrol. Earth Syst. Sci. 6, 85–100. https://doi.org/10.5194/hess-6-85-2002.
Syed, T.H., Famiglietti, J.S., Chambers, D.P., Willis, J.K., Hilburn, K., 2010. Satellitebased global-ocean mass balance estimates of interannual variability and emerging
trends in continental freshwater discharge. Proc. Natl. Acad. Sci. 107, 17916–17921.
https://doi.org/10.1073/pnas.1003292107.
Talsma, C.J., Good, S.P., Jimenez, C., Martens, B., Fisher, J.B., Miralles, D.G., McCabe,
M.F., Purdy, A.J., 2018. Partitioning of evapotranspiration in remote sensing-based
models. Agric. For. Meteorol. https://doi.org/10.1016/j.agrformet.2018.05.010.
Twine, T.E.E., Kustas, W.P.P., Norman, J.M.M., Cook, D.R.R., Houser, P.R.R., Meyers,
T.P.P., Prueger, J.H.H., Starks, P.J.J., Wesely, M.L.L., 2000. Correcting eddy-covariance ﬂux underestimates over a grassland. Agric. For. Meteorol. 103, 279–300.
https://doi.org/10.1016/S0168-1923(00)00123-4.
van Diepen, C.A., Wolf, J., van Keulen, H., Rappoldt, C., 1989. WOFOST: a simulation
model of crop production. Soil Use Manag. 5, 16–24. https://doi.org/10.1111/j.

Oleson, K., Papale, D., Richardson, A.D., Roupsard, O., Running, S., Tomelleri, E.,
Viovy, N., Weber, U., Williams, C., Wood, E., Zaehle, S., Zhang, K., 2010. Recent
decline in the global land evapotranspiration trend due to limited moisture supply.
Nature 467, 951–954. https://doi.org/10.1038/nature09396.
Kelliher, F.M., Leuning, R., Schulze, E.D., 1993. Evaporation and canopy characteristics of
coniferous forests and grasslands. Oecologia. https://doi.org/10.1007/BF00323485.
Kerr, Y.H., Al-Yaari, A., Rodriguez-Fernandez, N., Parrens, M., Molero, B., Leroux, D.,
Bircher, S., Mahmoodi, A., Mialon, A., Richaume, P., Delwart, S., Al Bitar, A.,
Pellarin, T., Bindlish, R., Jackson, T.J., Rüdiger, C., Waldteufel, P., Mecklenburg, S.,
Wigneron, J.P., 2016. Overview of SMOS performance in terms of global soil
moisture monitoring after six years in operation. Remote Sens. Environ. 180, 40–63.
https://doi.org/10.1016/j.rse.2016.02.042.
Knoop, W.T., Walker, B.H., 1985. Interactions of woody and herbaceous vegetation in a
southern African savanna. J. Ecol. 73, 235–253. https://doi.org/10.2307/2259780.
Köhli, M., Schrön, M., Zreda, M., Schmidt, U., Dietrich, P., Zacharias, S., 2015. Footprint
characteristics revised for ﬁeld-scale soil moisture monitoring with cosmic-ray neutrons. Water Resour. Res. 51, 5772–5790. https://doi.org/10.1002/2015WR017169.
Law, Bev, 2017. AmeriFlux US-Me2 Metolius mature ponderosa pine. https://doi.org/10.
17190/AMF/1246076.
Levine, P.A., Randerson, J.T., Swenson, S.C., Lawrence, D.M., 2016. Evaluating the
strength of the land-atmosphere moisture feedback in earth system models using
satellite observations. Hydrol. Earth Syst. Sci. 20, 4837–4856. https://doi.org/10.
5194/hess-20-4837-2016.
Lo, M.H., Famiglietti, J.S., 2013. Irrigation in California's Central Valley strengthens the
southwestern U.S. water cycle. Geophys. Res. Lett. 40, 301–306. https://doi.org/10.
1002/grl.50108.
Martens, B., Miralles, D.G., Lievens, H., Van Der Schalie, R., De Jeu, R.A.M., FernándezPrieto, D., Beck, H.E., Dorigo, W.A., Verhoest, N.E.C., 2017. GLEAM v3: satellitebased land evaporation and root-zone soil moisture. Geosci. Model Dev. 10,
1903–1925. https://doi.org/10.5194/gmd-10-1903-2017.
Massman, Bill, 2017. AmeriFlux US-GLE GLEES. https://doi.org/10.17190/AMF/
1246056.
McDowell, N.G., 2011. Mechanisms linking drought, hydraulics, carbon metabolism, and
vegetation mortality. Plant Physiol. 155, 1051–1059. https://doi.org/10.1104/pp.
110.170704.
Michel, D., Jiménez, C., Miralles, D.G., Jung, M., Hirschi, M., Ershadi, A., Martens, B.,
Mccabe, M.F., Fisher, J.B., Mu, Q., Seneviratne, S.I., Wood, E.F., Fernández-Prieto, D.,
2016. The WACMOS-ET project - part 1: tower-scale evaluation of four remote-sensing-based evapotranspiration algorithms. Hydrol. Earth Syst. Sci. 20, 803–822.
https://doi.org/10.5194/hess-20-803-2016.
Miralles, D.G., De Jeu, R.A.M., Gash, J.H., Holmes, T.R.H., Dolman, A.J., 2011.
Magnitude and variability of land evaporation and its components at the global scale.
Hydrol. Earth Syst. Sci. 15, 967–981. https://doi.org/10.5194/hess-15-967-2011.
Miralles, D.G., Van Den Berg, M.J., Teuling, A.J., De Jeu, R.A.M., 2012. Soil moisturetemperature coupling: a multiscale observational analysis. Geophys. Res. Lett. 39.
https://doi.org/10.1029/2012GL053703.
Miralles, D.G., Teuling, A.J., van Heerwaarden, C.C., Vilà-Guerau de Arellano, J., 2014.
Mega-heatwave temperatures due to combined soil desiccation and atmospheric heat
accumulation. Nat. Geosci. 7, 345–349. https://doi.org/10.1038/ngeo2141.
Mohammed, P.N., Aksoy, M., Piepmeier, J.R., Johnson, J.T., Bringer, A., 2016. SMAP Lband microwave radiometer: RFI mitigation prelaunch analysis and ﬁrst year on-orbit
observations. IEEE Trans. Geosci. Remote Sens. 54, 6035–6047. https://doi.org/10.
1109/TGRS.2016.2580459.
Monteith, J.L.L., 1965. Evaporation and environment. Symp. Soc. Exp. Biol. 19, 205–234.
https://doi.org/10.1613/jair.301.
Montzka, C., Bogena, H.R., Zreda, M., Monerris, A., Morrison, R., Muddu, S., Vereecken,
H., 2017. Validation of spaceborne and modelled surface soil moisture products with
cosmic-ray neutron probes. Remote Sens. 9. https://doi.org/10.3390/rs9020103.
Mu, Q., Zhao, M., Running, S.W., 2011. Improvements to a MODIS global terrestrial
evapotranspiration algorithm. Remote Sens. Environ. 115, 1781–1800. https://doi.
org/10.1016/j.rse.2011.02.019.
Mu, Q., Zhao, M., Kimball, J.S., McDowell, N.G., Running, S.W., 2013. A remotely sensed
global terrestrial drought severity index. Bull. Am. Meteorol. Soc. 94, 83–98. https://
doi.org/10.1175/BAMS-D-11-00213.1.
Mueller, B., Hirschi, M., Jimenez, C., Ciais, P., Dirmeyer, P.A., Dolman, A.J., Fisher, J.B.,
Jung, M., Ludwig, F., Maignan, F., Miralles, D.G., McCabe, M.F., Reichstein, M.,
Sheﬃeld, J., Wang, K., Wood, E.F., Zhang, Y., Seneviratne, S.I., 2013. Benchmark
products for land evapotranspiration: LandFlux-EVAL multi-data set synthesis.
Hydrol. Earth Syst. Sci. 17, 3707–3720. https://doi.org/10.5194/hess-17-3707-2013.
Nemani, R.R., Keeling, C.D., Hashimoto, H., Jolly, W.M., Piper, S.C., Tucker, C.J., Myneni,
R.B., Running, S.W., 2003. Climate-driven increases in global terrestrial net primary
production from 1982 to 1999. Science 300, 1560–1563. https://doi.org/10.1126/
science.1082750.
Nepstad, D.C., de Carvalho, C.R., Davidson, E.A., Jipp, P.H., Lefebvre, P.A., Negreiros,
G.H., da Silva, E.D., Stone, T.A., Trumbore, S.E., Vieira, S., 1994. The role of deep
roots in the hydrological and carbon cycles of Amazonian forests and pastures. Nature
372, 666–669. https://doi.org/10.1038/372666a0.
Njoku, E.G., Jackson, T.J., Lakshmi, V., Chan, T.K., Nghiem, S.V., 2003. Soil moisture
retrieval from AMSR-E. IEEE Trans. Geosci. Remote Sens. 41, 215–228. https://doi.
org/10.1109/TGRS.2002.808243.
Novick, Kim, Phillips, Rich, 2017. AmeriFlux US-MMS Morgan Monroe State Forest.
https://doi.org/10.17190/AMF/1246080.
Novick, K.A., Ficklin, D.L., Stoy, P.C., Williams, C.A., Bohrer, G., Oishi, A.C., Papuga, S.A.,
Blanken, P.D., Noormets, A., Sulman, B.N., Scott, R.L., Wang, L., Phillips, R.P., 2016.
The increasing importance of atmospheric demand for ecosystem water and carbon
ﬂuxes. Nat. Clim. Chang. 6, 1023–1027. https://doi.org/10.1038/nclimate3114.

13

Remote Sensing of Environment 219 (2018) 1–14

A.J. Purdy et al.

INTRODUCTION.
Wood, Jeﬀrey, Gu, Lianhong, 2017. AmeriFlux US-MOz Missouri Ozark Site. https://doi.
org/10.17190/AMF/1246081.
Zreda, M., Desilets, D., Ferré, T.P.A., Scott, R.L., 2008. Measuring soil moisture content
non-invasively at intermediate spatial scale using cosmic-ray neutrons. Geophys. Res.
Lett. 35. https://doi.org/10.1029/2008GL035655.
Zreda, M., Shuttleworth, W.J., Zeng, X., Zweck, C., Desilets, D., Franz, T., Rosolem, R.,
2012. COSMOS: the cosmic-ray soil moisture observing system. Hydrol. Earth Syst.
Sci. 16, 4079–4099. https://doi.org/10.5194/hess-16-4079-2012.

1475-2743.1989.tb00755.x.
Vecchi, G.A., Wittenberg, A.T., 2010. El Niño and our future climate: where do we stand?
Wiley Interdiscip. Rev. Clim. Chang. 1, 260–270. https://doi.org/10.1002/wcc.33.
Vinukollu, R.K., Wood, E.F., Ferguson, C.R., Fisher, J.B., 2011. Global estimates of evapotranspiration for climate studies using multi-sensor remote sensing data: evaluation of three process-based approaches. Remote Sens. Environ. 115, 801–823.
https://doi.org/10.1016/j.rse.2010.11.006.
Wang, K., Dickinson, R.E., 2012. A review of global terrestrial evapotranspiration: observation. J. Geophys. Res. Lett. https://doi.org/10.1029/2011RG000373.1.

14

