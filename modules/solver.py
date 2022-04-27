#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""

Perform the explicit solution in time of the motion equation:

.. math::
	\frac{\partial \sigma_{ij}}{\partial x_j} + \rho b_i = \rho \ddot{u}_i

where,
$$\sigma_{ij}$$: is the Cauchy stress tensor,
$$\rho$$: is the material density, and
$$b_i$$: is the body force per unit mass acting on the continuum, and
$$\ddot{u}_i$$: is the acceleration

"""

# local modules
from modules import interpolation as interpola # for interpolation tasks
from modules import integration as integra # for integration tasks
from modules import update # for updating tasks

def explicit_solution(msh,msetup):
	"""
    Calculate the explicit solution of the motion equation using the MPM
    
    Arguments
    ---------

    msh: mesh
        a mesh object

    msetup : model_setup
    	a model_setup object containing the model options

    """  
    
    # loop couter
	loop_counter = 1
	
	# current loop time
	it = 0

	# main simulation loop
	while it<=msetup.time:
	    
	    # update particles list in each element
	    update.particle_list(msh)

	    # update interpolation functions values
	    update.interpolation_functions_values(msh)
	    
	    # particle mass to grid nodal mass
	    interpola.mass_to_nodes(msh)

	    # particle momentum to grid nodal momentum
	    interpola.momentum_to_nodes(msh)
	     
	    # impose essential boundary conditions (in fixed nodes set mv=0)
	    msh.elements[0].n1.momentum=0  
	    
	    # Update Stress First Scheme
	    if msetup.integration_scheme=='USF':

	        # calculate the grid nodal velocity
	        update.nodal_velocity(msh)
	    
	        # calculate particle strain increment
	        update.particle_strain_increment(msh,msetup.dt)
	        
	        # update particle density
	        update.particle_density(msh,msetup.dt)
	    
	        # update particle stress
	        update.particle_stress(msh,msetup.dt)
	        
	    # particle internal force to nodes
	    interpola.internal_force_to_nodes(msh)
	    
	    # particle external forces to nodes
	    interpola.external_force_to_nodes(msh)

	    # calculate total force in node
	    integra.total_force_in_nodes(msh)    
	    
	    # impose essential boundary conditions (in fixed nodes set f=m*a=0)
	    msh.elements[0].n1.f_tot=0

	    # integrate the grid nodal momentum equation
	    integra.momentum_in_nodes(msh, msetup.dt/2.0 if loop_counter==1 else msetup.dt)
	 
	    # update particle velocity
	    update.particle_velocity(msh,msetup.dt/2.0 if loop_counter==1 else msetup.dt)
	    
	    # update particle position
	    update.particle_position(msh,msetup.dt)

	    # Modified Update Stress Last Scheme
	    if(msetup.integration_scheme=='MUSL'):
	        
	        # recalculate the grid nodal momentum
	        update.nodal_momentum(msh)
	        
	        # impose essential boundary conditions (in fixed nodes v=0)
	        msh.elements[0].n1.velocity=0
	        msh.elements[0].n1.momentum=0
	    
	    # Modified Update Stress Last or Update Stress Last Scheme
	    if(msetup.integration_scheme=='MUSL' or msetup.integration_scheme=='USL'):
	        
	        # calculate the grid nodal velocity
	        update.nodal_velocity(msh)
	    
	        # calculate particle strain increment
	        update.particle_strain_increment(msh,msetup.dt)

	        # update particle density
	        update.particle_density(msh,msetup.dt)
	    
	        # update particle stress
	        update.particle_stress(msh,msetup.dt)
	    
	    # reset all nodal values
	    update.reset_nodal_vaues(msh)

	    # store data for plot
	    msetup.solution_array[0].append(it)
	    
	    if msetup.solution_field=='velocity':
	    	msetup.solution_array[1].append(msh.particles[msetup.solution_particle].velocity)
	    
	    elif msetup.solution_field=='position':
	    	msetup.solution_array[1].append(msh.particles[msetup.solution_particle].position)
	    
	    # update loop counter
	    loop_counter+=1

	    # advance in time
	    it+=msetup.dt