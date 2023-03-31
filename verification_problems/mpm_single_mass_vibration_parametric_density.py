#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This example approximates the 1D single mass bar vibration problem using MPM.
In this example, a parametric study over the density of the mass is performed 

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
import matplotlib.colors as mcolors # for colors
import numpy as np # numpy

# local modules
from modules import mesh # for mesh definition
from modules import material # for material definition
from modules import setup # for setup the problem
from modules import solver # for solving the problem in time

# density values
density_serie = np.linspace(1,15,6)


# get color palete for plot
tableau_colors = mcolors.TABLEAU_COLORS
color_list = list(tableau_colors.values())[:len(density_serie)]

# main loop
for i in range(len(density_serie)):

    # bar length
    L=1
    
    # number of elements
    nelements=1
    
    # create an 1D mesh
    msh = mesh.mesh_1D(L,nelements)
    
    # define a linear material 
    elastic = material.linear_elastic(E=50,density=density_serie[i])
    
    # put particles in mesh element and set the material
    msh.put_particles_in_all_mesh_elements(ppelem=1,material=elastic)
    
    # setup the model
    msetup = setup.model_setup()
    msetup.interpolation_type="linear"
    msetup.integration_scheme="MUSL"
    msetup.time=10
    msetup.dt=0.001
    msetup.solution_particle=-1
    msetup.solution_field="position"
    msetup.damping_local_alpha=0.0
    
    # verify time step
    dt_critical=msh.elements[0].L/(elastic.E/elastic.density)**0.5
    msetup.dt = msetup.dt if msetup.dt < dt_critical else dt_critical
    
    # impose initial condition in particle
    vo = 0.1
    msh.particles[-1].velocity=vo
    
    # solve the problem in time
    solver.explicit_solution(msh,msetup)
    
    n_values = 100
    indices = np.linspace(0, len(msetup.solution_array[0])-1, n_values, dtype=int)
    
    y_subset = []
    x_subset = []
    
    for i_index in range(len(indices)): 
        x_subset.append(msetup.solution_array[0][indices[i_index]])
        y_subset.append(msetup.solution_array[1][indices[i_index]])
        
    # plot mpm solution
    plt.plot(x_subset,y_subset,' ',color=color_list[i],marker='s',markerfacecolor='none',label='mpm, density='+'{:.2f}'.format(density_serie[i]))
    
    # plot the analytical solution
    from analitical_solutions import analitical_solution_single_mass_vibration as smpv
    [anal_xt, anal_t] = smpv.single_mass_point_vibration_solution(L,elastic.E,elastic.density,msetup.time,msetup.dt,L/2,vo)
    
    plt.plot(anal_t,anal_xt,'-',color=color_list[i],label='analytical')

# configure axis, legends and show plot
plt.xlabel('time (s)')
plt.ylabel('displacement (m)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()