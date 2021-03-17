#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:29:59 2021

@author: Fabricio Fernandez 
@e-mail: fabricio.hmf@gmail.com

Purpose
-------
This file defines classes for elements representation

"""
class bar_1D:
    """
    Class to create 1D bar element with 2 nodes

    Attributes
    ----------
    eid : int
    	Element identification
    n1 : node type
    	Node 1 (left)
    n2 : node type
    	Node 2 (right)
    L : float
    	Element length
    particles : list
    	List of particles in element
    """
    def __init__(self):
        self.eid = 0 # element id 
        self.n1 = 0  # node 1
        self.n2 = 0  # node 2
        self.L = 0   # element length
        self.particles = [] # particles in element