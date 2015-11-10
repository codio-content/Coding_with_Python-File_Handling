Once we know the format of a file, how to do we load and read it? There are many file formats and reading many of them is beyond the scope of this lesson. But we will learn about some common methods for organizing files.

One simple way to organize files is to establish an exact length for a record, which allows us to know how much data to read and write for each record. For example, our format might specify 16 characters for first name, 16 for a last name, and 8 for a birthday in MMDDYYYY order. 

Our file would look like this:

`Adam____________Smith___________11111985`
`Theodore________Anderson________03201990`
`Monty___________Biscuit-Barrel__10181980`

Note that there are no newline characters at the end of the records. It is split up here so we can read it.

**Hint:** you might find the `trim()` function helpful. It removes whitespace from the front and end of a string.

{Check It!|assessment}(test-1456892332)

|||guidance
### Solution
```python
// Get the filepath from the command line
P= sys.argv[2] 
F= sys.argv[3]
L= sys.argv[4]
B= sys.argv[5]

// Your code goes here
f= open(P, 'r')

// Read the contents of P into `data`
data= f.read()

// Create a list of all the records
var recordList= []
while(data.length > 0){
  var record= []
  record[0]= data.substring(0,16)
  record[1]= data.substring(16,32)
  record[2]= data.substring(32,40)
  recordList.push(record)
  data= data.substring(40)
}

// Find the matching name
var output= ''
for(var i=0; i < recordList.length; i++){
  var thisRecord= recordList[i]
  if(thisRecord[0].trim() == F && thisRecord[1].trim() == L){
    thisRecord[2]= B
  }
  output+= thisRecord[0] + thisRecord[1] + thisRecord[2]
}

// Write out the finished string to our file P
fs.writeFileSync(P, output, 'utf8')

```
