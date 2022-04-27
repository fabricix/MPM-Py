#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Defines nodal integration functions. 
This functions in general have the objective to advance in time, or adding quantities at the nodes.

"""

def total_force_in_nodes(msh, msetup):
    """
    Calculate total forces in nodes
    
    Arguments
    ---------
    msh: mesh
        a mesh object
    """

    # add damping force if needed
    if msetup.damping_local_alpha>0:
        
        # add damping force in nodes
        for node in msh.nodes:
            
            # damping factor
            alpha = msetup.damping_local_alpha

            # unbalanced nodal force magnitude
            unbalanced_force_mag = abs(node.f_int + node.f_ext)

            # nodal velocity
            nodal_vel = node.momentum/node.mass

            if abs(nodal_vel)!=0:

                # velocity direction
                vel_direction = nodal_vel/abs(nodal_vel)
                
                # damping force proportional to unbalanced forces and opposite to the nodal velocity
                node.f_damp = - alpha * unbalanced_force_mag * vel_direction

    # total nodal force
    for node in msh.nodes:
        node.f_tot = node.f_int + node.f_ext + node.f_damp
                  
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