import numpy as np
import matplotlib.pyplot as plt

S=3
T=10
n_o=np.zeros(shape=(S,1))
n_f=np.zeros(shape=(S,T))
l_m=np.zeros(shape=(S,S))

n_o[0]=10
n_o[1]=4
n_o[2]=1
print n_o

l_m[0,0]=2
l_m[0,1]=4
l_m[0,2]=2
l_m[1,0]=0.7
l_m[2,1]=0.4
print l_m

for i in range(0, T):
    n=np.dot(l_m, n_o)
    n_o=n
    n_f[:,i]=n.squeeze()
    
print n_f
print n_f.shape
print n.ndim
print n.squeeze().ndim

# plt.plot(n_f[0,:],label="Age class 1",color="red",linewidth=2)
# plt.plot(n_f[1,:],label="Age class 2",color="blue",linewidth=2)
# plt.plot(n_f[2,:],label="Age class 3",color="black",linewidth=2)
# plt.xlabel("Time steps")
# plt.ylabel("Number of individuals")
# plt.title("Leslie")
# plt.legend()
# plt.show()
