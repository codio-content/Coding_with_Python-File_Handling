Another way to store data is called a *variable length record*. Instead of using a set amount of space for fields and records, it stores only what is needed. This saves space and allows for storing much longer records.

Field Delimited Data
----
Since we do not use the “|” (pipe) character in normal sentences, it is a commonly used character to delimit fields in a variable length record. These are called “pipe delimited” files are they have the constraint that no pipe characters can occur in the data. Usually each record is one line long (newline delimited) and each field is separated by a pipe character.

Hints:
----
### Use Functions of Your Own
Working with files and records is a great time to use functions. The example program provided in the challenge has **stubs**, empty functions, for you to fill out to help.


### Array.join()
There is a function named `join()` that will convert an array of strings into a single string with a delimiter between the parts.

```python
list= ['a', 'b', 'c']
delimiter= ':'
print(delimiter.join(list))
```
{Run the code}(python content/join.py)

### The String.split() function
There is another function called `split()` that you may find will help you. 

```python
text= 'a:b:c:d'
delimiter= ':'
list= text.split(delimiter)
print(str(list))
```
{Run the code}(python content/split.py)



{Check It!|assessment}(test-4023378015)


|||guidance
### Solution
```python
# Get the filepath from the command line
import sys
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]

# ----------------------------------------------------------------
# 
# Our Helper functions:
# 
# ----------------------------------------------------------------

#
# Loads the file at filepath 
# Returns a 2d array with the data
# 
def load2dArrayFromFile(filepath):
  # Your code goes here:
  f= open(filepath)
  t= f.read()
  lines= t.split("\n")
  for i in range(0, len(lines)):
    lines[i]= lines[i].split("|")
  return lines

#
# Searches the 2d array 'records' for firstname, lastname.
# Returns the index of the record or -1 if no record exists
# 
def findIndex(records, firstname, lastname):
  # Your code goes here:
  for i in range(0, len(records)):
    if(records[i][0] == firstname and records[i][1] == lastname):
      return i
  return -1

# Sets the birthday of the record at the given index
# Returns: nothing
def setBirthday(records, index, newBirthday):
  # Your code goes here:
  if(index >= 0):
    records[index][2]= newBirthday
  
# Convert the 2d array back into a string
# Return the text of the 2d array
def makeTextFrom2dArray(records):
  # Your code goes here:
  for i in range(0,len(records)):
    records[i]= "|".join(records[i])
  return "\n".join(records)    
  
# ----------------------------------------------------------------
# 
#  Our main code body, where we call our functions.
#  
# ----------------------------------------------------------------

# Load our records from the file into a 2d array
records= load2dArrayFromFile(P)

# Find out which index, if any, has the name we are hunting
indexWeAreHunting= findIndex(records, F, L)

# Set the birthday record to the one we were passed
setBirthday(records, indexWeAreHunting, B)

# Convert the records into a text string
output= makeTextFrom2dArray(records)

# Your code goes here
# write the text string out to the file
o= open(P, 'w')
o.write(output)
o.close()


```
|||