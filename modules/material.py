#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This module defines classes representing materials

"""

class linear_elastic:
    """ 
    Represents a linear elastic material

    Arguments
    ---------
    E : float
    	Young's modulus
    density : float
    	density
    """
    def __init__(self,E,density):
        
        self.E=E # Young's modulus
        self.density=density # density

    def update_stress(self,particle,dt):
        
        """
        Update particle stress using linear elastic constitutive model

        Arguments
        ---------
        particle: particle
            a particle object
        """
        
        particle.stress+=particle.dstrain*self.E

class newtonian_fluid:
    """ 
    Represents a Newtonian fluid material

    Arguments
    ---------
    
    mu : float
        Viscosity

    density : float
        density
    
    """

    def __init__(self,mu,density):
        
        self.mu=mu # viscosity
        self.density=density # density

    def update_stress(self,particle,dt):
        
        """
        Update particle stress

        Arguments
        ---------
        particle: particle
            a particle object
        """
        
        particle.stress=self.mu*particle.dstrain/dt
