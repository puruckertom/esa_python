file = open('myFileName.txt')

for line in file:
    print(line)   # line is a string, lets print it!

file.close()

file = open('myFileName.txt')
for line in file:
    print(line)   # line is a string, lets print it!
file.close() 

file = open('myFileName.txt')
for line in file:
    for word in line.split():
        print(word)   # lets print each word!
file.close()

