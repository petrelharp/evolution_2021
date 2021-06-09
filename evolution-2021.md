---
title:  "New tools for popgen simulation and analysis: <br/> What's possible?"
author: "Peter Ralph <br/> University of Oregon <br/> Institute of Ecology and Evolution"
date: "Evolution 2021"
---


# Overview of simulators

<!--
- overview of simulators and development
- background on forwards vs coalescent
- bullet points of features
- tree sequences: adding neutral mutations afterwards
- benchmarking for "plain vanilla": how many individuals and how long a genome?
- benchmarking for adding selection to (4) as a function of how much selection
- benchmarking for spatial nonWF: as a function of neighborhood size
- recapitation best practices
-->


*In this talk:*

::: {.columns}
:::::: {.column width=50%}

- [msprime](https://tskit.dev/msprime): a coalescent simulator
- [SLiM](https://messerlab.org/SLiM): a forwards simulator



Other good ones:

- [fwdpy11](https://tskit.dev/fwdpy11)
- [Gspace](http://www1.montpellier.inra.fr/CBGP/software/gspace/download.html)
- [geonomics](https://geonomics.readthedocs.io/en/latest/)
- [simbit](https://github.com/RemiMattheyDoret/SimBit)
- [fastsimcoal](http://cmpg.unibe.ch/software/fastsimcoal2/)
- [SFS_CODE](http://sfscode.sourceforge.net/SFS_CODE/index/index.html)

:::
:::::: {.column width=50%}


![msprime logo](figs/msprime-logo.png){width=80%}

![SLiM logo](figs/slim_logo.png){width=100%}

:::
::::::


## Development philosophy

::: {.columns}
:::::: {.column width=50%}

- open, welcoming, supportive
- well-documented
- reliable, reproducible
- backwards compatible

:::
:::::: {.column width=50%}

![tskit logo](figs/tskit_logo.png){width=80%}

*tskit*: the tree sequence toolkit

::: {.floatright}
[https://tskit.dev](https://tskit.dev)
:::

:::
::::::


## Forwards or backwards?

![](figs/simulation_types.ink.svg){width=100%}

## Forwards or backwards?

Do your digital organisms:

> - have at most one site under selection?
> - live in a collection of randomly-mating populations?
> - not need some specific life cycle?

. . .

If so, then
*coalescent simulation*
is the way to go!


# msprime

![msprime logo](figs/msprime-logo.png)

::: {.floatright}
![jerome kelleher](figs/jerome.jpeg){width=50%}


:::: {.caption}
[Kelleher, Etheridge, & McVean](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004842) 
::::
:::


## msprime v1.0

![msprime collaborators](figs/msp_folks.png)

## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites

::: {.hide}
- recombination rate maps
- gene conversion
- nicer demographic model specification
- mutation rate maps
- quick analysis
:::

:::
:::::: {.column width=50%}

![](figs/example1.png)

:::
::::::

## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites
- recombination rate maps

::: {.hide}
- gene conversion
- nicer demographic model specification
- mutation rate maps
- quick analysis
:::

:::
:::::: {.column width=50%}

![](figs/example2.png)

:::
::::::

## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites
- recombination rate maps
- gene conversion

::: {.hide}
- nicer demographic model specification
- mutation rate maps
- quick analysis
:::

:::
:::::: {.column width=50%}

![](figs/example3.png)

:::
::::::


## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites
- recombination rate maps
- gene conversion
- nicer demographic model specification

::: {.hide}
- mutation rate maps
- quick analysis
:::

:::
:::::: {.column width=50%}

![](figs/example4.png)

:::
::::::

## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites
- recombination rate maps
- gene conversion
- nicer demographic model specification
- mutation rate maps

::: {.hide}
- quick analysis
:::

:::
:::::: {.column width=50%}

![](figs/example5.png)

:::
::::::

## New features:

::: {.columns}
:::::: {.column}

- $k$-ploid individuals, finite sites
- recombination rate maps
- gene conversion
- nicer demographic model specification
- mutation rate maps
- quick analysis

:::
:::::: {.column width=50%}

![](figs/example6.png)

:::
::::::



## Ancestry models

::: {.columns}
:::::: {.column width=40%}

- "the" coalescent
- discrete-time Wright-Fisher
- selective sweeps
- multiple mergers

:::
:::::: {.column width=60%}

::: {.small}

```
sweep_model = msprime.SweepGenicSelection(
    position=2.5e4, s=0.01,
    start_frequency=0.5e-4, end_frequency=0.99, dt=1e-6)
sts = msprime.sim_ancestry(9,
    model=[sweep_model, msprime.StandardCoalescent()],
    population_size=1e4, recombination_rate=1e-8, sequence_length=5e4)
```

:::

:::
::::::

![](figs/sweep_trees.svg)

## Mutation models

::: {.columns}
:::::: {.column width=40%}

- infinite sites/alleles
- nucleotides
- amino acids
- arbitrary Markovian models

:::
:::::: {.column width=60%}

::: {.small}
```
dem = msprime.Demography.from_species_tree(
   "((A:900,B:900)ab:100,C:1000)abc;",
   initial_size=1e3)
samples = {"A": 2, "B": 1, "C": 1}
ts = msprime.sim_ancestry(
   8, demography=dem, sequence_length=5e4,
   recombination_rate=1e-8
)
mts = msprime.sim_mutations(ts, rate=1e-7)
mts.draw_svg()
```
:::

:::
::::::


![](figs/mutated_trees.svg)

# SLiM {data-background-image="figs/slim_screenshot.png" data-background-position=left data-background-size=100%}

## An eco-evolutionary simulator

::: {.columns}
:::::: {.column}

- ecological dynamics with "non-Wright-Fisher" models
- populations in continuous, heterogeneous geography
- sex chromosomes, haplodiploidy
- complex traits
- context-dependent mutations

:::
:::::: {.column width=50%}


![SLiM logo](figs/slim_logo.png){width=80%}

![Ben Haller](figs/ben-haller.jpg){width=30%}

:::{.caption .floatright}
Ben Haller
:::


:::
::::::



## {data-background-image="figs/slim_manual.png" data-background-position=left data-background-size=50%}

::: {.columns}
:::::: {.column width=60%}

:::
:::::: {.column width=40%}

**Getting started:**

1. read the introduction of the SLiM manual
2. find a recipe that's close to what you want
3. open up the GUI and try it
4. print stuff in the console
5. add in other bits
6. take a workshop!


:::
::::::

# tree sequences

![tskit logo](figs/tskit_logo.png){width=30%}

::: {.floatright}
![jerome kelleher](figs/jerome.jpeg){width=50%}


:::: {.caption}
[Kelleher, Etheridge, & McVean](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004842) 
::::
:::

-------

![tskit contributors](figs/tsk_folks.png)


## The tree sequence

![](figs/MCEB-final_animation.mp4)

:::: {.caption}
*video credit: Yan Wong*
::::

## Benefits

::: {.columns}
:::::: {.column}

- extremely efficient for large simulations
- retains genotypes *and* genealogical history

Interoperable: now supported by

- [msprime](https://tskit.dev/msprime/docs/stable/intro.html)
- [SLiM](https://messerlab.org/SLiM)
- [fwdpy11](https://molpopgen.github.io/fwdpy11/intro.html)
- [Gspace](http://www1.montpellier.inra.fr/CBGP/software/gspace/download.html)
- [geonomics](https://geonomics.readthedocs.io/en/latest/)

:::
:::::: {.column width=50%}

![](figs/fire_trees.svg)

:::
::::::


## Post-hoc mutations

![diagram of adding mutations to a tree sequence](figs/add_mutations.svg)

## Recapitation

![diagram of recapitation](figs/recapitation.svg)


# Runtime

## Considerations

- $N$ = population size
- $L$ = genome length
- sample size (doesn't matter much)
- number of generations (SLiM only)
- selection
- geography
- adding neutral mutations (nearly instant)

## msprime: 1000 samples

![](benchmarking/msprime_times_small.png)

*takeaway:* hundreds of thousands of megabases takes seconds

## msprime: 1000 samples

![](benchmarking/msprime_times.png)

*takeaway:* hundreds of thousands of megabases takes seconds

## basic demography: SLiM

![](benchmarking/run_wf_neutral.speeds.png)

*Note:* with **no** mutations

## Basic demography: SLiM

![](benchmarking/run_wf_neutral.speeds_perN.png)

*takeaway:* seconds per thousand individuals per thousand generations

## Selection: SLiM, total rate $10^{-10}$

![](benchmarking/run_wf_selection.speeds_perN.png)

*takeaway:* similar, but slower by a factor of 3 for lots of positive mutations

## Spatial simulations: SLiM

![](benchmarking/run_spatial.speeds.png)

*takeaway:* Slower than genomes!
Scales with neighborhood size ($\sigma^2$).

# Suggestions

## How long to run it for?

> 1. Until equilibrium. (4N? 20N?)
> 2. If that's too long, for a "while", and recapitate.
> 3. Your results shouldn't depend too much on how you do it.

. . .

Big picture: how accurate do you think your demographic model
    reflects 2N generations ago, really?


## How to get help

- SLiM: [the mailing list](https://groups.google.com/forum/#!forum/slim-discuss)

- msprime/tskit: ["discussions" on github](https://github.com/tskit-dev/msprime/discussions)

- Get involved! Suggest features, write documentation, write code...


# Thanks!

::: {.columns}
:::::: {.column}

![BDI](figs/bdi.png){ width=30% }

![NHGRI](figs/nih.jpeg)


:::
:::::: {.column width=50%}

![tskit logo](figs/tskit_logo.png){width=50%}

- Jerome Kelleher
- Ben Haller
- Ben Jeffery
- Yan Wong
- Murillo Rodrigues
- Andy Kern
- Philipp Messer

:::
::::::



