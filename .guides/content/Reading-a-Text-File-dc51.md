We are now ready to start reading file data. Python provides a way to read an entire file at one time and store the contents into a variable. This allows us to skip most of the management of file descriptors and all the other complexities of reading files. 

```python
// open the file for reading
fd1= open(filepath, 'r') 

// read the entire file
text= fd1.read()

// `text` now contains the entire content of the file
```

While this shortcut will help us learn the basics of working with files, remember that many files will be too large to read into memory all at once and will have to be processed in small amounts at a time. But for now we will work with small files that we can load into memory all at once. We will return to file descriptors in a later lesson.

{Check It!|assessment}(test-1572606935)


|||guidance
### Solution
```python
# Load our command line arguments
import sys
P= sys.argv[1]
S= sys.argv[2]

# Your code goes here

# Read in the data from our file
f = open(P, 'r')
data= f.read()

# Run through the file data, counting S.

counter= 0                         # counter variable
nextIndex= data.find(S)            # find first occurence of S
while(nextIndex >= 0):             # while we found another S
  counter= counter + 1             # increment the counter
  data= data[nextIndex + len(S):]  # remove the text we searched
  nextIndex= data.find(S)          # look for S again

print(counter)                      # print the result
```
|||