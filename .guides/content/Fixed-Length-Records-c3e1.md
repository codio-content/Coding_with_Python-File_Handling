Once we know the format of a file, how to do we load and read it? There are many file formats and reading many of them is beyond the scope of this lesson. But we will learn about some common methods for organizing files.

One simple way to organize files is to establish an exact length for a record, which allows us to know how much data to read and write for each record. For example, our format might specify 16 characters for first name, 16 for a last name, and 8 for a birthday in MMDDYYYY order. 

Our file would look like this:

`Adam____________Smith___________11111985`
`Theodore________Anderson________03201990`
`Monty___________Biscuit-Barrel__10181980`

Note that there are no newline characters at the end of the records. It is split up here so we can read it.


### The `String.strip()` Function
----
You might find the `strip()` function helpful. It removes whitespace from the front and end of a string.

```python
text= '  Words   Other   Words\tTab   '
print(':' + text + ':')
text= text.strip()
print(':' + text + ':')
```
{Run the code}(python content/strip.py)



{Check It!|assessment}(test-2484565952)

|||guidance
### Solution
```python
# Get the filepath from the command line
P= sys.argv[2] 
F= sys.argv[3]
L= sys.argv[4]
B= sys.argv[5]

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
