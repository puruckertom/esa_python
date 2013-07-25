# lists
species_names = []
species_names.append("Geospiza fuliginosa") # small
species_names.append("Geospiza fortis") # medium
species_names.append("Geospiza magnirostris") # large
species_names
species_names.sort() #lists are mutable
#sorted(species_names) would not change the list

#mixing types
#None and Boolean types
some_list = [23, 23., 'Frog', None, True]

#list methods
some_list[0]
len(some_list)
[1,2] + [3,4]

#looping over list
for thing in some_list: 
  print thing

# use 'in' to see if elements are in list
'Frog' in some_list
'Bird' in some_list

# deleting list elements
some_list
some_list.pop(0)
some_list
del some_list[2]
del some_list

# tuples
some_tuple = (23,23.,'Frog',None,True)

# slicing
some_tuple[0:2]
some_list[0:2]



