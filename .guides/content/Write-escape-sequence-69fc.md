{Run the code}(/home/codio/workspace/ch-write.sh)

{Check It!|assessment}(test-808628205)

|||guidance
### Solution
```python
input0 = input0([ 
  ['Mary had a little lamb', '24'], 
  ['This, that and the other', '14'] 
])

myFile = open('data.csv','w')

# we will keep track of what row number we are on
r = 0

for row in input0:
  # increase the row
  r = r + 1
  
  # create a new empty string to hold the line's contents
  line = ''
  
  # we will keep track of what column we are on in a row 
  c = 0

  for col in row:
    # increase the column
    c = c + 1

    # add the cell's contents to the end of the line
    escaped = col.replace(',', '|c')
    line = line + escaped
    
    # if we are not at the end of the row and a ','
    if c < len(row):
      line = line + ','  
    
  # write each line once we have assembled all its contents
  myFile.write(line)

  # if we are not at the end of the table write a new line character
  # comment out these two lines 
  # too see what happens if we don't output new line characters
  if r < len(input0):
    myFile.write('\n')

myFile.close()
```
|||