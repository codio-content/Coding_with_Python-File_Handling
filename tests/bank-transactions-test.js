var fs= require('fs');
var test = require('./test-fw.js');

function copyFileToFile(src, dst){
  fs.writeFileSync(dst, fs.readFileSync(src, 'utf8'), 'utf8');
}

function loadAccounts(pathToAccounts){
  var text= fs.readFileSync(pathToAccounts, 'utf8').trim()
  var accounts= text.split("\n").map(function(n){ return n.split("|"); });
  accounts= accounts.filter(function(n){ return (n && n.length > 0) })
  return accounts;
}

function loadTransactions(pathToTransactions){
  var text= fs.readFileSync(pathToTransactions, 'utf8').trim()
  var tx= text.split("\n").map(function(n) { return n.split("|") })
  return tx;
}

function a2dToPipeDelim(a2d){
  return a2d.map(function(n,i){ return n.join("|"); }).join("\n");
}

function generateTestTransactions(pathToAccounts, pathToTransactions){
  var result= [];
  var accounts= loadAccounts(pathToAccounts);
  if(accounts.length > 0){
    var a= accounts[7 % accounts.length];        // semi random selection
    result.push(['add', 1000, a[0], a[1]]);      // add some
    result.push(['add', 1000, a[0], +a[1] + 1]); // bad pin
    
    a= accounts[5 % accounts.length];            // semi random selection
    result.push(['sub', a[2], a[0], a[1]]);      // good sub
    result.push(['sub', 10000, a[0], a[1]]);     // bad sub

    a= accounts[17 % accounts.length];               // semi random selection
    result.push(['add', 1000, a[0], a[1]]);          // add some
    result.push(['add', 1000, a[0] + '9999', a[1]]); // bad acct
    result.push(['sub', +a[2] + +100, a[0], a[1]]);  // bad sub
  }
  
  var out= a2dToPipeDelim(result);
  
  fs.writeFileSync(pathToTransactions, out, 'utf8');
}

function buildTest(pathAccounts, tmpFilenameIn, tmpFilenameOut){
  var F1= '/tmp/f1-' + tmpFilenameIn;
  var F2= '/tmp/f2-' + tmpFilenameOut;
  
  copyFileToFile(pathAccounts, F1);
  generateTestTransactions(F1, F2);
  
  
  var accounts= loadAccounts(F1);
  var transactions= loadTransactions(F2);
  
  accounts= accounts.map(function(account){
    var currentBalance= parseInt(account[2]);
    transactions.forEach(function(transaction){
      if(transaction[2] == account[0] && transaction[3] == account[1]){
        var prebal= currentBalance;
        var delta= parseInt(transaction[1]);
        if(transaction[0] == 'add'){
          currentBalance= currentBalance + delta;
        } else if(transaction[0] == 'sub' && delta <= currentBalance) {
          currentBalance= currentBalance - delta;
        }
      }
    });
    account[2]= currentBalance;
    return account;
  });
  
	var correctOutput= a2dToPipeDelim(accounts);
  
  return {
		inputs: [F1, F2],
		outputs: [],
    validate: function(i){
      var actualOutput= a2dToPipeDelim(loadAccounts(i.inputs[0]))
      //var actualOutput= fs.readFileSync(i.inputs[0], "utf8").replace(/\s\s*$/, '');
      var resultAsExpected= correctOutput == actualOutput;
      if(!resultAsExpected){
        console.info("You gave:\n" + actualOutput)
        console.info("Expected:\n" + correctOutput)
      }
      return resultAsExpected;
		}
	}
}

var script = 'challenges/bank-transactions.js';

var cpath= 'content/textfiles';

test.tests(script, [
	buildTest(cpath+'/accounts.txt', 'a1', 'tx1'),
	buildTest(cpath+'/accounts.txt', 'a2', 'tx2'),
	buildTest(cpath+'/accounts.txt', 'a3', 'tx3')
]);
