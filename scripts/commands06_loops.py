grade = 80

if grade >= 90:
  print "A"
elif grade >= 80:
  print "B"
elif grade >= 70:
  print "C"
elif grade >= 60:
  print "D"
else:
  print "F"

# boolean
print(bool("alpha"<"beta"))

# through a list of strings with indices
watersheds = ["Suwanne", "Oconee", "Tennessee", "Flint"]
for index, value in enumerate(watersheds):
  print index, value

a = 9
b = 0
c = []
while b < 100:
  b = b + 5
  a = a + 1
  c. append(b)
  print b
  
# break
for number in range(1,8):
 if number < 5:
   print number
 else:
     break

# continue
for number in range(1,8):
    if number == 5:
      continue
    print number
 if number < 5:
   print number
   continue

# pass
for number in range(1,8):
  if number < 5:
    print number
  else:
    pass

