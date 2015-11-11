import test
import sys
import re

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def copyFileToFile(src, dst):
  open(dst, 'w').write(open(src, 'r').read())

def file2array(path):
  text= open(path).read()
  return map(lambda n: return n.split("|"), text.split("\n"))
  
def array2file(records, path):
  open(path, 'w').write(a2dToPipeDelim(records))
  
def a2dToPipeDelim(a2d):
  return "\n".join(map(lambda n: return "|".join(n), a2d))
  
def generateTestTransactions(pathToAccounts, pathToTransactions):
  result= []
  accounts= file2array(pathToAccounts)
  if(accounts.length > 0):
    a= accounts[7 % accounts.length]          # semi random selection
    result.append(['add', 1000, a[0], a[1]])      # add some
    result.append(['add', 1000, a[0], +a[1] + 1]) # bad pin
    
    a= accounts[5 % accounts.length]          # semi random selection
    result.append(['sub', a[2], a[0], a[1]])      # good sub
    result.append(['sub', 10000, a[0], a[1]])     # bad sub

    a= accounts[17 % accounts.length]         # semi random selection
    result.append(['add', 1000, a[0], a[1]])          # add some
    result.append(['add', 1000, a[0] + '9999', a[1]]) # bad acct
    result.append(['sub', +a[2] + +100, a[0], a[1]])  # bad sub 
  
  # Write out the transactions to the file
  array2file(result, pathToTransactions)
  
  
def correctOutput(inputs):
  accounts= file2array(inputs[0])
  transations= file2array(inputs[1])
  for transactionIndex in range(0, len(transactions)):
    transaction= transactions[transactionIndex]
    for accountIndex in range(0, len(accounts)):
      account= accounts[accountIndex]
      if(transaction[2] == account[0]):
        if(transaction[3] == account[1]):
          balance = int(account[2])
          change= int(transaction[1])
          if(transaction[0] == 'add'):
            accounts[accountIndex][2] = balance + change
          if(transaction[0] == 'sub' and change < balance):
            accounts[accountIndex][2]= balance - change
        else:
          # bad pin code
      else:
        # this is not the right account number for this transaction
  return a2dToPipeDelim(accounts)

  
def validate(inputs, internalTestOutput, studentSTDOUT):
  studentFileOutput= open(input[0], 'r').read()
  return studentFileOutput == internalTestOutput

  
script = 'challenges/bank-transactions.py'
CPATH= 'content/textfiles'

def runTest(accountPath, id=0):
  tmpAccountPath= '/tmp/account'+id
  tmpTransactionPath= '/tmp/transaction'+id
  copyFileToFile(accountPath, tmpAccountPath)
  generateTestTranactions(tmpAccountPath, tmpTransactionPath)
  test.test(script, [tmpAccountPath, tmpTransactionPath], correctOutput, _validate=validate)
  
logging.debug("RUNNING TEST")  
runTest(CPATH+'/accounts.txt', 1)
#runTest(CPATH+'/accounts.txt', 1)
#runTest(CPATH+'/accounts.txt', 1)
