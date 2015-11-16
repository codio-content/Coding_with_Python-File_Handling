Most systems have more than one program running at a time. In order to ensure that multiple programs do not “run into each other” while attempting to use a single file, a program must “open” the file first. This allows the system to restrict access to this file.

{Run the code}(python3 content/open-file.py content/textfiles/poem.txt)

We hang on to the file descriptor so that we can use it later. The file descriptor can be used to read from the file, write to the file, and eventually close the file when we are done with it.

Python wraps all this file handling business up in a single variable to hide the details from the programmer, allowing us to focus on using the file to get what we want from it.
