def compareTwoVariables(var0, var1):
	if var0>var1:
		print "var0 is greater than var1"
	else:
		print "var1 is greater than var 0" 

def compareTwoVariablesCorrect(var0, var1):
	if var0>var1:
		print "var0 is greater than var1"
	elif var0<var1:
		print "var1 is greater than var0" 
	else:
		print "var0 is equal to var1"


if 2 > 1:
	print "1 is greater than 2"
if 1 > 2:
	print "Something is wrong here"

compareTwoVariables(2,1)
compareTwoVariables(1,2)
compareTwoVariables(1,1)
compareTwoVariablesCorrect(2,1)
compareTwoVariablesCorrect(1,2)
compareTwoVariablesCorrect(1,1)

