#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This module defines classes representing a finite element mesh

"""

from modules import element
from modules import node
from modules import particle

class mesh_1D: 
    """
    A class to represent a 1D Eulerian mesh containing elements,
    nodes and particles.
    
    Attributes
    ----------
    elements : list
        elements forming the mesh
        
    particles : list
        particles in mesh
        
    nodes : list
        nodes in mesh
        
    nelem : int
        number of elements in mesh
        
    ppelem : int
        particles per element
    """
    
    def __init__(self,L,nelem):
        
        self.elements=[]    # mesh elements
        self.particles=[]   # particles in mesh
        self.nodes=[]       # nodes in mesh
        self.nelem=nelem    # elements in mesh
        self.ppelem=0       # particles per element
        
        for i in range(nelem):
            
            if i==0: 
                
                ielem = element.bar_1D()
                ielem.id=i 
                
                ielem.n1=node.node_1D()
                ielem.n1.id=len(self.nodes)
                self.nodes.append(ielem.n1)
                
                ielem.n2=node.node_1D()
                ielem.n2.id=len(self.nodes)
                self.nodes.append(ielem.n2)
                
            else:
                ielem = element.bar_1D()
                ielem.id=i
                ielem.n1=self.elements[i-1].n2
                
                ielem.n2=node.node_1D()
                ielem.n2.id=len(self.nodes)
                self.nodes.append(ielem.n2)
            
            le = L/nelem
            ielem.L=le
            ielem.n1.x=i*le
            ielem.n2.x=ielem.n1.x+le
            
            self.elements.append(ielem)
            
    def put_particles_in_all_mesh_elements(self,ppelem,material):
        """
        Distributes particles in elements mesh
        
        Arguments
        ---------
        ppelem: int
            number of particles per element

        material: material
            a material object

        """
        self.ppelem=ppelem
            
        for ie in range(self.nelem):
            
            ie = self.elements[ie]
            le = ie.L
         
            for i in range(ppelem):
                
                # particle mass
                pmass = le*material.density/ppelem
                
                # particle position
                if(len(ie.particles)==0):
                    xp=ie.n1.x+le/(2*ppelem)
                    
                elif(len(ie.particles)==(ppelem-1)):
                    xp=ie.n2.x-le/(2*ppelem)   
                
                else:
                    xp=ie.n1.x+le/(2*ppelem)+len(ie.particles)*(le/ppelem)
                    
                # create particle
                ip = particle.material_point(pmass,material,xp)
                ip.id=len(self.particles)
                
                # set the element in the particle
                ip.element=ie

                # append in elements
                ie.particles.append(ip)                
                                
                # append in mesh
                self.particles.append(ip)
        
    def put_particles_in_mesh_by_elements_id(self,ppelem,material,elem_i,elem_f):
        """
        Distributes particles in elements mesh from xi to xf
        
        Arguments
        ---------
        ppelem: int
            number of particles per element

        material: material
            a material object

        elem_i: int
            initial element id to distribute particles

        elem_f: int
            final element id to distribute particles

        """
        self.ppelem=ppelem

        for ie in range(self.nelem):
            
            ie = self.elements[ie]
            le = ie.L
            
            # verify if the element is allow to get particles
            if ie.id<elem_i or ie.id>elem_f:
                continue 

            for i in range(ppelem):
                
                # particle mass
                pmass = le*material.density/ppelem
                
                # particle position
                if(len(ie.particles)==0):
                    xp=ie.n1.x+le/(2*ppelem)
                    
                elif(len(ie.particles)==(ppelem-1)):
                    xp=ie.n2.x-le/(2*ppelem)   
                
                else:
                    xp=ie.n1.x+le/(2*ppelem)+len(ie.particles)*(le/ppelem)
                    
                # create particle
                ip = particle.material_point(pmass,material,xp)
                ip.id=len(self.particles)
                
                # set the element in the particle
                ip.element=ie

                # append in elements
                ie.particles.append(ip)                
                                
                # append in mesh
                self.particles.append(ip)

    def print_mesh(self,print_labels=True):
        """
        Function for print the mesh in a plot

        Arguments
        ---------
        print_labels: bool
            determines if the label of the mesh will be plotted
        """
        import matplotlib.pyplot as plt
        plt.cla()
        
        for ie in self.elements:
            plt.plot([ie.n1.x,ie.n2.x],[0,0],'--sk')
            dy=0.005
            
            if(print_labels):
                x=(ie.n1.x+ie.n2.x)/2
                plt.annotate("e%d"%ie.id, xy=(x,-1.5*dy),fontsize=13)
                plt.annotate("n%d"%ie.n1.id, xy=(ie.n1.x,dy),fontsize=13)
                plt.annotate("n%d"%ie.n2.id, xy=(ie.n2.x,dy),fontsize=13)
            
            for ip in ie.particles:
                plt.plot(ip.position,0,'ob')
                if(print_labels):
                    plt.annotate("p%d"%ip.id, xy=(ip.position,dy),fontsize=13)
                    
        ie = self.elements[0]
        x = ie.n1.x
        y = -0.04
        plt.annotate("n = node\np = material point\ne = element", xy=(x,y),fontsize=13)
        plt.xlabel(r"Node position, $x_I$")
        plt.title("Mesh and Material Points")
        plt.show()
    
    def print_mesh_info(self):
        """
        Function for print mesh informations
        """
        
        print(20*'--')
        print('elements = %d'%self.nelem)
        print('particles per element = %d'%self.ppelem)
        print(20*'--')
            
        for ie in self.elements:
            
            print('element')
            print('id\tn1\txn1\tn2\txn2')
            print('%d\t%d\t%.2f\t%d\t%.2f'%(ie.id,ie.n1.id,ie.n1.x,ie.n2.id,ie.n2.x))
            
            print('particles')
            print('id\txp')
            for ip in ie.particles:    
                print('%d\t%.2f'%(ip.id,ip.position))
                
            print(20*'--')