# Get the filepath from the command line
F1= sys.argv[2] 
F2= sys.argv[3]

# Your code goes here

#
# Create a function that turns pipe-delimited strings into 2d arrays
# 
def pipe2a(text):
  records= text.split("\n")
  for i in range(0, len(records)):
    records[i]= records[i].split("|")
  return records

#
# Create a function that turns 2d arrays into pipe-delimited strings.
# 
def a2pipe(a):
  text= ""
  for i in range(0, len(a)):
    text = text + "|".join(a[i]) + "\n"
  return text;

#
# Read in the accounts and transactions
# 
accounts= pipe2a(open(F1, 'r').read())
transactions= pipe2a(open(F2, 'r').read())

# ----------------------------------------------------------------
# Main Section
#

# for each transaction
for transactionIndex in range(0, len(transations)):
  transaction= transactions[transactionIndex]
  # look through the accounts for the matching account
  for accountIndex in range(0,len(accounts)):
    account= accounts[accountIndex]
    balance= int(account[2])
    transactionAmount= int(transaction[1])
    if(account[0] == transaction[2]):         # account matches?
      if(account[1] == transaction[3]):       # pin code matches?
        if(transaction[0] == 'add'):          
          accounts[accountIndex][2]= balance + transactionAmount 
        else if (transaction[0] == 'sub' && change <= balance):
          accounts[accountIndex][2]= balance - transactionAmount           

          
# Write the answer back out to the original file
open(F1, 'w').write(a2pipe(accounts))

