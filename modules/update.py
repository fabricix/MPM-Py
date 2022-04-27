#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This file defines functions for updating tasks

"""
from modules import interpolation as interp
from modules import shape as shape

def particle_velocity(msh,dt):
    """
    Update particle velocity

    Arguments
    ---------
    msh: mesh
        a mesh object
    dt: float
        time step
    """
    for ip in msh.particles:
   
        # current element
        ie=ip.element    
        
        f1=ie.n1.f_tot # total force node 1
        m1=ie.n1.mass  # mass node 1
        
        f2=ie.n2.f_tot # total force node 2
        m2=ie.n2.mass  # mass node 2
        
        ip.velocity+=(f1/m1*ip.N1+f2/m2*ip.N2)*dt
        
def particle_position(msh,dt):
    """
    Update particle position

    Arguments
    ---------
    msh: mesh
        a mesh object
    dt: float
        time step
    """
    for ip in msh.particles:
   
        # current element
        ie=ip.element    
         
        p1=ie.n1.momentum # momentum node 1
        m1=ie.n1.mass     # mass node 1
        
        p2=ie.n2.momentum # momentum node 2
        m2=ie.n2.mass     # mass node 2
        
        ip.position+=(p1/m1*ip.N1+p2/m2*ip.N2)*dt
        
def nodal_velocity(msh):
    """
    Calculate nodal velocity

    Arguments
    ---------
    msh: mesh
        a mesh object
    """
    for inode in msh.nodes:
        if(inode.mass!=0):
            inode.velocity=inode.momentum/inode.mass
            
def nodal_momentum(msh):
    """
    Calculate nodal momentum
    
    Arguments
    ---------
    msh: mesh
        a mesh object
    """
    for inode in msh.nodes:
        inode.momentum=0
    
    for ie in msh.elements:
        for ip in ie.particles:

            ie.n1.momentum+=ip.mass*ip.velocity*ip.N1
            ie.n2.momentum+=ip.mass*ip.velocity*ip.N2
              
def particle_strain_increment(msh,dt):
    """
    Calculate particle strain increment

    Arguments
    ---------
    msh: mesh
        a mesh object
    dt: float
        time step
    """
    for ip in msh.particles:
   
        # current element
        ie=ip.element    
        
        # nodal velocities
        v1=ie.n1.velocity # velocity node 1
        v2=ie.n2.velocity # velocity node 2
        
        # particle strain increment
        ip.dstrain=(ip.dN1*v1+ip.dN2*v2)*dt
        
def particle_density(msh,dt):
    """
    Update particle density

    Arguments
    ---------
    msh: mesh
        a mesh object
    dt: float
        time step

    """
    for ip in msh.particles:
   
        ip.density = ip.density/(1+ip.dstrain)
        
def particle_stress(msh,dt):
    """
    Update particle stress

    Arguments
    ---------
    msh: mesh
        a mesh object
    dt: float
        time step
    """
    for ip in msh.particles:

        ip.material.update_stress(ip,dt)
        
def interpolation_functions_values(msh):    
    """
    Update the values of the nodal interpolation functions and its gradients

    Arguments
    ---------
    msh: mesh
        a mesh object
    """
    for ip in msh.particles:
        
        # current element
        ie=ip.element
        
        # interpolation functions
        ip.N1=shape.NiLinear(ip.position,ie.n1.x,ie.L)
        ip.N2=shape.NiLinear(ip.position,ie.n2.x,ie.L)
        
        # interpolation functions gradients
        ip.dN1=shape.dNiLinear(ip.position,ie.n1.x,ie.L)
        ip.dN2=shape.dNiLinear(ip.position,ie.n2.x,ie.L)
        
def  reset_nodal_vaues(msh):
    """
    Reset all nodal values for the next step calculation

    Arguments
    ---------
    msh: mesh
        a mesh object
    """
    for inode in msh.nodes:
        inode.velocity = 0
        inode.mass     = 0
        inode.momentum = 0
        inode.f_int = 0
        inode.f_ext = 0
        inode.f_tot = 0

def particle_list(msh):
    """
    Update particle list in each mesh element.

    Arguments
    ---------
    msh: mesh
        a mesh object
    """

    # clear particle list in elements
    for ie in msh.elements:
        ie.particles = []

    # for each particle in model
    for ip in msh.particles:

        # get particle position
        xp = ip.position

        # for each element in mesh
        for ie in msh.elements:

            # get the nodal position
            xn1 = ie.n1.x
            xn2 = ie.n2.x

            # verify the particle is inside the element
            if xp>=xn1 and xp<xn2:

                # update element in particle
                ip.element = ie

                # add the particle to the element list
                ie.particles.append(ip)

                # break element loop for testing other particle
                break