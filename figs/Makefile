SHELL := /bin/bash
.PHONY: figs 

figs: msp_folks.png tsk_folks.png

msp_folks.png : msp_folks/*
	montage msp_folks/*jpg $@

tsk_folks.png : tsk_folks/*
	montage tsk_folks/*jpg $@

include ../rules.mk
