#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 08:52:30 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)

Purpose
-------

This examples tests the linear interpolation functions and its derivative.

"""

# local modules
from modules import mesh # for mesh generation
from modules import interpolation # for interpolation

# domain
L = 2

# elements
nelem = 2

# create an 1D mesh
msh=mesh.mesh_1D(L,nelem)

#show mesh
msh.print_mesh()

# print the interpolation functions and its derivative
interpolation.test(x1=0,x2=L,xI=L/2,L=L/nelem)