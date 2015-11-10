Another way to store data is called a *variable length record*. Instead of using a set amount of space for fields and records, it stores only what is needed. This saves space and allows for storing much longer records.

Field Delimited Data
----
Since we do not use the “|” (pipe) character in normal sentences, it is a commonly used character to delimit fields in a variable length record. These are called “pipe delimited” files are they have the constraint that no pipe characters can occur in the data. Usually each record is one line long (newline delimited) and each field is separated by a pipe character.

Hint: Use Functions
----
Working with files and records is a great time to use functions. The example program provided in the challenge has **stubs**, empty functions, for you to fill out to help.


{Check It!|assessment}(test-4023378015)


|||guidance
### Solution
```python
// Load the file system library
var fs = require('fs')             

// Get the filepath from the command line
var P= process.argv[2] 
var F= process.argv[3]
var L= process.argv[4]
var B= process.argv[5]

// ----------------------------------------------------------------
// 
// Our Helper functions:
// 
// ----------------------------------------------------------------

//
// Loads the file at filepath 
// Returns a 2d array with the data
// 
function load2dArrayFromFile(filepath){
  // Your code goes here:
  var text= fs.readFileSync(filepath, 'utf8')
  var records= text.split("\n")
  for(var i=0; i < records.length; i++){
    records[i]= records[i].split("|")
  }
  return records
}

//
// Searches the 2d array 'records' for firstname, lastname.
// Returns the index of the record or -1 if no record exists
// 
function findIndex(records, firstname, lastname){
  // Your code goes here:
  for(var i=0; i < records.length; i++){
    if(records[i][0] == firstname && records[i][1] == lastname){
      return i
    }
  }
  return -1
}

// Sets the birthday of the record at the given index
// Returns: nothing
function setBirthday(records, index, newBirthday){
  // Your code goes here:
  if(index >= 0 && index < records.length){
    records[index][2]= newBirthday
  }
}

// Convert one record into a pipe-delimited string
function makeLineFromRecord(record){
  // Your code goes here:
  return record.join("|");
}

// Convert the 2d array back into a string and return it
function makeTextFrom2dArray(records){
  // Your code goes here:
  var lines= []
  for(var i=0; i < records.length; i++){
    lines.push(makeLineFromRecord(records[i]))
  }
  return lines.join("\n")
}

// ----------------------------------------------------------------
// 
//  Our main code body, where we call our functions.
//  
// ----------------------------------------------------------------

// Load our records from the file into a 2d array
var records= load2dArrayFromFile(P)

// Find out which index, if any, has the name we are hunting
var indexWeAreHunting= findIndex(records, F, L)

// Set the birthday record to the one we were passed
setBirthday(records, indexWeAreHunting, B)

// Convert the records into a text string
var output= makeTextFrom2dArray(records)

// write the text string out to the file
fs.writeFileSync(P, output, 'utf8')



```
|||