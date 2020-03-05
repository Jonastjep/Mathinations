#Code taken partly from https://gist.github.com/jfpuget/7849c931dd7b8ef6f952
#Credit jfpuget

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors

def julia_image(N,cmap='hot'):
    z = julia_set(N)
    dpi = 20000
    width = 1+ N//dpi
    height = 1+ N//dpi
    
    fig, ax = plt.subplots(figsize=(width, height),dpi=72)
    
    ax.imshow(z,cmap=cmap,origin='lower')
    plt.show()
    #plt.savefig('JuliaSet{}.png'.format(cmap),bbox_inches='tight',dpi=20000)
    
from numba import jit

@jit
def julia_numba(N):
    T = np.empty((N, 2*N), dtype=np.uint8)
    creal = -0.835
    cimag = - 0.2321
    h = 2.0/N
    for J in range(N):
        for I in range(2*N):
            zimag = -1.0 + J*h
            zreal = -2.0 + I*h
            T[J,I] = 0
            zreal2 = zreal*zreal
            zimag2 = zimag*zimag
            while zimag2 + zreal2 <= 4:
                zimag = 2* zreal*zimag + cimag
                zreal = zreal2 - zimag2 + creal
                zreal2 = zreal*zreal
                zimag2 = zimag*zimag 
                T[J,I] += 1 
    return T
    
julia_set = julia_numba
julia_image(10000)
