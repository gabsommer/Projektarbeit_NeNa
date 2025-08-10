import matplotlib.pyplot as plt
import numpy as np
import math

n_inner = 4
n_outer = 2
dimer = True


total_radius = n_inner + n_outer



def create_lattice_in(r: int) -> np.ndarray:
    a1 = np.array([1,0],dtype=int)
    a2 = np.array([0,1],dtype=int)
    basis = 0.5*(a1+a2)
    box_y = r+1
    box_x = r+1
    points = np.empty((0,2),dtype=int)
    for i in range(-box_x,box_x):
        for j in range(-box_x,box_y):
            vec = i*a1 + j*a2
            ############################
            if np.linalg.norm(vec) <= r and not (i == 0 and j == 0) :
                points = np.append(points,[vec],axis=0)
                points = np.append(points,[vec+basis],axis=0)
            elif (i == 0 and j == 0):
                points = np.append(points,[vec+basis],axis=0)

    return points

def create_lattice_out(r_in: int,r_out: int) -> np.ndarray:
    a1 = np.array([1,0],dtype=int)
    a2 = np.array([0,1],dtype=int)
    basis = 0.5*(a1+a2)
    box_y = r_out+r_in+1
    box_x = r_out+r_in+1
    points = np.empty((0,2),dtype=int)
    for i in range(-box_x+1,box_x):
        for j in range(-box_x+1,box_y):
            vec = i*a1 + j*a2
            #####################################################################
            if np.linalg.norm(vec) <= r_out+r_in and np.linalg.norm(vec) > r_in :
                points = np.append(points,[vec],axis=0)
                points = np.append(points,[vec+basis],axis=0)
    return points


lattice_inner = create_lattice_in(4)
lattice_outer = create_lattice_out(4,2)

fig, ax = plt.subplots(figsize=(6, 6))



ax.set_ylabel("y-Distance [lattice constants]")
ax.set_xlabel("x-Distance [lattice constants]")
ax.scatter(lattice_inner[:,0],lattice_inner[:,1],label="dynamic NE")
ax.scatter(lattice_outer[:,0], lattice_outer[:,1],label="fixed NE")
ax.grid(True)
if dimer:
    ax.set_title('2D Slice at z=0 of the fcc LAMMPS Setup for Na-Dimer')
    plt.scatter((0,1/2),(0,1/2), color = "red", label="Na")
    ax.legend(loc='upper right')
    plt.savefig("../Inhalt/Bilder/lammps_dimer_setup.png")
    plt.savefig("./lammps_setup.png")
else:
    ax.set_title('2D Slice at z=0 of the fcc LAMMPS Setup for Na-Monomer')
    plt.scatter(0,0,color="red", label="Na")
    ax.legend(loc='upper right')
    plt.savefig("../Inhalt/Bilder/lammps_mono_setup.png")
    plt.savefig("./lammps_setup.png")


