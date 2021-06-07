SHELL := /bin/bash
.PHONY: figs 

figs: msp_folks.png 

msp_folks.png : msp_folks/*
	montage msp_folks/*jpg $@

include ../rules.mk
