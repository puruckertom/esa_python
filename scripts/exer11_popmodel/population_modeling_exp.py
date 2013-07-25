import numpy as np

def exponentialgrow(N_o , r,  T):
    index_set = np.arange(T+1)	            #How to do this in np.linspace?
##    index_set = np.linspace(0,T,T+1)
    x = np.zeros(len(index_set))	    #create an array to hold the results
    x[0] = N_o			            #initial condition

    for t in index_set[1:]:		    #t starts at 0, ends at T
        x[t] = N_o*np.exp(r*t)
    return x


N_t=exponentialgrow(10, 0.4, 10)            #Call the defined function
print N_t
