# 1 Read a file
# 1.1 Read StateOfTheUnion.txt
# 1.2 Output each word on its own line
# file = open("StateOfTheUnion.txt")
# for line in file:
# 	print (line)
# file.close()

# 2 Sum a file
# 2.1 Read IntegerFile.txt, which has many numbers on one line.
# 2.2 Calculate the sum, and the mean. Hint, the int() function
# turns a string into a number.
# num_all=[]
# file = open("IntegerFile.txt")
# for line in file:
# 	for word in line.split():
# 		num_all.append(int(word))
# file.close()
# print sum(num_all)

# 3 File copier
# 3.1 Copy http://www.ubertool.org/index.html to a file on your local disk.
# import urllib2
# file = urllib2.urlopen('http://www.ubertool.org/index.html')
# file_read = file.read()
# print file_read
# file_out = open('save_out.txt', 'w')
# file_out.write(file_read)
# file_out.close()
# file.close()