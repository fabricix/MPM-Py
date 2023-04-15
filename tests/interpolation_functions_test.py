#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 08:52:30 2021

Author
------
Fabricio Fernandez (<fabricio.hmf@gmail.com>)

Purpose
-------

This examples tests the interpolation functions and its derivative.

"""

import matplotlib.pyplot as plt

# include the modules' path to the current path
import sys
sys.path.append("..") 

# local modules
from modules import shape as shape# for interpolation

# domain
L = 2

# elements
nelem = 2

# cell dimension
le = L/nelem 

# get linear interpolation functions values in nodes
[x1,n1_linear,dn1_linear] = shape.get_interpolation_functions(x1=0,x2=L,xI=0,L=L/nelem,shape_type="linear")
[x2,n2_linear,dn2_linear] = shape.get_interpolation_functions(x1=0,x2=L,xI=L/2,L=L/nelem,shape_type="linear")
[x3,n3_linear,dn3_linear] = shape.get_interpolation_functions(x1=0,x2=L,xI=L,L=L/nelem,shape_type="linear")

plt.plot(x1,n1_linear,"--",label="n1-linear")
plt.plot(x2,n2_linear,"--",label="n2-linear")
plt.plot(x3,n3_linear,"--",label="n3-linear")
plt.plot(x1,n1_linear+n2_linear+n3_linear,"--",label="n1+n2+n3-linear")
plt.legend()

# get cpgimp interpolation functions values
[x1,n1_cpgimp,dn1_cpgimp] = shape.get_interpolation_functions(x1=0,x2=L,xI=0,L=L/nelem,shape_type="cpGIMP")
[x2,n2_cpgimp,dn2_cpgimp] = shape.get_interpolation_functions(x1=0,x2=L,xI=L/2,L=L/nelem,shape_type="cpGIMP")
[x3,n3_cpgimp,dn3_cpgimp] = shape.get_interpolation_functions(x1=0,x2=L,xI=L,L=L/nelem,shape_type="cpGIMP")

plt.plot(x1,n1_cpgimp, label="n1-cpGIMP")
plt.plot(x2,n2_cpgimp, label="n2-cpGIMP")
plt.plot(x3,n3_cpgimp, label="n3-cpGIMP")
plt.plot(x1,n1_cpgimp+n2_cpgimp+n3_cpgimp, label="n1+n2+n3-cpGIMP")
plt.legend()