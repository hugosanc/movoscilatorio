#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import *

x=[1]
x1=[1]
v=[0]
v1=[0]
t=[0]
t1=[0]
a=[0]
a1=[0]
dt=0.01
k=1
m=1
g=9.8
gl=1.625
mi=0.003

while (t[-1]<=100):
	t.append(t[-1]+dt)
	x.append(x[-1]+v[-1]*dt+0.5*a[-1]*dt**2)
	a.append(-(k/m)*x[-1]+(-(np.sign(v[-1])*mi*g)))
	v.append(v[-1]+0.5*(a[-2]+a[-1])*dt)
while (t1[-1]<=100):
	t1.append(t1[-1]+dt)
	x1.append(x1[-1]+v1[-1]*dt+0.5*a1[-1]*dt**2)
	a1.append(-(k/m)*x1[-1]+(-(np.sign(v1[-1])*mi*gl)))
	v1.append(v1[-1]+0.5*(a1[-2]+a1[-1])*dt)	


plt.figure(figsize=(8,5),dpi=100)
plt.axis ([0,100,-1,1])
ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.autoscale()

plt.rc('text',usetex=True)
plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
plt.xlabel(r'\textnormal{Tempo} (s)')
plt.ylabel(r'\textnormal{Posicao} (m)')
plt.title(r'\textnormal{Oscilador com atrito e com diferentes valores de "g"}',fontsize=12)

plt.plot(t,x,'-b',linewidth=1,label="Terra")
plt.plot(t1,x1,'-g',linewidth=1,label="Lua")
plt.legend(loc="upper right")
plt.grid()
plt.savefig("terralua.pdf",dpi=96)
plt.show()
