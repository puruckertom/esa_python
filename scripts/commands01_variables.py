#check for libraries
import sys
sys . version
import numpy
import scipy
#import matplotlib

#implicitly assign different types to variables
pop_size = 112 # integer
print type(pop_size)
pop_density = 4 # still an integer
print type(pop_density)
pop_density = 4. # now its a float
print type(pop_density)
species_name = "Oedipina complex" # string
print type(species_name)
species_name = "4" # still a string
print type(species_name)

#be careful about int versus float
pop_size = 1086
area = 1254
pop_density = pop_size/area
print pop_density
print 'pop_density = ' + str(pop_density)
print type(pop_density)
#need to make pop_size and/or area a float
area = 1254.
pop_density = pop_size/area
print pop_density
print 'pop_density = ' + str(pop_density)
print type(pop_density)
