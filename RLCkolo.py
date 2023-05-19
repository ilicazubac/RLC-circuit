import numpy as np
import matplotlib.pyplot as plt

def promstr(i,S):
    return -R/L*S-i/L/C

R=1 #om
V=1 #V
C=1 #F
L=15 #H
t0=0 #s
tk=200 #s
n=1001
i0=V/R
S0=0
t=np.linspace(t0,tk,n)
i=np.zeros(n)
S=np.zeros(n)
Dt=(tk-t0)/(n-1)

for k in range (0,n-1):
    i[0]=i0
    t[0]=t0
    S[0]=S0
    i[k+1]=i[k]+Dt*S[k]
    S[k+1]=S[k]+Dt*promstr(i[k+1],S[k])

plt.plot(t,i,label="aproksimativno resenje")
plt.xlabel("Vreme [s]")
plt.ylabel("jacina struje [A]")
plt.show()