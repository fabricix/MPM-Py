#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
Compute the analytical solution of a continuum bar vibration

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
vo : float
	initial velocity
x_sol : float
	position to get the solution

Data
----
Created on Sat Mar 20 20:26:08 2021

Author
------
Fabricio Fernandez <fabricio.hmf@gmail.com>

"""

# import external modules
import numpy as np

def continuum_bar_vibration_solution(L,E,rho,time,dt,vo,x_sol):
	"""calculate the continuum bar vibration solution (mode 1)"""

	# frequency of the system (mode 1)
	w1 = (np.pi/2.0/L)*((E/rho)**0.5)
	b1 = (np.pi/2.0/L)

	# position in time
	xt = []
	vt = []
	t  = []

	# initial time
	ti = 0

	# compute the exact solution
	while ti<time:

		# position
		xt.append(vo/w1*np.sin(w1*ti)*np.sin(b1*x_sol))

		# velocity
		vt.append(vo*np.cos(w1*ti)*np.sin(b1*x_sol))

		# current time
		t.append(ti)
		
		# advance in time
		ti+=dt

	return [xt,vt,t]