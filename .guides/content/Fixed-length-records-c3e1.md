Once the format of a file is known, how can it be loaded and read? In this section, you will learn about some of the most common methods for organising files.

One simple way to organise files is to establish an exact length for a record. This allows you to know how much data to read and write for each record. 

For example, the format used might specify sixteen characters for first name, sixteen for a last name, and eight for a birthday in DDMMYYYY order. 

Our file would look like this:

`Adam____________Smith___________11111985`
`Theodore________Anderson________20031990`
`Monty___________Biscuit-Barrel__18101980`

Note that there are no newline characters at the end of the records. It is split up in the example so we can read it.

{Run the test code}(python3 content/parse-text.py)


### The `String.strip()` Function
----
You might find the `strip()` function helpful. It removes white space (gaps) from the beginning and end of a string.

```python
text= '  Words   Other   Words\tTab   '
print(':' + text + ':')
text= text.strip()
print(':' + text + ':')
```
{Run the split test code}(python content/strip.py)

