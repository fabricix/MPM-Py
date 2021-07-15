#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Represents a material point

"""

class material_point:
    """
    Represent a material point.

    Attributes
    ----------
    
    mass : float
        particle mass
    
    position  : float
        particle position
    
    material : material type
        material
    
    density : float
        particle density
    
    velocity : float
        particle velocity
    
    stress : float
        particle stress
    
    dstrain : float
        particle strain increment
    
    momentum : float
        particle momentum (mass*velocity)
    
    pid : int
        particle identification
    
    f_ext : float
        external force in particle
    
    element : element type
        element containing the particle
    
    N1 : float
        value of the interpolation function of node 1
    
    N2 : float
        value of the interpolation function of node 2
    
    dN1 : float
        value of the interpolation function gradient of node 1
    
    dN2 : float
        value of the interpolation function gradient of node 2
    """
    def __init__(self, mass, material,x):
        
        self.mass = mass
        self.position  = x 
        self.material = material 
        self.density = material.density 

        self.velocity  = 0    
        self.stress    = 0    
        self.dstrain   = 0    
        self.momentum  = 0    
        self.pid = 0          
        self.f_ext = 0        
        self.element = 0      
        self.N1 = 0           
        self.N2 = 0           
        self.dN1 = 0          
        self.dN1 = 0          