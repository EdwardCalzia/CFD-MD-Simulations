
from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np

# define lattice vectors
lat=[[1.0,0.0],[0.5,np.sqrt(3.0)/2.0]]
# define coordinates of orbitals
orb=[[1./3.,1./3.],[2./3.,2./3.]]

# make two dimensional tight-binding graphene model
my_model=tb_model(2,2,lat,orb)

# set model parameters
delta=0.0
t=-1.0

# set on-site energies
my_model.set_onsite([-delta,delta])
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t, 0, 1, [ 0, 0])
my_model.set_hop(t, 1, 0, [ 1, 0])
my_model.set_hop(t, 1, 0, [ 0, 1])

# visualize infinite model

# cutout finite model along direction 0
cut_one=my_model.cut_piece(8,0,glue_edgs=False)


# cutout finite model along direction 1 as well
cut_two=cut_one.cut_piece(8,1,glue_edgs=False)
#
(fig,ax)=cut_two.visualize(0,1)
ax.set_title("Graphene, finite")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_finite.pdf")

print('Done.\n')
