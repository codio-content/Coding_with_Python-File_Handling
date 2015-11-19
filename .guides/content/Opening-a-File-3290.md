Most systems have more than one program running at a time. In order to ensure that multiple programs do not “run into each other” while attempting to use a single file, a program must “open” the file first. This allows the system to restrict access to this file.

```python
7  fileA= open(pathA, 'r')                # open file 1
8  fileB= open(pathB, 'r')                # open file 2
```


{Run the sample}(python3 content/file-descriptor.py)

Python wraps all this file handling business up in a single variable to hide the details from the programmer, allowing us to focus on using the file to get what we want from it.
