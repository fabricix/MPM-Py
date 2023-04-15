#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This module defines nodal shape functions and its derivative

"""

def NiLinear(x,xI,L):
	"""
	Calculates the values of the linear interpolation function

	Arguments
	---------
	x: float
		point to calculate the function
	xI: float
		nodal point position
	L: float
		grid cell spacing
	"""
	
	if(abs(x-xI)>=L):
		return 0
	
	if(-L<(x-xI) and (x-xI)<=0):
		return 1+(x-xI)/L
	
	if(0<(x-xI) and (x-xI)<L):
		return 1-(x-xI)/L

def dNiLinear(x,xI,L):
	"""
	Calculates the values of the linear interpolation function gradient
	
	Arguments
	---------
	x: float
		point to calculate the function
	xI: float
		nodal point position
	L: float
		grid cell spacing
	"""
	
	if(abs(x-xI)>=L):
		return 0
	
	if(-L<(x-xI) and (x-xI)<=0):
		return 1/L
	
	if(0<(x-xI) and (x-xI)<L):
		return -1/L

def sgn(a):
	"""
	Sign function

	Arguments
	---------
	a : float
		Value
	"""
	if a<0.0:
		return -1.0
	else:
		return 1.0

def NicpGIMP(L,lp,xp,xi):
	"""
	Calculates contiguous GIMP shape function value
	
	Arguments
	---------

	L : float
		cell spacing
	lp : float
		half of current particle size
	xp : float
		particle position
	xi : float
		node position
	"""
	
	s = xp-xi

	if abs(s)>=(L+lp):
		return 0
		
	if (-L-lp)<s and s<=(-L+lp):
		return ((L+lp+s)**2)/(4*L*lp)
	
	if (-L+lp)<s and s<=(-lp):
		return 1 + (s/L)

	if (-lp)<s and s<=lp:
		return 1 - (s**2 + lp**2)/(2*L*lp)
	
	if lp<s and s<=(L-lp):
		return 1 - (s/L)

	if (L-lp)<s and s<=(L+lp):
		return ((L+lp-s)**2)/(4*L*lp)


def dNicpGIMP(L,lp,xp,xi):
	"""
	Calculates the gradient of the contiguous particle GIMP shape functions 
	
	Arguments
	---------

	L : float
		cell spacing
	lp : float
		half of current particle size
	xp : float
		particle position
	xi : float
		node position
	"""

	s = xp-xi

	if abs(s)>=(L+lp):
		return 0
	
	if (-L-lp)<s and s<=(-L+lp):
		return (L+lp+s)/(2*L*lp)
	
	if (-L+lp)<s and s<=(-lp):
		return 1/L
	
	if (-lp)<s and s<=lp:
		return -s/(L*lp)
	
	if lp<s and s<=(L-lp):
		return -1/L
	
	if (L-lp)<s and s<=(L+lp):
		return -(L+lp-s)/(2*L*lp)

def test_interpolation_functions(x1,x2,xI,L,shape_type):
	"""
	Tests the interpolation functions Ni and its gradients dNi

	Arguments
	---------
	x1 : float
		initial particle position
	x2 : float
		final particle position
	xI : float
		fixed node position
	L  : float
		element length
	shape_type: string
		interpolation function type, may be 'linear' or 'cpGIMP'
	"""
	import numpy as np
	import matplotlib.pyplot as plt

	# particle position	
	x = np.linspace(x1,x2,num=500);

	# interpolation function values and its gradients
	ni = np.zeros_like(x)
	dni = np.zeros_like(x)

	# linear shape function
	if (shape_type=='linear'):
		for i in range(len(x)):
			ni[i]  = NiLinear(x[i],xI,L)
			dni[i] = dNiLinear(x[i],xI,L)
	
	# cpGIMP shape function
	elif (shape_type=='cpGIMP'):
		for i in range(len(x)):
			ni[i]  = NicpGIMP(L,L/4,x[i],xI)
			dni[i] = dNicpGIMP(L,L/4,x[i],xI)

	plt.plot(x,ni,'-r',label=r'$N_I$')
	plt.plot(x,dni,'-b',label=r'$dN_I/dx$')
	plt.plot(x,np.zeros_like(x),'--k')
	plt.title("Interpolation functions and its derivatives")
	plt.legend()
	plt.ylabel(r"$N_I$, $dN_I/dx$")
	plt.xlabel(r"x")
	plt.show()

def get_interpolation_functions(x1,x2,xI,L,shape_type):
	"""
	Returns the interpolation functions Ni and its gradients dNi

	Arguments
	---------
	x1 : float
		initial particle position
	x2 : float
		final particle position
	xI : float
		fixed node position
	L  : float
		element length
	shape_type: string
		interpolation function type, may be 'linear' or 'cpGIMP'
	"""
	import numpy as np
	import matplotlib.pyplot as plt

	# particle position	
	x = np.linspace(x1,x2,num=500);

	# interpolation function values and its gradients
	ni = np.zeros_like(x)
	dni = np.zeros_like(x)

	# linear shape function
	if (shape_type=='linear'):
		for i in range(len(x)):
			ni[i]  = NiLinear(x[i],xI,L)
			dni[i] = dNiLinear(x[i],xI,L)
	
	# cpGIMP shape function
	elif (shape_type=='cpGIMP'):
		for i in range(len(x)):
			ni[i]  = NicpGIMP(L,L/4,x[i],xI)
			dni[i] = dNicpGIMP(L,L/4,x[i],xI)

	return [x, ni, dni]