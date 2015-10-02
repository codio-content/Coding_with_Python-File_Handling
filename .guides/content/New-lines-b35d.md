Did you notice how the first example displayed over 4 lines? This is because the new line characters in the file are carried across when displaying it. Those same new line characers tell Python when a line ends when you read the file line by line.

A common name for the new line is *carriage return*. This harks back to the days of the typewriter when a typist had to return the carriage mechanism back to the start of the line. 

We use this character to *delimit* (separate) one line from another. This is rather like we used the `,` to separate items in a list.

## A list of lines

Python conveniently treats the file as a list of lines for easy looping:

```python
for line in myFile:
```

Each element in the list is a line from the file:

```python
myFile = [
  'Mary had a little lamb',
  'Whose fleece was white as snow',
  'And everywhere that Mary went',
  'Her lamb was sure to go'
]

