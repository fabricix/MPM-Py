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

# include the modules' path to the current path
import sys
sys.path.append("..")

# external modules
import matplotlib.pyplot as plt # for plot

# local modules
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import setup # for setup the problem
from modules import solver # for solving the problem in time
from analitical_solutions import analitical_solution_wave_in_pile as wip

# pile length
L=15

# number of elements
nelements=150

# create an 1D mesh
msh = mesh.mesh_1D(L=L,nelem=nelements)

# define a linear material 
elastic = material.linear_elastic(E=100e6,density=2500)

# put particles in mesh element and set the material
msh.put_particles_in_all_mesh_elements(ppelem=2,material=elastic)

# setup the model
msetup = setup.model_setup()
msetup.interpolation_type="linear"
msetup.integration_scheme="USF"
msetup.time=0.2
msetup.dt=0.01
msetup.solution_particle=0
msetup.solution_field='position'
msetup.damping_local_alpha=0.0
  
# verify time step
dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
msetup.dt = msetup.dt if msetup.dt < dt_critical else dt_critical

# external force
po =-10e3

# impose intial condition in particle
msh.particles[-1].f_ext=po

# initial particle position to calculate analytical solution
pos_initial=msh.particles[0].position

# solve the problem in time
solver.explicit_solution(msh,msetup)

# figure to plot
fig,ax = plt.subplots()

# plot mpm solution
ax.plot(msetup.solution_array[0],msetup.solution_array[1],linestyle='solid',linewidth=1.5,color="blue",marker='o',markersize=0,markerfacecolor='none',label='MPM')

# plot the analytical solution
[anal_xt,anal_vt, anal_t] = wip.wave_in_pile_fixed_and_loaded(L=L,E=elastic.E,rho=elastic.density,time=msetup.time,dt=msetup.dt/2,po=po,x=pos_initial,n_sum=1000)
ax.plot(anal_t,anal_xt,'r',linewidth=1.5,label='Analytical solution')

# vertical line for the theorical arrival time
plt.axvline(x = (L-pos_initial)/(elastic.E/elastic.density)**0.5,linestyle="dashed",color='k',label='Analitical arrival time')

# configure axis, legends and show plot
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
ax.legend()
plt.show()