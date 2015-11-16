# Get the pathname from the command line
import sys
pathname= sys.argv[1]

# Opens a file named “pathname”
# Returns a file descriptor we will 
# use to access the file until we are done with it.
file= open(pathname, 'r')

# Python has a special way to see the file descriptor
# for an open file
fd= file.fileno()

print("File Descriptor: " + str(fd))

