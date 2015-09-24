
# read the entire file  
myFile = open('./1-intro/poem.txt')

print(myFile.read())

myFile.close()

# output an empty line
print()

# read line by line
myFile = open('1-intro/poem.txt')

for line in myFile:
  print(line.rstrip())

myFile.close()
