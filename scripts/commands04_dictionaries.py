# dictionaries
bw_grams = {}
bw_grams['Spring peeper'] = 4
bw_grams['Bullfrog'] = 500
bw_grams['Cane toad'] = 1800
print bw_grams['Bullfrog']

#searching a dictionary
print bw_grams['Barking treefrog']
'Barking treefrog' in bw_grams
print bw_grams.get('Barking treefrog', 'Not found')

# setting a default value for a key
if 'Barking treefrog' not in bw_grams:
  bw_grams['Barking treefrog'] = 80

# another way to set a a value for key
bw_grams.setdefault('Barking treefrog', 80)

# mixing types
male43 = {"sp":"Orca", "bw":10., "status":"suscept"}
male43["status"] = "infected"
male43

#deleting a key
del bw_grams['infected']
