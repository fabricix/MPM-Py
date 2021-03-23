#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This file defines functions for updating tasks

Data
----
Created on Tue Mar 16 16:24:45 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)
"""
from modules import interpolation as interp

def particle_velocity(msh,dt):
    """
    update particle velocity
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
    update particle position
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
    calculate nodal velocity
    """
    for inode in msh.nodes:
        inode.velocity=inode.momentum/inode.mass
            
def nodal_momentum(msh):
    """
    calculate nodal momentum
    """
    for inode in msh.nodes:
        inode.momentum=0
    
    for ie in msh.elements:
        for ip in ie.particles:

            ie.n1.momentum+=ip.mass*ip.velocity*ip.N1
            ie.n2.momentum+=ip.mass*ip.velocity*ip.N2
              
def particle_strain_increment(msh,dt):
    """
    calculate particle strain increment
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
    update particle density
    """
    for ip in msh.particles:
   
        ip.density = ip.density/(1+ip.dstrain)
        
def particle_stress(msh,dt):
    """
    update particle stress
    """
    for ip in msh.particles:

        ip.stress += ip.dstrain*ip.material.E
        
def interpolation_functions_values(msh):    
    """
    update the values of the nodal interpolation functions and its gradients
    """
    for ip in msh.particles:
        
        # current element
        ie=ip.element
        
        # interpolation functions
        ip.N1=interp.Ni(ip.position,ie.n1.x,ie.L)
        ip.N2=interp.Ni(ip.position,ie.n2.x,ie.L)
        
        # interpolation functions gradients
        ip.dN1=interp.dNi(ip.position,ie.n1.x,ie.L)
        ip.dN2=interp.dNi(ip.position,ie.n2.x,ie.L)
        
def  reset_nodal_vaues(msh):
    """
    reset all nodal values for the next step calculation
    """
    for inode in msh.nodes:
        inode.velocity = 0
        inode.mass     = 0
        inode.momentum = 0
        inode.f_int = 0
        inode.f_ext = 0
        inode.f_tot = 0