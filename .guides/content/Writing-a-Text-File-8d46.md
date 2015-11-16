We can write the contents of a variable out to a file all at once like this:

```python
// get the path to the file
path= sys.argv[2]      
// something to write out
text= "Some text"       

// open the file for writing
fd1= open(P, 'w')

// write contents of ‘text’
// - to the file ‘path’
fd1.write(text)
```


{Check It!|assessment}(test-1033858382)



|||guidance
### Solution
```python

# Get the filepath from the command line
import sys
I= sys.argv[1] 
O= sys.argv[2] 
S= sys.argv[3]
T= sys.argv[4]

# Your code goes here

# Load the data from the inputPath
f= open(I, 'r')       # open file for read and write
filedata= f.read()    # read the data
f.close()             # close the file

# Create a variable to hold our output while we build it
output= ""

# Find the first occurance of S
positionS= filedata.find(S)

# If positionS is -1, we are done.
while(positionS >= 0) :
  output= output + filedata[0:positionS] + T
  filedata= filedata[positionS + len(S):]
  positionS= filedata.find(S)

output= output + filedata

# Write out the contents.
f2= open(O, 'w')    # open the output file for writing
f2.write(output)    # write the output
f2.close()          # close the file
```
|||