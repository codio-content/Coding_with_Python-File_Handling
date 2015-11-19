import sys

pathA= 'content/textfiles/parrot.txt'
pathB= 'content/textfiles/empty.txt'
pathC= 'content/textfiles/cheese.txt'

fileA= open(pathA, 'r')                # open file 1
fileB= open(pathB, 'r')                # open file 2

fd1= fileA.fileno()                    # get file descriptor 1
fd2= fileB.fileno()                    # get file descriptor 2

print ('File Descriptor A: '+str(fd1)) # print the fd number
print ('File Descriptor B: '+str(fd2)) # print the fd number

fileA.close()                          # close file 1, freeing fd1
print ('Closed FD A ['+str(fd1)+'].')

fileC= open(pathC, 'r')                # open file 3
fd3= fileC.fileno()                    # get file descriptor 3
print ('File Descriptor C: '+str(fd3)) # print the fd number

fileB.close()                          # close the file
fileC.close()                          # close the file