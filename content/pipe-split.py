# ----------------------------------------------------------------
# My Pipe Delimited String Functions 
# ----------------------------------------------------------------

# function returns a list from a pipe dlimited string
def getListFromPipeDelimitedText(pipeDelimitedText):
  recordList= pipeDelimitedText.split('|')
  return recordList

# function returns a pipe delimited string from a list
def getPipeDelimitedTextFromList(recordList):
  return ('|').join(recordList)

# function which will print out all of our records
def printRecords(recordList):
  for i in range(0,len(records)):
    print('Record '+ str(i) +': ('+ str(records[i]) +')')

# ----------------------------------------------------------------
# Main Section
# ----------------------------------------------------------------
data= '100|1000|1|999999|700'                # sample data
print(data)                                  # print data

records= getListFromPipeDelimitedText(data)  # create records
printRecords(records)                        # and print them

data2= getPipeDelimitedTextFromList(records) # make a string
print(data2)                                 # print it
