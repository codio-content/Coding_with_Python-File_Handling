One of the simpler file types are text files. The file on the bottom left shows the first verse of a poem. 

{Run the code}(python3 run-user.py ./1-intro/poem.py)

## Reading it in
The code on the top left shows two ways we can read in the `poem.txt` file and display it. Before we can read the file it must be opened using the `open('filename')` function. 

The first example uses the open file's `read()` method to return all the lines at once:

```python
myFile.read()
```

While the second version uses a loop to iterate through all the lines in a file. We need to use the line's `rstrip()` method to remove any white space including the new line characers. Tryin removing to `.rstrip()` and see what happens.

```python
for line in myFile:
  print(line.rstrip())
```

When you are done working with the file you should close it using its `close()` method. It is not essential to do this when reading files, as nothing has been changed, but it is good practice as it lets the operating system know you are done using it and other programs may access it.
