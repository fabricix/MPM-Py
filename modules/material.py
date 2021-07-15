#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Represents a linear elastic material

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