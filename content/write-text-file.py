# set a variable to the path of the file
filepath= '/tmp/out.txt'

# something to write out
text= "A newt?"

# open our file for writing
file1= open(filepath, 'w')

# write 'text', to the file at ‘filepath’
file1.write(text)
file1.close()

# print out the contents of the file
file1= open(filepath, 'r')
print(file1.read())
file1.close()

# write something else out to the same file
file1= open(filepath, 'w')
file1.write('I got better.')
file1.close()

# print out the contents of the file again
file1= open(filepath, 'r')
print(file1.read())
