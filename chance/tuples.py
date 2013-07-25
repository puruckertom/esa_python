#!/usr/bin/python
tuple =('a','b','c','d')
print(tuple[0:3]==('a','b','c','d'))
print(tuple[0:3]==('a','b','c'))
print(tuple[0:3]==1,2,3)
tuple=tuple + ('e',)
tuple=tuple + ('f')
tuple = tuple + 'f'
a=1
b=2
print a,b
a,b = b,a
print a,b
result = ()
for tuple in x:
	max = 0
	for value in tuple:
		if value > max:
			max = value
		result = result + (max, )
print result


