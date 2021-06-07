---
title:  "New tools for popgen simulation and analysis: <br/> What's possible?"
author: "Peter Ralph <br/> University of Oregon <br/> Institute of Ecology and Evolution"
date: "Evolution 2021"
---


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


# Overview of simulators

*In this talk:*

- msprime: a coalescent simulator
- SLiM: a forwards simulator

. . .

Other good ones:

- [simbit](LINK)
- [fastsimcoal](LINK)
- [SFS_CODE](LINK)
- [that other one](LINK)
- [geowhatever](LINK)


## Development philosophy

- open, welcoming, supportive
- well-documented
- reliable, reproducible
- backwards compatible


## Forwards or backwards?

::: {.columns}
:::::: {.column width=50%}

forwards simulators

::: 
:::::: {.column width=50%}

coalescent simulators

:::
:::::: 

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

![msprime logo](figures/msprime_logo.png)

![Jerome Kelleher](figures/jerome.jpg)

## New features:

- finite sites
- recombination rate maps
- mutation rate maps
- gene conversion
- nicer demographic model specification

## Ancestry models

- "the" Kingman/Hudson coalescent
- discrete-time Wright-Fisher
- selective sweeps
- multiple mergers


## Mutation models

- infinite sites/alleles
- nucleotides
- amino acids

. . .

tree with fancy mutation model


# SLiM

![SLiM logo](figures/slim_logo.png)
![Ben Haller](figures/ben_haller.png)


## An eco-evolutionary simulator

- ecological dynamics with "non-Wright-Fisher" models
- populations in continuous, heterogeneous geography
- sex chromosomes, haplodiploidy
- complex traits
- context-dependent mutations

##

image of local adaptation


## How to get started

1. read the introduction of the SLiM manual (chapters 1 & 3)
2. find a recipe that's close to what you want to do
3. open up the GUI and try it out

. . .

4. print stuff out in the Eidos console
5. add in bits from other recipes

. . .

6. take a workshop!


# tree sequences

![tskit logo](figures/tskit.png)

## 

Yan's video of a tree sequence

## Benefits of interoperability

- recapitate with msprime
- Add mutations with msprime
- interleave the two

(figure)

##

Now also supported by

- geoXXX
- the other one

# Runtime

## basic demography

- msprime: XXX
- SLiM: seconds per thousand individuals per megabase of genome per thousand generations

## selection

doesn't change much

## spatial simulations:

depends a lot on neighborhood size


# Best practices

## How long to run it for?

what is equilibrium?

when is recapitation ok?

## How to get help

- SLiM: the mailing list

- msprime/tskit: "discussion" on github

