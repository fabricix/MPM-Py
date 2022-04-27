#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
This example demostrate the use of the viscous constitutive model.

Data
----
Created on Wed Apr 27 14:05:43 2022

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

# mesh definition
L=10

# number of elements
nelements=20

# particles per element
p_per_elem = 4

# create an 1D mesh
msh = mesh.mesh_1D(L,nelements)

# define a viscous material
material = material.newtonian_fluid(mu=100000,density=2000)

# put particles in some elements, from elem_i to elem_f
msh.put_particles_in_mesh_by_elements_id(ppelem=p_per_elem,material=material, elem_i=0,elem_f=5)

#show mesh
#msh.print_mesh()

# setup the model
msetup = setup.model_setup()
msetup.interpolation_type="linear"
msetup.integration_scheme="MUSL"
msetup.time=1
msetup.dt=0.001
msetup.solution_particle=-1
msetup.solution_field="position"
msetup.damping_local_alpha=0.0

# set gravity load in particles
for ip in msh.particles:
    ip.f_ext += ip.mass*9.81

# solve the problem in time
solver.explicit_solution(msh,msetup)

# plot mpm solution
plt.plot(msetup.solution_array[0],msetup.solution_array[1],'-',markersize=2,label=r'mpm, $\mu$='+str(material.mu))

# configure axis, legends and show plot
plt.xlabel('time (s)')
plt.ylabel('displacement (m)')
plt.legend()
plt.show()

#msh.print_mesh()