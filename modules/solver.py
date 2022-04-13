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

def explicit_solution(it,dt,time,msh,mpm_scheme,x_plot,y_plot,particle_plot,field_plot):
	"""
    Calculate the explicit solution of the motion equation using the MPM
    
    Arguments
    ---------
    it: float
        Initial time

    dt: float
        Time step

    time: float
        total simulation time

    msh: mesh
        a mesh object

    mpm_scheme: string
    	Update stress scheme ("USL", "MUSL" or "USF")

    x_plot: list
    	List to add the x variable of a result plot

    y_plot: list
    	List to add the y variable of a result plot

    particle_plot: int
    	Index of the particle to be plot the results

    field_plot: string
    	Field to be plotted ("velocity" or "position")
    """  
    
    # loop couter
	loop_counter = 1
	
	# main simulation loop
	while it<=time:
	    
	    # update interpolation functions values
	    update.interpolation_functions_values(msh)
	    
	    # particle mass to grid nodal mass
	    interpola.mass_to_nodes(msh)

	    # particle momentum to grid nodal momentum
	    interpola.momentum_to_nodes(msh)
	     
	    # impose essential boundary conditions (in fixed nodes set mv=0)
	    msh.elements[0].n1.momentum=0  
	    
	    # Update Stress First Scheme
	    if mpm_scheme=='USF':

	        # calculate the grid nodal velocity
	        update.nodal_velocity(msh)
	    
	        # calculate particle strain increment
	        update.particle_strain_increment(msh,dt)
	        
	        # update particle density
	        update.particle_density(msh,dt)
	    
	        # update particle stress
	        update.particle_stress(msh,dt)
	        
	    # particle internal force to nodes
	    interpola.internal_force_to_nodes(msh)
	    
	    # particle external forces to nodes
	    interpola.external_force_to_nodes(msh)

	    # calculate total force in node
	    integra.total_force_in_nodes(msh)    
	    
	    # impose essential boundary conditions (in fixed nodes set f=m*a=0)
	    msh.elements[0].n1.f_tot=0

	    # integrate the grid nodal momentum equation
	    integra.momentum_in_nodes(msh, dt/2.0 if loop_counter==1 else dt)
	 
	    # update particle velocity
	    update.particle_velocity(msh,dt/2.0 if loop_counter==1 else dt)
	    
	    # update particle position
	    update.particle_position(msh,dt)

	    # Modified Update Stress Last Scheme
	    if(mpm_scheme=='MUSL'):
	        
	        # recalculate the grid nodal momentum
	        update.nodal_momentum(msh)
	        
	        # impose essential boundary conditions (in fixed nodes v=0)
	        msh.elements[0].n1.velocity=0
	        msh.elements[0].n1.momentum=0
	    
	    # Modified Update Stress Last or Update Stress Last Scheme
	    if(mpm_scheme=='MUSL' or mpm_scheme=='USL'):
	        
	        # calculate the grid nodal velocity
	        update.nodal_velocity(msh)
	    
	        # calculate particle strain increment
	        update.particle_strain_increment(msh,dt)

	        # update particle density
	        update.particle_density(msh,dt)
	    
	        # update particle stress
	        update.particle_stress(msh,dt)
	    
	    # reset all nodal values
	    update.reset_nodal_vaues(msh)

	    # store data for plot
	    x_plot.append(it)
	    
	    if field_plot=='velocity':
	    	y_plot.append(msh.particles[particle_plot].velocity)
	    
	    elif field_plot=='position':
	    	y_plot.append(msh.particles[particle_plot].position)
	    
	    # update loop counter
	    loop_counter+=1

	    # advance in time
	    it+=dt
