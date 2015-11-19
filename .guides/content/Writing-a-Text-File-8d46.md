We can write the contents of a variable out to a file all at once after we have opened the file:

```python
7   # open our file for writing
8   file1= open(filepath, 'w')
9
10  # write 'text', to the file at ‘filepath’
11  file1.write(text)
12  file1.close()
```
Make sure you notice that the file was opened with the `'w'` option telling the system we wanted to write to the file. Also note that the we closed the file.

When we want to read the contents of the file that we just wrote, we open the file again for reading with the `'r'` option this time at line 15.

```python
14  # print out the contents of the file
15  file1= open(filepath, 'r')
16  print(file1.read())
17  file1.close()
```

{Run the write sample}(python3 content/write-text-file.py)