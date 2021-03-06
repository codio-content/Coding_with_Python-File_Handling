Now you are ready to start learning about how to read file data. Python provides a way to read an entire file at one time and store the contents into a variable. This means you can skip most of the management of file descriptors and all the other complexities of reading files. 

First, this line gives us a way to work with a specific file. After this call, `file1` is our handle to the file in filepath.
```python
5  file1= open(filepath, 'r')
```

Here, the entire contents of the file is read into a single variable. Since it is a text file, this will result in single string with the entire file contents.

```python
8  var data = file1.read()
```

This shortcut will help you to learn the basics of working with files. However, remember that many files will be too large to read into memory all at once and will have to be processed in small amounts at a time. For now you will work with small files that you can load into memory all at once.

{Run the Sample}(python3 content/read-text-file.py)