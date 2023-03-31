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
import numpy as np

# local modules
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import setup # for setup the problem
from modules import solver # for solving the problem in time
from analitical_solutions import analitical_solution_wave_in_pile as wip


# density values
young_serie = np.linspace(100e6,200e6,5)

# get color palete for plot
color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

for i in range(len(young_serie)):
    
    # pile length
    L=15

    # number of elements
    nelements=150

    # create an 1D mesh
    msh = mesh.mesh_1D(L=L,nelem=nelements)

    # define a linear material 
    elastic = material.linear_elastic(E=young_serie[i],density=2500)
    
    # put particles in mesh element and set the material
    msh.put_particles_in_all_mesh_elements(ppelem=2,material=elastic)
    
    # setup the model
    msetup = setup.model_setup()
    msetup.interpolation_type="linear"
    msetup.integration_scheme="USF"
    msetup.time=0.14
    msetup.dt=0.01
    msetup.solution_particle=0
    msetup.solution_field='position'
    
    # verify time step
    dt_critical=msh.elements[0].L/(young_serie[i]/elastic.density)**0.5
    msetup.dt = msetup.dt if msetup.dt < dt_critical else dt_critical
    
    # external force
    po =-10e3
    
    # impose intial condition in particle
    msh.particles[-1].f_ext=po
    
    # initial particle position to calculate analytical solution
    pos_initial=msh.particles[0].position
    
    # solve the problem in time
    solver.explicit_solution(msh,msetup)
    
    # subset data for plot
    n_values = 100
    indices = np.linspace(0, len(msetup.solution_array[0])-1, n_values, dtype=int)
    
    y_subset = []
    x_subset = []
    
    for i_index in range(len(indices)): 
        x_subset.append(msetup.solution_array[0][indices[i_index]])
        y_subset.append(msetup.solution_array[1][indices[i_index]])
        
    # plot mpm solution
    plt.plot(x_subset,y_subset,linestyle='solid',linewidth=1,color=color_list[i],marker='o',markersize=3,markerfacecolor='none',label='Young='+'{:.1f}e6-MPM'.format(young_serie[i]/1e6))
    
    # plot the analytical solution
    [anal_xt,anal_vt, anal_t] = wip.wave_in_pile_fixed_and_loaded(L=L,E=young_serie[i],rho=elastic.density,time=msetup.time,dt=msetup.dt/2,po=po,x=pos_initial)
    plt.plot(anal_t,anal_xt,color=color_list[i],linewidth=1,label='Young='+'{:.1f}e6-Analytical'.format(young_serie[i]/1e6))

# configure axis, legends and show plot
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('Position (m)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()