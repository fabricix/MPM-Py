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
L = 5

# elements
nelem = 10

# particles per element
p_per_elem = 2

# create an 1D mesh
msh = mesh.mesh_1D(L,nelem)

# define a linear material 
elastic = material.linear_elastic(E=50,density=1)
 
# put particles in some elements, from elem_i to elem_f
msh.put_particles_in_mesh_by_elements_id(ppelem=p_per_elem,material=elastic, elem_i=0,elem_f=3)

#show mesh
msh.print_mesh()