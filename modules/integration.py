#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------
Defines nodal integration functions

Data
----
Created on Tue Mar 16 16:17:03 2021

Author
------
Fabricio Fernandez, <fabricio.hmf@gmail.com>
"""

def total_force_in_nodes(msh):
    """
    Calculate total forces in nodes
    """
    for node in msh.nodes:
            node.f_tot = node.f_int + node.f_ext
                  
def momentum_in_nodes(msh,dt):
    """
    Calculate momentum in nodes
    """
    for inode in msh.nodes:
        inode.momentum += inode.f_tot*dt