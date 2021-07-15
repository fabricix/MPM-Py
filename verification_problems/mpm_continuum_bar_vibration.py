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
import numpy as np # for sin

# local modules
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import solver # for solving the problem in time

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

# solve the problem in time
solver.explicit_solution(it,dt,time,msh,mpm_scheme,x_plot,y_plot,particle_plot=-1,field_plot='velocity')
    
# plot mpm solution
plt.plot(x_plot,y_plot,'ob',markersize=2,label='mpm')

# plot the analytical solution
from analitical_solutions import analitical_solution_continuum_bar_vibration as cbv
[anal_xt,anal_vt, anal_t] = cbv.continuum_bar_vibration_solution(L,elastic.E,elastic.density,time,dt,vo,msh.particles[-1].position)
plt.plot(anal_t,anal_vt,'r',linewidth=2,label='analytical')

# configure axis, legends and show plot
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.legend()
plt.show()