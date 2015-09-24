The code on the left shows how we write data to a file.

{Run the code}(/home/codio/workspace/write.sh)

## Creating some data to write
The top section of code shows defines some tabular data we will write to a CSV file.

The next section of code loops through each row and each row's columns and builds a lines that will be written to the file. See you various counters `r` and `c` are used to find out when we are not at the end of a row or the table.

## Writing the line to file
Finally, we write our string `line` to the file `write-demo.csv`. 

To see this, click on the `write-demo.csv` file tab next to the `write.py` code tab in top of the left pane.
