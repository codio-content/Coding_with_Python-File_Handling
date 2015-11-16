For your final challenge of this Unit, we will load two files. The first file **( F1 )** will have information about some accounts. It will be pipe-delimited and have one record per line, with these fields:

`ACCOUNT NUMBER | PIN CODE | BALANCE`

The second file **( F2 )** will contain instructions: one on each line. The instructions will look like this:

`COMMAND | AMOUNT | ACCOUNT NUMBER | PIN CODE`

`COMMAND` will be either `add` or `sub`. If the command is `add`, you will add `AMOUNT` to the `BALANCE` in the account files **( F1 )**. If the command is `sub`, you will subtract. 

However, there are a number of reasons for which you may need to reject the transaction. If you are asked to subtract an amount that would put the account below zero or if the pin code you are provided does not match the pin code in the account record, the transaction is ignored.


{Check It!|assessment}(test-1550596684)


|||guidance
### Solution
```python
# Get the filepath from the command line
import sys
F1= sys.argv[1] 
F2= sys.argv[2]

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
    account= a[i]
    for j in range(0, len(account)):
      account[j]= str(account[j])
      
    text = text + "|".join(account) + "\n"
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
for transactionIndex in range(0, len(transactions)):
  transaction= transactions[transactionIndex]
  if(len(transaction) >= 4):
    # look through the accounts for the matching account
    for accountIndex in range(0,len(accounts)):
      account= accounts[accountIndex]
      if(len(account) >= 3):                      # make sure we have 
        balance= int(account[2])                  # enough fields
        transactionAmount= int(transaction[1])
        if(account[0] == transaction[2]):         # account matches?
          if(account[1] == transaction[3]):       # pin code matches?
            if(transaction[0] == 'add'):          
              accounts[accountIndex][2]= balance + transactionAmount 
            elif (transaction[0] == 'sub' and transactionAmount <= balance):
              accounts[accountIndex][2]= balance - transactionAmount           

          
# Write the answer back out to the original file
open(F1, 'w').write(a2pipe(accounts))


```
|||