We are now ready to start reading file data. Python provides a way to read an entire file at one time and store the contents into a variable. This allows us to skip most of the management of file descriptors and all the other complexities of reading files. 

First, this line gets us a way to work with a specific file. After this call, `file` is our handle to the file in filepath.
```python
5  file1= open(filepath, 'r')
```

Here, we read the entire contents of the file into a single variable. Since it is a text file, this will result in single string with the entire file contents.

```python
8  var data = file1.read()
```

While this shortcut will help us learn the basics of working with files, remember that many files will be too large to read into memory all at once and will have to be processed in small amounts at a time. But for now we will work with small files that we can load into memory all at once. We will return to file descriptors in a later lesson.

{Run the Sample}(python3 content/read-text-file.py)