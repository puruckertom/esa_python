import numpy as np

def fellerarleygrow(N_o,T,r,b):
    index_set = np.arange(T+1)
    x = np.zeros(len(index_set))
    x_mu = np.zeros(len(index_set)) 
    x_mu[0]=N_o
    x[0]=N_o
    n=0
    
    while n<T:
        x_mu[n+1]=(1+r-b)*x_mu[n]                   #calculate the average numeber
        
        if x[n]<10000:
            n_birth=np.random.binomial(x[n], r)     #the number of birth in one time step
            n_death=np.random.binomial(x[n], b)
            x[n+1]=x[n]+n_birth-n_death
            
            if x[n+1]<0:                            #cent
                x[n+1]=0 
##        else:                                     #question 1: where should I put this else statement?
##            x[n+1]=(1+r-b)*x[n]
            else:                       
                x[n+1]=(1+r-b)*x[n]                
        n=n+1
    return x, x_mu



N_t=fellerarleygrow(10,10,0.4,0.3)            #Call the defined function
print N_t
