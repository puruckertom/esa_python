def print1Var(var0):
	print var0

def add2Vars(var0, var1):
	sum = var0 + var1
	return sum

def getTuple(var0, var1, var2, var3):
	returnTuple = (var0, var1, var2, var3)
	return returnTuple

def reverseVarsIntoList(var0, var1, var2, var3):
	returnList = [var3, var2, var1, var0]
	return returnList

print1Var(1)
var = add2Vars(1,2)
print var
var = getTuple(1,2,3,4)
print var
var = reverseVarsIntoList(1,2,3,4)
print var


