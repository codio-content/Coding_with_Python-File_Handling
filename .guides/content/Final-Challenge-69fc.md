For your final challenge of this Unit, we will load two files. The first file **( F1 )** will have information about some accounts. It will be pipe-delimited and have one record per line, with these fields:

`ACCOUNT NUMBER | PIN CODE | BALANCE`

The second file **( F2 )** will contain instructions: one on each line. The instructions will look like this:

`COMMAND | AMOUNT | ACCOUNT NUMBER | PIN CODE`

Command will be either `add` or `sub`. If the command is `add`, you will add `AMOUNNT` to the customer total in the account files **( F1 )**. If the command is `sub`, you will subtract. 

However, there are a number of reasons that you may need to reject the transation. If you are asked to subtract an amount that would put the account below zero or if the pin code you are provided does not match the pin code in the account record, the transaction is ignored.



{Check It!|assessment}(test-1690867941)

|||guidance
### Solution
```javascript
// Load the file system library
var fs = require('fs')             

// Get the filepath from the command line
var F1= process.argv[2] 
var F2= process.argv[3]

// Your code goes here


//
// Create a function that turns pipe-delimited strings 
// into 2d arrays
// 
function pipe2a(text){
  var records= text.split("\n")
  for(var i=0; i < records.length; i++){
    records[i]= records[i].split("|")
  }
  return records
}

//
// Create a function that turns 2d arrays into 
// pipe-delimited strings.
// 
function a2pipe(a){
  var text= ""
  for(var i=0; i < a.length; i++){
    var record= a[i]
    text+= record.join("|") + "\n"
  }
  return text;
}

// Read in the accounts and transactions
var accounts= pipe2a(fs.readFileSync(F1, 'utf8'))
var transactions= pipe2a(fs.readFileSync(F2, 'utf8'))

// for each transaction
for(var transactionIndex=0; transactionIndex < transactions.length; transactionIndex++){
  var transaction= transactions[transactionIndex]
  // look for the matching account
  var accountFound= false
  for(var accountIndex=0; !accountFound && accountIndex < accounts.length; accountIndex++){
    var account= accounts[accountIndex]
    var balance= parseInt(account[2])
    var transactionAmount= parseInt(transaction[1])
    if(account[0] == transaction[2]){
      accountFound= true;
      if(account[1] == transaction[3]){
        if(transaction[0] == 'add'){
          accounts[accountIndex][2]= balance + transactionAmount 
        } else if (transaction[0] == 'sub' && change <= balance){
          accounts[accountIndex][2]= balance - transactionAmount           
        }
      }
    }
  }
}

// Write the answer back out to the original file
fs.writeFileSync(F1, a2pipe(accounts), 'utf8')
```
|||