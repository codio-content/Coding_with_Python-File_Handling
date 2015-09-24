Having this sort of data in a single string is not much use, however. 

We need to *parse* it into a proper Javascript array. Parse means *to split up data based on some rules*.

{Run the code}(/home/codio/workspace/read2.sh)

## String .split() method

Here's a reminder of our file data.

```python
Alice,23,Blue,Audi
Tariq,18,Red,Mini
Bob,31,Green,Renault
```

### Columns
A String's `split()` method will split a string at each occurence of the supplied string and then return the result as a list.

```python
  columns = line.split(',')
```

We store the list in a variable called columns and then append it to our list of rows. We have now constructed a table of rows and each row contains columns.
