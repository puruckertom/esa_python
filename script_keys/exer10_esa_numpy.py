import numpy as np

#create a 1 dim array 
a=np.array([10,20,30,40])
print a
print a.shape

#create a 2 dim array 
b = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print b

#change the shape of b
print b.shape
b.reshape(4,3)
print b

b.shape=6,-1
print b
print b.shape

#create an array with assigned data type
b = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]],dtype=float)
print b.dtype
print b

#create an array using np.arange
np.arange(0,4,1)
np.arange(4)

#create an array using np.linespace
a = np.linspace(2.0, 3.0, num=5, endpoint= True, retstep=True)
print a
b = np.linspace(2.0, 3.0, num=5, endpoint= False, retstep=True)
print b

#structured array

persontype = np.dtype({'names':['name', 'age', 'weight'],'formats':['S32','i', 'f']})
a = np.array([('Name A',32,75.5),('Name B',24,65.5)], dtype=persontype)

print a
print a['name']
print a['age'][0]
a['name'][0]='tao'
print a

#fromfunction
def func(i):
    return i%4+1

a=np.fromfunction(func,(5,))
print a

#other properties
a = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]],dtype=float)
print a.shape
print a.ndim
print a.dtype
print a.size

for i in a.flat:
    print i

################
 ##indexing###
################
import numpy as np
a = np.arange(10)

print a[5]
print a[3:5]
print a[:5]
print a[:-1]

print a[::-1][::2]
b = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
c= b[:,::-1]
print b
print c

a[2:4] = 100,101
print a
a[1:-1:2]
print a

x = np.arange(10)
print x
print x[[3, 3, -3, 8]]














