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