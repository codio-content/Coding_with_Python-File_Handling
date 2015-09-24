
table = [
  [1,3,5,2],
  [5,3,5,6],
  [0,9,7,1]
]

myFile = open('write-demo.csv','w')

# we will keep track of what row number we are on
r = 0

for row in table:
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
    line = line + str(col)
    
    # if we are not at the end of the row and a ','
    if c < len(row):
      line = line + ','  
    
  # write each line once we have assembled all its contents
  myFile.write(line)

  # if we are not at the end of the table write a new line character
  # comment out these two lines 
  # too see what happens if we don't output new line characters
  if r < len(table):
    myFile.write('\n')

myFile.close()
