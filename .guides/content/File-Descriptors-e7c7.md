Because the handling of files can be different on different systems or types of storage, the programing language provides us with a generic file handling mechanism which abstracts away the details so that we can focus on using the data in the file. 

Most operating systems manage files through a **file descriptor** which controls low level file access. By accessing this **file descriptor** through an abstract interface, we do not have to learn the details of how the operating system manages the file itself, and the interface will remain the same, even if the underlying system is different when our program is run on another system.

These lines show the file descriptor in the sample code:
```python
10  fd1= fileA.fileno()                    # get file descriptor 1
11  fd2= fileB.fileno()                    # get file descriptor 2
12
13  print ('File Descriptor A: '+str(fd1)) # print the fd number
14  print ('File Descriptor B: '+str(fd2)) # print the fd number
```


{Run the sample}(python3 content/file-descriptor.py)