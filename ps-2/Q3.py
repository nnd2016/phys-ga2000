# -*- coding: utf-8 -*-


M = 0  # Madelung constant 
L = 100  # number of atoms

for i in range (-L, L + 1):
    for j in range (-L, L + 1):
        for k in range (-L, L + 1):
            if (i == j == k == 0): # excluding the atom at the origin since it is the test charge
                continue
                
            V = (i ** 2 + j ** 2 + k ** 2) ** -0.5 # potential at index (i, j, k) without constants
            
            if (i + j + k) % 2 == 1: # for when the sum of the indices is odd
                V *= -1
                
            M += V
            
print ('The Madelung Constant is', M )

