import numpy as np
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

# 20x20 Lattice
L = 20

# number of iterations
it = 25000

T = 1
Tn = 4
sp = 0.02
st = int((Tn-T)/sp)

E = []
M = []
C = []
S = []
t = np.linspace(T,Tn,num=st)

for h in tqdm(range(st)):
    
    l = np.random.choice([1,-1],size=(L,L))
    T += sp
    eng = 0
    eng2 = 0
    mag = 0
    mag2 = 0

    for k in range(it):
        x = np.random.rand()
        m = np.random.randint(20)
        n = np.random.randint(20)
        a = l[m,n]
        de = 2*a*(l[(m+1)%20,n] + l[(m-1)%20,n] + l[m,(n+1)%20] + l[m,(n-1)%20])
        y = math.exp(-de/T)
        if de<0 or x<y:
            l[m,n] = -a
    for i in range(L):
        for j in range(L):
            a = l[i,j]
            h = a*(l[i,(j+1)%L]+l[i,(j-1)%20]+l[(i+1)%L,j]+l[(i-1)%L,j])
            h2 = h*h
            eng = eng - h
            eng2 = eng2 + h2
            
    mag = np.sum(l) 
    mag2 = np.sum(l*l)
    E.append(eng/(2*L**2))
    M.append(mag/L**2)
    C.append((eng2/(4*L**2) - eng**2/(4*L**4))/T**2)
    S.append((1 - mag**2/L**4)/T)


plt.figure(figsize=(12,12), dpi=95)
plt.subplot(221)
plt.plot(t,E,'.r')
plt.xlabel('Temperature')
plt.ylabel('Average Energy')
plt.subplot(222)
plt.plot(t,M,'.b')
plt.xlabel('Temperature')
plt.ylabel('Magnetisation per Spin')
plt.subplot(223)
plt.plot(t,C,'.g')
plt.xlabel('Temperature')
plt.ylabel('Specific Heat Capacity')
plt.subplot(224)
plt.plot(t,S,'.k')
plt.xlabel('Temperature')
plt.ylabel('Magnetic Susceptibility')
plt.show()

