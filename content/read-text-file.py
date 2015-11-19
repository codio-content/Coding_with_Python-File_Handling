
filepath= 'content/textfiles/parrot.txt'

# Open the file in filename for reading
file1= open(filepath, 'r')

# Read the entire file into the variable
data = file1.read()

# Print out the contents
print(data)