#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module defines a class representing the configuration of the problem

"""

class model_setup:

    """
    Represent a configuration object containing the model options
    
    Attributes
    ----------
    interpolation_type : string
        interpolation function type, can be 'linear' or 'cpGIMP'
    
    integration_scheme : string
        material point method integration scheme, can be 'USL', 'USF' or 'MUSL'
    
    time : float
        simulation time

    dt : float
        time step

    solution_particle : integer
        index of the particle to get the solution

    solution_field : string
        the solution field, can be "velocity" or "position"

    solution_array : array
        array to store the solution in terms of time and field

    damping_local_alpha : float
        local damping factor proportional to the total nodal force
        
    """
    def __init__(self):
        
        self.interpolation_type="linear"
        self.integration_scheme="MUSL"
        self.time=0
        self.dt=0
        self.solution_particle=0
        self.solution_field="position"
        self.solution_array=[[],[]]
        self.damping_local_alpha=0