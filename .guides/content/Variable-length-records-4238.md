Another way to store data is called a *variable length record*. Instead of using a set amount of space for fields and records, it stores only what is needed. This saves space and allows for storing much longer records, however, it is slightly more complex to read.

Field delimited data
----
The “|” (pipe) character is not used in normal sentences. Therefore, it is a commonly used character to delimit fields in a variable length record. These are called “pipe delimited” files and they have the constraint that no pipe characters can occur in the data. Usually, each record is one line long (newline delimited) and each field is separated by a pipe character.

Hints:
----
### Use functions of your own
Working with files and records is a great time to use functions. The example program provided in the challenge has **stubs** (empty functions) for you to fill out.


### Array.join()
There is a function named `join()` that will convert an array of strings into a single string with a delimiter between the parts:

```python
list= ['a', 'b', 'c']
delimiter= ':'
print(delimiter.join(list))
```
{Run the code}(python content/join.py)

### String.split() function
There is another function called `split()` that you may find will help you: 

```python
text= 'a:b:c:d'
delimiter= ':'
list= text.split(delimiter)
print(str(list))
```
{Run the code}(python content/split.py)

Sample program:
----
Look at the sample code provided. It uses a simple pipe delimited string. The code uses the `split()` function to convert pipe delimited strings into lists:
```python
6  def getListFromPipeDelimitedText(pipeDelimitedText):
7    recordList= pipeDelimitedText.split('|')
8    return recordList
```

The code also uses the `join()` function to convert lists into pipe delimited strings:

```python
11  def getPipeDelimitedTextFromList(recordList):
12    return ('|').join(recordList)
```
{Run the Pipe Sample Program}(python3 content/pipe-split.py)

Use what you have learned here to help you with the next challenge.
