# dictionaries
#Slide 2
# bw_grams = {}
# bw_grams['Spring peeper'] = 4
# bw_grams['Bullfrog'] = 500
# bw_grams['Cane toad'] = 1800
# print bw_grams['Bullfrog']

#Slide 3
# print bw_grams['Barking treefrog']
# print 'Barking treefrog' in bw_grams
# print bw_grams.has_key('Barking treefrog')
# print bw_grams.get('Barking treefrog', 'Not found')
# print bw_grams.get('Bullfrog', 'Not found')
# if 'Barking treefrog' not in bw_grams:
# 	bw_grams['Barking treefrog'] = 80
# print bw_grams.get('Barking treefrog', 'Not found')
# another way to set a a value for key
# bw_grams.setdefault('Barking treefrog', 80)

#Slide 4
# male43 = {"sp" : "Orca" , "bw" :10. , "status" : "suscept"}
# print male43
# male43["status"] = "infected"
# print male43

# male4 = {"male43" : male43}
# print male4
# print male4['male43']["status"]

#Slide 5
# bw_grams = {}
# frog = 'Cricket frog'
# weight = '10'
# print bw_grams
# bw_grams['frog'] = frog
# bw_grams['weight'] = weight
# print bw_grams

#Slide 6
#deleting a key
# print bw_grams
# del bw_grams['weight']
# print bw_grams
# a=bw_grams.pop('frog')
# print a
# print bw_grams

#Slide 7
# bw_grams = {}
# bw_grams['Spring peeper' ] = 4
# bw_grams['Bull frog' ] = 500
# bw_grams['Cane toad' ] = 1800

# print bw_grams
# print bw_grams.items()
# print bw_grams.keys()
# print bw_grams.values()

# tmp= bw_grams.iteritems()
# for i in tmp:
# 	print i

# for i in bw_grams:
# 	print i

# for i in bw_grams.items():
# 	print i