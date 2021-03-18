#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:53:24 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)

"""

"""
This example approximates the 1D axial bar vibration problem using MPM.

"""

# external libs
import matplotlib.pyplot as plt # for plot

# internal libs
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import interpolation as interpola # for interpolation tasks
from modules import integration as integra # for integration tasks
from modules import update # for updating tasks

# create an 1D mesh
msh = mesh.mesh_1D(L=1,nelem=1)

# define a linear material 
elastic = material.linear_elastic(E=50,density=1)

# put particles in mesh element and set the material
msh.put_particles_in_mesh(ppelem=1,material=elastic)

# simulation time 
time = 3 # total time
dt = 0.005 # time step
it = 0 # initial time

# verify time step
dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
dt = dt if dt < dt_critical else dt_critical

# impose initial condition in particle
msh.particles[-1].velocity=0.1

# MPM scheme integration
mpm_scheme='MUSL' # USL or USF or MUSL
    
# main simulation loop
while it<=time:
    
    # update interpolation functions values
    update.interpolation_functions_values(msh)
    
    # particle mass to grid nodal mass
    interpola.mass_to_nodes(msh)

    # particle momentum to grid nodal momentum
    interpola.momentum_to_nodes(msh)
     
    # impose essential boundary conditions (in fixed nodes set mv=0)
    msh.elements[0].n1.momentum=0  
    
    # Update Stress First Scheme
    if mpm_scheme=='USF':

        # calculate the grid nodal velocity
        update.nodal_velocity(msh)
    
        # calculate particle strain increment
        update.particle_strain_increment(msh,dt)
        
        # update particle density
        update.particle_density(msh,dt)
    
        # update particle stress
        update.particle_stress(msh,dt)
        
    # particle internal force to nodes
    interpola.internal_force_to_nodes(msh)
    
    # particle external forces to nodes
    interpola.external_force_to_nodes(msh)

    # calculate total force in node
    integra.total_force_in_nodes(msh)    
    
    # impose essential boundary conditions (in fixed nodes set f=m*a=0)
    msh.elements[0].n1.f_tot=0

    # integrate the grid nodal momentum equation
    integra.momentum_in_nodes(msh,dt)
 
    # update particle velocity
    update.particle_velocity(msh,dt)
    
    # update particle position
    update.particle_position(msh,dt)

    # Modified Update Stress Last Scheme
    if(mpm_scheme=='MUSL'):
        
        # recalculate the grid nodal momentum
        update.nodal_momentum(msh)
        
        # impose essential boundary conditions (in fixed nodes v=0)
        msh.elements[0].n1.velocity=0
        msh.elements[0].n1.momentum=0
    
    # Modified Update Stress Last or Update Stress Last Scheme
    if(mpm_scheme=='MUSL' or mpm_scheme=='USL'):
        
        # calculate the grid nodal velocity
        update.nodal_velocity(msh)
    
        # calculate particle strain increment
        update.particle_strain_increment(msh,dt)

        # update particle density
        update.particle_density(msh,dt)
    
        # update particle stress
        update.particle_stress(msh,dt)
    
    # reset all nodal values
    update.reset_nodal_vaues(msh)

    # plot position of the last particle
    plt.plot(it,msh.particles[-1].position,'ob',markersize=3)
    
    # advance in time
    it+=dt