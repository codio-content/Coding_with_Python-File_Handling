
# sample data with records 6 characters long
data= '   100  1000     1999999   700'
print(data)

recordLength= 6
start= 0
records= []

# use the substring function to read all the records
while( (len(data) - start) >= recordLength):
  record= data[start:start + recordLength]
  records.append(record)
  start+= recordLength

# print out all of our records
for i in range(0,len(records)):
  print('Record '+ str(i) +': ('+records[i]+')')
