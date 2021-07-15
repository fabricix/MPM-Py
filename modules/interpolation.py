#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""

Defines interpolation functions in order to transfer quantities from particles to nodes.

This functions, have the general form:

.. math::
	f_I = \sum_p N_I(x_p) f_p

where,
$$f_I$$: is a nodal quantity,
$$f_p$$: is a particle quantity, and
$$N_I(x_p)$$: is the weight or interpolation function of the node *I* evaluated at particle position $$x_p$$

"""

def Ni(x,xI,L):
	"""
	Calculate the values of the interpolation function

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

def dNi(x,xI,L):
	"""
	Calculate the values of the interpolation function gradient.
	
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
	
def test(x1,x2,xI,L):
	"""
	Function to test the interpolation functions Ni and its gradients
	dNi.
	
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
	"""
	import numpy as np
	import matplotlib.pyplot as plt
	
	x = np.linspace(x1,x2,num=500);
	
	ni = np.zeros_like(x)
	dni = np.zeros_like(x)
	
	for i in range(len(x)):    
		ni[i]  = Ni(x[i],xI,L)
		dni[i] = dNi(x[i],xI,L)
	
	plt.plot(x,ni,'-r',label=r'$N_I$')
	plt.plot(x,dni,'-b',label=r'$dN_I/dx$')
	plt.plot(x,np.zeros_like(x),'--k')
	plt.legend()
	plt.show()
	
def mass_to_nodes(msh):
	"""
	Interpolate mass from particles to nodes.

	Arguments
	---------
	msh: mesh
		a mesh object
	"""
	for ie in msh.elements:
		for ip in ie.particles:

			ie.n1.mass+=ip.mass*ip.N1
			ie.n2.mass+=ip.mass*ip.N2
	
	
def momentum_to_nodes(msh):
	"""
	Interpolate momentum from particles to nodes.

	Arguments
	---------
	msh: mesh
		a mesh object
	"""  
	for ie in msh.elements:
		for ip in ie.particles:
			
			ie.n1.momentum+=ip.mass*ip.velocity*ip.N1
			ie.n2.momentum+=ip.mass*ip.velocity*ip.N2    
			
			
def internal_force_to_nodes(msh):
	"""
	Interpolate internal forces from particles to nodes.

	Arguments
	---------
	msh: mesh
		a mesh object
	"""   
	for ie in msh.elements:
		for ip in ie.particles:
			
			ie.n1.f_int-=ip.dN1*ip.stress*ip.mass/ip.density
			ie.n2.f_int-=ip.dN2*ip.stress*ip.mass/ip.density

def external_force_to_nodes(msh):
	"""
	Interpolate external forces from particles to nodes.

	Arguments
	---------
	msh: mesh
		a mesh object
	"""
	for ie in msh.elements:
		for ip in ie.particles:
		
			ie.n1.f_ext+=ip.N1*ip.f_ext
			ie.n2.f_ext+=ip.N2*ip.f_ext