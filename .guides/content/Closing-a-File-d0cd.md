To let the system know we are done with a file that we have opened, we need to close it. This signals that it is okay for other programs to use the file now.

Notice in the code example here, the first two file descriptors have different numbers. Once the first file is closed, the descriptor number goes back in for reuse, so when the next file (3) is opened, the number is reused.

{Run the code}(python run-user.py content/close-file.py content/textfiles/poem.txt content/textfiles/cheese.txt content/textfiles/fixed-length.txt)

If we do not close files when we finish using them, there may be problems accessing the file later, or the system may run out of file resources.