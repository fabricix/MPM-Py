#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
Compute the analytical solution of a single mass point vibration

Arguments
---------
L : float
	Bar length
E : float
	Young's modulus
rho : float
	density
time : float
	total time
dt : float
	time step
xo : float
	initial position
vo : float
	initial velocity

Data
----
Created on Thu Mar 18 16:57:57 2021

Author
------
Fabricio Fernandez <fabricio.hmf@gmail.com>

"""

# import external modules
import numpy as np

def single_mass_point_vibration_solution(L,E,rho,time,dt,xo,vo):
	""" calculate the single mass point vibration solution """

	# frequency of the system
	w = (1.0/L)*((E/rho)**0.5)

	# mass position in time
	xt = []
	t  = []

	# initial time
	ti = 0

	# compute the exact solution
	while ti<time:

		#particle position
		xt.append(xo*np.exp(vo/(L*w)*np.sin(w*ti)))

		t.append(ti)
		
		ti+=dt

	return [xt, t]