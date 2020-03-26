import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button,TextBox

fig, ax = plt.subplots(figsize=(16,5))
plt.subplots_adjust(bottom=0.25)
ax.set_facecolor("lightgray")
fig.set_facecolor("darkgray")
ax.set_title("Flatten the Curve : A Simple SIR Model for Spread of Infectious Disease ")
################################ ODE PART ################################
#Define the Dif. Eq that needs to be solved
#We have three derivatives, SRI, and everything works through arrays
def SRIp(y,t,transm,recov):
	Sv,Rv,Iv = y
	S = -transm*Sv*Iv
	R = recov*Iv
	I = transm*Sv*Iv-recov*Iv 
	return [S,R,I]

#Initial Values
N = 1
Istart = 0.01
Rstart = 0
Sstart = N-Istart

transm0 = 1.5
recov0 = 0.2

#Time axis
t = np.linspace(0,40,2000)

#Solving the ODE
ODE = odeint(SRIp, [Sstart,Rstart,Istart],t,args = (transm0,recov0))

l1, = ax.plot(t,ODE[:,0],"b",label="Susceptible")
l2, = ax.plot(t,ODE[:,1],"g",label="Recovered")
l3, = ax.plot(t,ODE[:,2],"r",label="Infected")

ax.set_ylabel("% of Population")
ax.set_xlabel("Time")
##########################################################################

axfreq = plt.axes([0.25, 0.09, 0.65, 0.03])
axamp = plt.axes([0.25, 0.13, 0.65, 0.03])

axcolor = "indianred"
srecov = Slider(axfreq, 'Recovery Rate', 0.1, 1, valinit=recov0,facecolor=axcolor)
stransm = Slider(axamp, 'Transmission Rate', 0.1, 5, valinit=transm0,facecolor=axcolor)

def update(val):
	ax.cla()
	transm = stransm.val
	recov = srecov.val
	ODE = odeint(SRIp, [Sstart,Rstart,Istart],t,args = (transm,recov))
	l1, = ax.plot(t,ODE[:,0],"b",label="Susceptible")
	l2, = ax.plot(t,ODE[:,1],"g",label="Recovered")
	l3, = ax.plot(t,ODE[:,2],"r",label="Infected")
	ax.axhline(y=0, color='k',linewidth=0.5)
	ax.axvline(x=0, color='k',linewidth=0.5)
	ax.legend(loc='best')
	ax.set_ylabel("% of Population")
	ax.set_xlabel("Time")
	ax.set_title("Flatten the Curve : A Simple SIR Model for Spread of Infectious Disease ")
srecov.on_changed(update)
stransm.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color="lightgray", hovercolor='0.9')
def reset(event):
	global t
	t = np.linspace(0,40,2000)
	srecov.set_val(0.5)
	submit("40")
	text_box.set_val("40")
	
    
button.on_clicked(reset)

def submit(text):
	x_lim = int(eval(text))
	global t 
	t = np.linspace(0,x_lim,(x_lim/2)*100)
	srecov.set_val(0.5)
	srecov.reset()
	stransm.reset()
axbox = plt.axes([0.25, 0.025, 0.08, 0.04])
text_box = TextBox(axbox, 'Time Length (resets the sliders) ',color="lightgray", initial="40")
text_box.on_submit(submit)

ax.axhline(y=0, color='k',linewidth=0.5)
ax.axvline(x=0, color='k',linewidth=0.5)
ax.legend(loc='best')
plt.show()
