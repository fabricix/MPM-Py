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

# local modules
from modules import mesh # for mesh generation
from modules import material # for material definition

# domain
L = 4

# elements
nelem = 3

# particles per element
p_per_elem = 2

# create an 1D mesh
msh = mesh.mesh_1D(L,nelem)

# define a linear material 
elastic = material.linear_elastic(E=50,density=1)
 
# put particles in elements
msh.put_particles_in_mesh(ppelem=p_per_elem,material=elastic)

#show mesh
msh.print_mesh()