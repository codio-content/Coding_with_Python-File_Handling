The way files are handled can be different depending on the system and type of storage used. However, programming languages provide a generic file handling mechanism which removes the unwanted details (this is also known as abstraction in computing). This allows you to focus on using the data in the file. 

Most operating systems manage files through a **file descriptor** which controls low level file access. By accessing the **file descriptor** through an abstract interface, you do not have to learn the details of how the operating system manages the file itself, and the interface will remain the same, even if the underlying system is different when the program is run on another system.

These lines show the file descriptor in the sample code:
```python
10  fd1= fileA.fileno()                    # get file descriptor 1
11  fd2= fileB.fileno()                    # get file descriptor 2
12
13  print ('File Descriptor A: '+str(fd1)) # print the fd number
14  print ('File Descriptor B: '+str(fd2)) # print the fd number
```

{Run the sample}(python3 content/file-descriptor.py)