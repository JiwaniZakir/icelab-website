---
layout: page
title: research
permalink: /research/
description: Research areas at the ICE Lab — 3-D ICs, hardware security, and near-threshold circuits.
nav: true
nav_order: 4
---

## 3D Integrated Circuits

<div class="row">
<div class="col-sm-8 mt-3 mt-md-0">

There are many design aspects that require consideration and analysis in the development of a three-dimensional integrated circuit. More specifically, when considering power delivery, synchronization, and signalling in a TSV-based 3-D IC, the potential to integrate disparate technologies with independent voltage and peak power requirements, clock speeds, thermal design power, noise requirements, and a slew of other design considerations requires new methodologies and techniques beyond which are used for two-dimensional system-on-chip integrated circuits.

In addition, considerations unique to 3-D ICs such as increased hot spot formation, place and route in the z direction as well as the x and y direction, and more importantly the potential to integrate ICs from different foundaries where not all design information is shared between vendors requires not only novel methodologies and techniques, but also novel circuits at the interface between the heterogeneous device planes. Our group develops circuit design techniques, methodologies, and algorithms at multiple levels of abstraction as well as experimental test vehicles to advance synchronization, power delivery, and signalling in 3-D SoC based circuits.

> **Sub-projects:** TSV modeling, synchronization, clock tree synthesis, power delivery, OCVR clustering, optical interconnect, thermal modeling
{: .block-tip}

[View 3-D IC projects]({{ '/projects/' | relative_url }}#active)

</div>
<div class="col-sm-4 mt-3 mt-md-0">
{% include figure.liquid loading="lazy" path="assets/img/research/3d-ics.jpg" title="3-D Integrated Circuits" class="img-fluid rounded z-depth-1" %}
</div>
</div>

---

## Hardware Security

<div class="row">
<div class="col-sm-4 mt-3 mt-md-0">
{% include figure.liquid loading="lazy" path="assets/img/research/hardware-security.jpg" title="Hardware Security" class="img-fluid rounded z-depth-1" %}
</div>
<div class="col-sm-8 mt-3 mt-md-0">

Modifications to integrated circuits (ICs) or the insertion of foreign intellectual property (i.e. hardware Trojans) pose a serious threat on US sovereignty as ICs are found in many commercial electronic devices including phones, computers, and televisions as well as US assets that rely on ICs for computation or control such as our energy infrastructure, banking, or more importantly defense systems.

The primary goal of our research group on hardware security and trust is to secure US electronic assets by assuring that the integrated circuits that are installed do not include functions (or modifications to expected functions) that compromise the IC and more importantly the systems that rely on these ICs. We aim to address hardware security by both prevention of attacks (including IP piracy and information theft) through circuit level techniques, and active detection of malicious circuitry. Our group is developing circuit techniques and methodologies that can be incorporated by the semiconductor industry to improve the security of ICs through enhanced detection of hardware modifications, countermeasures that disable adversarial circuit components, and simulation infrastructure to analyze the efficacy and cost of security measures such as RTL/circuit obfuscation.

> **Sub-projects:** Run-time detection and countermeasures, design-for-trust algorithms and methodologies
{: .block-tip}

[View hardware security projects]({{ '/projects/' | relative_url }}#active)

</div>
</div>

---

## Sub/Near-Threshold Circuits with Current-Mode Logic

Since power and energy have not scaled similarly to the dimension of the transistor, it has become difficult to operate all transistors simultaneously for a given power budget and time (concept of dark silicon). In addition, the energy and power efficiency of mobile devices is critical to extend usage. One potential solution is to operate circuits in the sub-threshold or near-threshold regime. A reduction in supply voltage reduces dynamic power quadratically and static power exponentially.

However, in the sub-threshold regime, performance degradation, reliability issues, and high leakage power severely affect the overall energy and power improvements. Near-threshold devices are more tolerant to performance degradation and are more reliable, and near-threshold circuits (NTC) are not as energy inefficient as sub-threshold circuits. Current-mode logic (CML) circuits are well known for higher operating speed compared to conventional CMOS, while dynamic current-mode logic (DCML) offers reduced static leakage with competitive delay. Our group explores NTC combined with DCML to trade off power and performance for energy-efficient computing.

> **Sub-projects:** Power reduction using NTC with CML
{: .block-tip}

[View NTC/CML project]({{ '/projects/' | relative_url }}#active)
