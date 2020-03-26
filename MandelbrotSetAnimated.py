#Code taken partly from https://gist.github.com/jfpuget/7849c931dd7b8ef6f952
#Credit jfpuget

from numba import jit
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation

def mandelbrot_image(coordTuple,fig, ax, width=3,height=3,maxiter=80,cmap='hot'):
    dpi = 400
    xmin,xmax,ymin,ymax = coordTuple
    
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    
    #ticks = np.arange(0,img_width,3*dpi)
    #x_ticks = xmin + (xmax-xmin)*ticks/img_width
    #plt.xticks(ticks, x_ticks)
    #y_ticks = ymin + (ymax-ymin)*ticks/img_width
    #plt.yticks(ticks, y_ticks)
    
    norm = colors.PowerNorm(0.7)
    return ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm, animated=True)
    
@jit
def mandelbrot(c,maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter)
    return (r1,r2,n3)
    
def MandelUpdate(i):
	if i != 0 and i <= 50:
		ax.margins(-0.01*i,-0.01*i)
	#plt.xlim(coordArr[0]/(i/2),coordArr[1]/(i/2))
	#plt.ylim(coordArr[2]/(i/2),coordArr[3]/(i/2))
	return m

width=3
height=3
fig, ax = plt.subplots(figsize=(width, height))
ax.use_sticky_edges = False

coordArr = np.array([-2.0,0.5,-1.25,1.25])
m = mandelbrot_image(coordArr,fig, ax, maxiter = 1000,cmap='gnuplot2')

ani = FuncAnimation(fig, MandelUpdate,frames=50, interval=100, blit=False)
plt.show()
