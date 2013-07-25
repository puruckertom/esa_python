def countdown(n): 
	if n == 0:
		print "Blastoff!" 
	else:
		print n 
		countdown(n-1)


def fibonacci( n ):

   if n == 0 or n == 1:  # base case
      	print "*"
	return n
   else:
      	# two recursive calls
	print "*"
	print "*"
      	return fibonacci( n - 1 ) + fibonacci( n - 2 )

def factorial(n):
	if n == 0: 
		return 1
  	else: 
		return n*factorial(n-1);

def recursive_sum(list):
    sum = 0
    for element in list:
        if type(element) == type([]):
            sum += recursive_sum(element)
        else:
            sum += element
    return sum



countdown(10)
fibonacci(10)
test = [0,1,2,3,4,5]
rec_sum = recursive_sum(test)
print rec_sum
print factorial(10)
