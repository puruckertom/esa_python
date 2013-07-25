import numpy as np

def fellerarleygrow(N_o, T, r, b, Ite):
    index_set = np.arange(T+1)
    x = np.zeros((Ite,len(index_set)))
    x_mu = np.zeros(len(index_set)) 
    x_mu[0]=N_o
    
    for i in range(0,Ite):                              #starts MC process
        x[i][0]=N_o
        n=0
        
        while n<T:
            x_mu[n+1]=(1+r-b)*x_mu[n]
            if x[i][n]<10000:
                n_birth=np.random.binomial(x[i][n],r)
                n_death=np.random.binomial(x[i][n],b)
                x[i][n+1]=x[i][n]+n_birth-n_death
                if x[i][n+1]<=0:
                    x[i][n+1]=0
                    break
            else:
                x[i][n+1]=(1+r-b)*x[i][n]
            n=n+1
    return x, x_mu



N_t=fellerarleygrow(10,10,0.4,0.9,6)            #Call the defined function
##x_avg=np.average(N_t[0],axis=0)               #Check the average
##print N_t




#Plot the data
import matplotlib.pyplot as plt

plt.plot(N_t[0].T, label="Random",color="red",linewidth=2)
plt.plot(N_t[1].T,"b--",label="Average")
plt.xlabel("Time steps")
plt.ylabel("Number of individuals")
plt.title("Birth-Death Process")
plt.legend()
plt.show()
