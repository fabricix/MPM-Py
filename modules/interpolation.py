#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""

This module defines interpolation functions to transfer quantities from particles to nodes

These functions have the general form:

.. math::
	f_I = \sum_p N_I(x_p) f_p

where,
$$f_I$$: is a nodal quantity,
$$f_p$$: is a particle quantity, and
$$N_I(x_p)$$: is the weight or interpolation function of the node *I* evaluated at particle position $$x_p$$

"""
	
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