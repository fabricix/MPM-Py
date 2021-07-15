#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This example approximates the 1D single mass bar vibration problem using MPM.

Data
----
Created on Mon Mar 15 13:53:24 2021

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
from modules import solver # for solving the problem in time

# bar length
L=1

# number of elements
nelements=1

# create an 1D mesh
msh = mesh.mesh_1D(L,nelements)

# define a linear material 
elastic = material.linear_elastic(E=50,density=1)

# put particles in mesh element and set the material
msh.put_particles_in_mesh(ppelem=1,material=elastic)

# simulation time 
time = 10 # total time
dt = 0.001 # time step
it = 0 # initial time

# verify time step
dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
dt = dt if dt < dt_critical else dt_critical

# impose initial condition in particle
vo = 0.1
msh.particles[-1].velocity=vo

# variables for plot
x_plot=[]
y_plot=[]

# MPM scheme integration
mpm_scheme='MUSL' # USL or USF or MUSL

# solve the problem in time
solver.explicit_solution(it,dt,time,msh,mpm_scheme,x_plot,y_plot,particle_plot=-1,field_plot='position')

# plot mpm solution
plt.plot(x_plot,y_plot,'ob',markersize=2,label='mpm')

# plot the analytical solution
from analitical_solutions import analitical_solution_single_mass_vibration as smpv
[anal_xt, anal_t] = smpv.single_mass_point_vibration_solution(L,elastic.E,elastic.density,time,dt,L/2,vo)
plt.plot(anal_t,anal_xt,'r',linewidth=2,label='analytical')

# configure axis, legends and show plot
plt.xlabel('time (s)')
plt.ylabel('displacement (m)')
plt.legend()
plt.show()