#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import matplotlib.pyplot as plt


# In[1]:


def Vpot(x):  # Pozo de potencial
    y=np.piecewise(x, [x < -1, x >= 1],[lambda x:20, lambda x:20])
    return y

#def Vpot(x):   # V(z)=z^2
 #   return x**2/2.


# In[156]:


a = float(input('limite inferior: '))
b = float(input(':limite superior '))
N = int(input('numero de pasos: '))


# In[157]:


x = np.linspace(a,b,N)
h = x[1]-x[0]
plt.plot(x,Vpot(x))


# In[158]:


T = np.zeros((N-2)**2).reshape(N-2,N-2)
for i in range(N-2):
    for j in range(N-2):
        if i==j:
            T[i,j]= -2
        elif np.abs(i-j)==1:
            T[i,j]=1
        else:
            T[i,j]=0


# In[159]:


V = np.zeros((N-2)**2).reshape(N-2,N-2)
for i in range(N-2):
    for j in range(N-2):
        if i==j:
            V[i,j]= Vpot(x[i+1])
        else:
            V[i,j]=0


# In[160]:


H = -T/(2*h**2) + V


# In[161]:


#Energía (Autovalores)
val,vec=np.linalg.eig(H)
z = np.argsort(val)
z = z[0:4]
energies=(val[z]/val[z][0])
print(energies)


# In[111]:


plt.figure(figsize=(12,10))
for i in range(len(z)):
    y = []
    y = np.append(y,vec[:,z[i]])
    y = np.append(y,0)
    y = np.insert(y,0,0)
    plt.plot(x,y,lw=3, label="{} ".format(i))
    plt.xlabel('x', size=14)
    plt.ylabel('$\psi$(x)',size=14)
plt.legend()
plt.title("normalized wavefunctions",size=14)
plt.show()


# In[ ]:





# In[89]:


3/2**0.5


# In[ ]:




