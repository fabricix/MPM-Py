#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:24:37 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)

Purpose
-------
This file defines classes for material representation

"""

class linear_elastic:
    """ 
    Represents a linear elastic material.

    Arguments
    ---------
    E : float
    	Young's modulus
    density : float
    	density
    """
    def __init__(self,E,density):
        
        self.E=E # Young's modulus
        self.density=density # # density