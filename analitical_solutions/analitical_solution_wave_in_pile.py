#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
Compute the analytical solution of a wave traveling in a pile

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
po : float
	external load
x_sol : float
	position to get the solution

Data
----
Created on Mon Jul 19 08:58:30 2021

Author
------
Fabricio Fernandez <fabricio.hmf@gmail.com>

"""

# import external modules
import numpy as np

def wave_in_pile_fixed_and_loaded(L,E,rho,time,dt,po,x):
	"""calculate the solution of the wave equation in a pile"""

	# Poisson's ratio in 1D is assumed to be equal to 0
	nu=0

	# bulk modulus
	K = E*(1-nu)/(1+nu)/(1-2*nu)

	# wave velocity
	c = np.sqrt(K/rho)

	# position an velocity in time
	xt = []
	vt = []
	t  = []

	# initial time
	ti = 0

	# compute the exact solution
	while ti<time:
		
		# displacement and velocity summation
		u_wave_sum = 0
		v_wave_sum = 0
        
		for n in range(1,100):

			lam = (2*n-1)*np.pi/2/L
			
			u_wave_sum+=((-1)**n)/((2*n-1)**2)*np.sin(lam*x)*np.cos(lam*c*ti)
			
			v_wave_sum-=(-1)**n/((2*n-1)**2)*lam*c*np.sin(lam*x)*np.cos(lam*c*ti)
		
		# displacement
		u_wave = po/K*(x+8*L/(np.pi**2)*u_wave_sum)

		# velocity
		v_wave = po*8*L/K/np.pi**2*v_wave_sum

		# position
		xt.append(u_wave+x)

		# velocity
		vt.append(v_wave)

		# current time
		t.append(ti)
		
		# advance in time
		ti+=dt

	return [xt,vt,t]



## test

# external modules
#import matplotlib.pyplot as plt # for plot

#[anal_xt,anal_vt, anal_t] = wave_in_pile_fixed_and_loaded(L=1,E=150,rho=1,time=0.5,dt=0.1,po=-0.1,x=0.005)
#plt.plot(anal_t,anal_xt,'r',linewidth=2,label='analytical')

# configure axis, legends and show plot
#plt.xlabel('time (s)')
#plt.ylabel('position (m)')
#plt.legend()
#plt.show()
