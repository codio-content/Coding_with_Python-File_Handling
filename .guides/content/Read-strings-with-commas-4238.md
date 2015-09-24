{Run the code}(/home/codio/workspace/ch-read.sh)

{Check It!|assessment}(test-3353555413)

|||guidance
### Solution
```python
myFile = open('data.csv')
rows = []

for line in myFile:
  # remove outer white space and new line characers 
  line = line.rstrip()
  
  # split the line at every comma
  # the split() method returns a list of words 
  # which will be a row's columns
  columns = line.split(',')

  # loop over each cell
  # use a generic for loop so we have an index 
  # to store the result of the replace method
  # back into the columns list
  for i in range(0, len(columns)):
    columns[i] = columns[i].replace('|c', ',')
  
  # add the collumns to the rows list
  rows.append(columns)
  
myFile.close()

# display our table of rows and columns
output(rows)
```
|||