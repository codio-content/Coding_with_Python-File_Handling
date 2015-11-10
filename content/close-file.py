
# Example of opening a file and then closing it
path1= sys.argv[2]          # the pathname to some file
path2= sys.argv[3]          # the pathname to some file
path3= sys.argv[4]          # the pathname to some file

# Open first 2 files
print ('Opening first file')
file1= open(path1, 'r')                # open file 1
fd1= file1.fileno()                    # get file descriptor 1
print ('File Descriptor 1: '+str(fd1)) # print the fd number

print ('Opening Second File')
file2= open(path2, 'r')                # open file 2
fd2= file2.fileno()                    # get file descriptor 2
print ('File Descriptor 2: '+str(fd2)) # print the fd number

# Close one, to show that file descriptors are reused
# when we open the next file.
print ('Closing First File')
file1.close()                          # close file 1, freeing fd1

print ('fd ['+str(fd1)+'] is now free for reuse.')

print ('Opening Third File')
file3= open(path3, 'r')                # open file 3
fd3= file3.fileno()                    # get file descriptor 3
print ('File Descriptor 3: '+str(fd3)) # print the fd number

print ('Closing remaining files.')
file2.close()                          # close the file by descriptor
file3.close()                          # close the file by descriptor


