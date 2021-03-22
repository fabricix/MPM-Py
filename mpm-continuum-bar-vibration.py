#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This example approximates the continuum 1D bar vibration problem using MPM.

Data
----
Created on Sat Mar 20 20:25:53 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)
"""

# external modules
import matplotlib.pyplot as plt # for plot
import numpy as np # for sin

# local modules
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import interpolation as interpola # for interpolation tasks
from modules import integration as integra # for integration tasks
from modules import update # for updating tasks

# bar length
L=25

# number of elements
nelements=15

# create an 1D mesh
msh = mesh.mesh_1D(L=L,nelem=nelements)

# define a linear material 
elastic = material.linear_elastic(E=100,density=1)

# put particles in mesh element and set the material
msh.put_particles_in_mesh(ppelem=2,material=elastic)

# simulation time 
time = 60 # total time
dt = 0.1  # time step
it = 0.0  # initial time

# verify time step
dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
dt = dt if dt < dt_critical else dt_critical

# impose initial condition in particles
vo=0.1
b1=np.pi/2.0/L
for ip in msh.particles:
  ip.velocity=vo*np.sin(b1*ip.position)

# variables for plot
x_plot=[]
y_plot=[]

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

    # store for plot
    x_plot.append(it)
    y_plot.append(msh.particles[-1].velocity)
    
    # advance in time
    it+=dt
    
# plot mpm solution
plt.plot(x_plot,y_plot,'ob',markersize=2,label='mpm')

# plot the analytical solution
from analytical import continuum_bar_vibration as cbv
[anal_xt,anal_vt, anal_t] = cbv.continuum_bar_vibration_solution(L,elastic.E,elastic.density,time,dt,vo,msh.particles[-1].position)
plt.plot(anal_t,anal_vt,'r',linewidth=2,label='analytical')

# configure axis, legends and show plot
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.legend()
plt.show()