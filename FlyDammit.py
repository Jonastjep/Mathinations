import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

#SAVE AS GIF (-> GIF = True) OR SHOW PLOT  (-> GIF = False) 
GIF = False

from matplotlib import rcParams
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsthm}', r'\usepackage{amsmath}', r'\usepackage{amssymb}',r'\usepackage{amsfonts}', r'\usepackage[T1]{fontenc}', r'\usepackage[utf8]{inputenc}', r'\usepackage{multicol}'
rcParams['legend.handleheight'] = 3.0
#This fixes the legend line be placed at same height that text legend

plt.style.use('dark_background')

def update_line(num, data, line):
	line.set_data(data[..., :num])
	return line,

def FlyDamn(arr, n):
	if (math.gcd(n,arr[n-1]) == 1):
		arr.append(arr[n-1]+n+1)
	else:
		arr.append(int(arr[n-1]/math.gcd(n,arr[n-1])))

numpoints = 1000
x = [0,1]
y = [1,1]
for i in range(2,numpoints):
	x.append(i)
	FlyDamn(y,i)

data = np.array([x,y])

fig1 = plt.figure()

l, = plt.plot([], [], 'o', ms=2.5) #ms for marker size and 'ro' for the red dots, no lines
plt.xlim(0, numpoints)
plt.ylim(-50, numpoints*3)
plt.xlabel('n')
plt.ylabel('a(n)')

tex = r'$a(n)=\left\{\begin{array}{lr} a(n-1)+n+1 & : gcd(n,a(n-1)) = 1\\ \frac{a(n-1)}{gcd(n,a(n-1))} & : gcd(n,a(n-1)) > 1\end{array}\right\}$'
plt.legend([tex], handletextpad=-2.0, markerscale=0, fancybox=True)
	
plt.title('Fly Dammit (Numberphile Video)')
line_ani = animation.FuncAnimation(fig1, update_line, numpoints, fargs=(data, l),interval=25, blit=True)

if GIF == False:
	plt.show()
else:
	line_ani.save('FlyDammit.mp4')
	print("Your GIF is ready.")

