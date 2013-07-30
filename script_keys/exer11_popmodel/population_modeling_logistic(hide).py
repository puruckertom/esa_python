import numpy as np

def logisticgrow(N_o, T, r, K):
    index_set = np.arange(T+1)
    x = np.zeros(len(index_set))
    x[0] = N_o
    
    for t in index_set[1:]:
        x[t] = x[t-1] + (r)*x[t-1]*(1 - x[t-1]/float(K))    #why it is float?
    return x


N_t=logisticgrow(10, 10, 0.4, 100)
print N_t

##print 10/100
##print 10/float(100)
