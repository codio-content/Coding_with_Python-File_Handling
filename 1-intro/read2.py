
myFile = open('data.csv')
rows = []

for line in myFile:
  # remove outer white space and new line characers 
  line = line.rstrip()
  
  # split the line at every comma
  # the split() method returns a list of words 
  # which will be a row's columns
  columns = line.split(',')

  # add the collumns to the rows list
  rows.append(columns)
  
myFile.close()

# display our table of rows and columns
print(rows)
