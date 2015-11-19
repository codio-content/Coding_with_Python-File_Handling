
{Check It!|assessment}(test-2484565952)

|||guidance
### Solution
```python
# Get the filepath from the command line
import sys
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]

# Your Code Goes Here

f= open(P, 'r')  # Open the file
data= f.read()   # Read the contents of P into `data`
f.close()        # close the file

# Create a list of all the records
recordList= []
while(len(data) > 0):
  record= []
  record.append(data[0:16])
  record.append(data[16:32])
  record.append(data[32:40])
  recordList.append(record)
  data= data[40:]

# Find the matching name
output= ''
for i in range(0, len(recordList)):
  thisRecord= recordList[i]
  if(thisRecord[0].strip() == F and thisRecord[1].strip() == L):
    thisRecord[2]= B
  # Either way, write the record out
  output+= thisRecord[0] + thisRecord[1] + thisRecord[2]

f= open(P, 'w')     # open the file for output
f.write(output)     # write the output
f.close()           # close the file

```
