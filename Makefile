SHELL := /bin/bash
# use bash for <( ) syntax

.PHONY : setup

evolution-2021.slides.html : setup

setup :
	$(MAKE) -C figs
	$(MAKE) -C benchmarking

include rules.mk
