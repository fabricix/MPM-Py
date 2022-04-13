#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Represents a node in a finite element mesh

"""

class node_1D:
    """
    Represent a 1D node
    
    Attributes
    ---------
    nid : int
        node identification

    x : float
        position

    velocity : float
        nodal velocity

    mass : float
        nodal mass

    momentum : float
        nodal momentum (mass*velocity)

    f_int : float
        nodal internal force

    f_ext : float
        nodal external force
        
    f_tot  : float
        total force
    """
    def __init__(self):
        
        self.nid = 0
        self.x = 0  
        self.velocity = 0  
        self.mass = 0  
        self.momentum = 0  
        self.f_int = 0
        self.f_ext = 0
        self.f_tot = 0