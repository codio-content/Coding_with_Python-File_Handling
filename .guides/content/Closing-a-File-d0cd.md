To let the system know we are done with a file that we have opened, we need to close it. This signals that it is okay for other programs to use the file now.

```python
16  fileA.close()                       
```

Notice in the code example here, the first two file descriptors have different numbers. Once the first file is closed, the descriptor number goes back in for reuse, so when the next file (3) is opened, the number is reused.

{Run the sample}(python3 content/file-descriptor.py)

If we do not close files when we finish using them, there may be problems accessing the file later, or the system may run out of file resources.