#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This example approximates the continuum 1D damped bar vibration problem using MPM.

Data
----
Created on Sat Mar 30 14:45:07 2023

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
from modules import setup # for setup the problem
from modules import solver # for solving the problem in time

damping_serie = np.linspace(0, 0.2, 10)

for i in range(len(damping_serie)):

  # bar length
  L=25

  # number of elements
  nelements=15

  # create an 1D mesh
  msh = mesh.mesh_1D(L=L,nelem=nelements)

  # define a linear material 
  elastic = material.linear_elastic(E=100,density=1)

  # put particles in mesh element and set the material
  msh.put_particles_in_all_mesh_elements(ppelem=2,material=elastic)

  # setup the model
  msetup = setup.model_setup()
  msetup.interpolation_type="linear"
  msetup.integration_scheme="MUSL"
  msetup.time=120
  msetup.dt=0.35
  msetup.solution_particle=-1
  msetup.solution_field='velocity'
  msetup.damping_local_alpha=msetup.damping_local_alpha=damping_serie[i]

  # verify time step
  dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
  msetup.dt = msetup.dt if msetup.dt < dt_critical else dt_critical

  # impose initial condition in particles
  vo=0.1
  b1=np.pi/2.0/L
  for ip in msh.particles:
    ip.velocity=vo*np.sin(b1*ip.position)

  # solve the problem in time
  solver.explicit_solution(msh,msetup)
      
  # plot mpm solution
  plt.plot(msetup.solution_array[0],msetup.solution_array[1],label=str('Damping={:.2f}-MPM'.format(damping_serie[i])))

# plot the analytical solution
from analitical_solutions import analitical_solution_continuum_bar_vibration as cbv
[anal_xt,anal_vt, anal_t] = cbv.continuum_bar_vibration_solution(L,elastic.E,elastic.density,msetup.time,msetup.dt,vo,msh.particles[msetup.solution_particle].position)
plt.plot(anal_t,anal_vt,'k',linewidth=1.5,label='Damping={:.2f}-Analytical'.format(0))

# configure axis, legends and show plot
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()