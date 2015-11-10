Because the handling of files can be different on different systems or types of storage, the programing language provides us with a generic file handling mechanism which abstracts away the details so that we can focus on using the data in the file. 

Most operating systems manage files through a **file descriptor** which controls low level file access. By accessing this **file descriptor** through an abstract interface, we do not have to learn the details of how the operating system manages the file itself, and the interface will remain the same, even if the underlying system is different when our program is run on another system.

