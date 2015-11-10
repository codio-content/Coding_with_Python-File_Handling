# Get the filepath from the command line
I= sys.argv[2] 
O= sys.argv[3] 
S= sys.argv[4]
T= sys.argv[5]

# Your code goes here

# Load the data from the inputPath
f= open(I, 'w')
filedata= f.read()

# Create a variable to hold our output while we build it
output= ""

# Find the first occurance of S
positionS= filedata.find(S)

# If positionS is -1, we are done.
while(positionS >= 0) {
  output= output + filedata[0:positionS] + T
  filedata= filedata[positionS + len(S):]
  positionS= filedata.find(S)
}
output= output + filedata

# Write out the contents.
f.write(output)

# Close the file
f.close()