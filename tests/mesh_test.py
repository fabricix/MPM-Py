#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:39:50 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)

Purpose
-------

This examples tests the mesh creation function.

"""

# include the modules' path to the current path
import sys
sys.path.append("..") 

# local modules
from modules import mesh # for mesh generation
from modules import material # for material definition

# domain
L = 4

# elements
nelem = 2

# particles per element
p_per_elem = 2

# create an 1D mesh
msh = mesh.mesh_1D(L,nelem)

# define a linear material 
elastic = material.linear_elastic(E=50,density=1)
 
# put particles in all elements
msh.put_particles_in_all_mesh_elements(ppelem=p_per_elem,material=elastic)

#show mesh
msh.print_mesh()