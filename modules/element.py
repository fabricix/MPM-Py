#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Represent a finite element

"""
class bar_1D:

	"""
	Represent an 1D finite element with 2 nodes

	Attributes
	----------

	eid : int
		Element identification

	n1 : node
		Node 1 (left)

	n2 : node
		Node 2 (right)

	L : float
		Element length

	particles : list
		List of particles in the element
	"""

	def __init__(self):
		
		self.eid = 0 # element id 
		self.n1 = 0  # node 1 (left)
		self.n2 = 0  # node 2 (right)
		self.L = 0   # element length
		self.particles = [] # list of particles in element