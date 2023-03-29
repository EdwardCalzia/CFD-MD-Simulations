from pythtb import tb_model, wf_array
import numpy as np
import matplotlib.pyplot as plt

# define lattice vectors and coordinates of orbitals
lat = [[1.0,0.0],[0.5,np.sqrt(3.0)/2.0]]
orb = [[1./3.,1./3.],[2./3.,2./3.]]

# create tight-binding graphene model and set parameters
my_model = tb_model(2,2,lat,orb)
delta, t = -0.1, -1.0
my_model.set_onsite([-delta,delta])
my_model.set_hop(t, 0, 1, [0,0])
my_model.set_hop(t, 1, 0, [1,0])
my_model.set_hop(t, 1, 0, [0,1])

# print tight-binding model
my_model.display()

# compute Berry phase along circular path
circ_step, circ_center, circ_radius = 31, np.array([1/3, 2/3]), 0.05
w_circ = wf_array(my_model, [circ_step])
for i in range(circ_step):
    ang = 2*np.pi*i/(circ_step-1)
    kpt = circ_radius*np.array([np.cos(ang), np.sin(ang)]) + circ_center
    w_circ.solve_on_one_point(kpt, i)
w_circ[-1] = w_circ[0]
print(f'Berry phase along circle with radius {circ_radius}:')
for b in range(2):
    print(f'  for band {b} equals :', w_circ.berry_phase([b], 0))

# compute Berry flux on square patch
square_step, square_center, square_length = 31, np.array([1/3, 2/3]), 0.1
w_square = wf_array(my_model, [square_step, square_step])
all_kpt = np.zeros((square_step, square_step, 2))
for i in range(square_step):
    for j in range(square_step):
        kpt = square_length*np.array([i, j])/(square_step-1) - square_length/2 + square_center
        all_kpt[i,j,:] = kpt
        (eval, evec) = my_model.solve_one(kpt, eig_vectors=True)
        w_square[i,j] = evec
print(f'Berry flux on square patch with length {square_length}:')
for b in [0, 1, [0,1]]:
    print(f'  for band {b} equals :', w_square.berry_flux([b]))

# plot Berry phase on each small plaquette of the mesh
plaq = w_square.berry_flux([0], individual_phases=True)
plt.imshow(plaq.T, origin='lower', extent=(all_kpt[0,0,0], all_kpt[-2,0,0],
                                           all_kpt[0,0,1], all_kpt[0,-2,1],))
plt.title('Berry curvature near Dirac cone')
plt.xlabel(r'$k_x$')
plt.ylabel(r'$k_y$')
plt.tight_layout()
plt.savefig('cone_phases.pdf')
print('Done.\n')
