#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Defines nodal integration functions. 
This functions in general have the objective to advance in time, or adding quantities at the nodes.

"""

def total_force_in_nodes(msh):
    """
    Calculate total forces in nodes
    
    Arguments
    ---------
    msh: mesh
        a mesh object
    """
    for node in msh.nodes:
            node.f_tot = node.f_int + node.f_ext
                  
def momentum_in_nodes(msh,dt):
    """
    Calculate momentum in nodes

    Arguments
    ---------
    msh: mesh
        a mesh object

    dt: float
        time step
    """
    for inode in msh.nodes:
        inode.momentum += inode.f_tot*dt