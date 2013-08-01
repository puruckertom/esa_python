import numpy as np
#Slide 4
# a=np.array([10, 20, 30, 40], float)
# b=np.array([10, 20, 30, 40])
# print a
# print b
# c = np.array([[1, 2],[4, 5]])
# print c
# d = np.array([[1, 2],[4, 5.0]])
# print d
# e = np.array([[1., 2],[4, 5]])
# print e

#Slide 5
# f = np.arange(0,4,1)
# print f
# g = np.arange(4)
# print g

#Slide 6
# h = np.linspace(2.0, 3.0, num=5)
# print h
# i = np.linspace(2.0, 3.0, num=5, endpoint=False)
# print i
# j = np.linspace(2.0, 3.0, num=5, retstep=True)
# print j

#Slide 7
# x = np.zeros((2,3),float)
# print x
# x = np.identity(3, float)
# print x

#Slide 8
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# print a.shape
# print a.reshape(1,6)
# print a.ndim
# print a.dtype
# print a.size

#Slide 9
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# print a
# k = a.flatten()
# print k

# l=a.tolist()
# print l 
# print type(l)

#Slide 10
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# m = a.transpose()
# print m

# p = np.array([[1, 2], [3, 4]])
# q = np.array([[5, 6], [7,8]])
# r = np.concatenate((p,q), axis=0)
# s = np.concatenate((p,q), axis=1)
# print r
# print s

#Slide 11
# a = np.arange(10)
# print a 
# print a[5]
# print a[3:5]


#Slide 12
# a = np.arange(10)
# print a[:3]
# print a[:-7]

#Slide 13
# a = np.arange(10)
# print a[::-1]
# print a[::-3]

#Slide 14
# a = np.arange(10)
# print a 
# a[2:4]=[100,101]
# print a
# print a[1:5:2]
# print a[1:-1:2]
# print a[1:100:2]
# print a[1::2]

#Slide 15
# x = np.arange(9.).reshape(3, 3)
# print x
# print np.where( x > 4.5 )

#Slide 16-17
# print np.random.rand(2, 3)
# print np.random.randn(2, 3)
# print np.random.lognormal(2, 1, (2,3))
# print np.random.poisson(5, (2,3))
# print np.random.beta(5, 2, (2,3))

# np.random.seed(1000)
# print np.random.rand(2, 3)
# np.random.seed(1000)
# print np.random.rand(2, 3)

#Slide 18
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# print a 
# print a.sum()
# print a.sum(axis=0)
# print a.mean()
# print a.var()

#Slide 19
# a = np.array([[1, 2, 2], [4, 5, 4]], float)
# print a
# print a.min()
# print a.argmax()
# print np.unique(a)
# print a.diagonal()

#Slide 20
# a = np.array([[1, 2], [4, 5]], float)
# print a
# b = np.linalg.inv(a)
# print b
# print np.linalg.det(a)

#Slide 21
# a = np.array([[1, 2], [4, 5]], float)
# b = np.linalg.inv(a)
# print np.dot(a,b)
# print a*b
# c = np.linalg.solve(a,b)

#Slide 22
# a = np.arange(0, 60, 10)
# b = a
# print a
# print b
# a[0] = 100
# print a
# print b 

#Slide 23
# import copy
# a = np.arange(0, 60, 10)
# b= copy.deepcopy(a)
# print a
# print b 
# a[0]=100
# print a
# print b 

