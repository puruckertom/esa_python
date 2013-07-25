#!/usr/bin/python

#This is not the cleanest way of doing it how can we improve
def printListDupes(list):
	dupes = []
	for item in list:
		if list.count(item) > 1 and (dupes.count(item) < 1):
			dupes.append(item)
			print item

def reverseUniqueSortList(list):
	uniques = []
	print list
	print uniques
	for item in list:
		if uniques.count(item) == 0:
			uniques.append(item)
	uniques.sort()
	uniques.reverse()
	return uniques

def push(list, item):
	list.append(item)
	
def peek(list):
	item = list.pop()
	push(list,item)
	return item

list = [0,1,2,3]
list.append(5)
print list
list.extend(list)
print list
list.insert(0,-1)
print list
list.remove(-1)
print list
list.pop(0)
print list
print list.count(1)
list.sort()
print list
list.reverse()
print list
list = [0,1,2,1,3,4,1,3]
printListDupes(list)
newList = reverseUniqueSortList(list)
print newList
push(newList,5)
print newList
item = peek(newList)
print item
print newList
