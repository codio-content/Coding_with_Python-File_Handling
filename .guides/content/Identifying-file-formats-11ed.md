Over the years, computer scientists have developed a number of different strategies for working out the format of a file. Here are a few that are still in common use today.

Extensions
----
On some systems, the filename itself is used to provide a clue as to the format of the file. In particular, the *extension* on the end of a file (“.txt”, “.mp3”, “.doc”,  etc) has traditionally been used to identify the format into which a file is expected to be organised.

Magic numbers
----
Another method is called the *magic number* of the file. Originally, this number was the first two bytes of a file and those bytes identified the file type. Later, this concept was extended to multiple bytes. For example, the first few bytes of a GIF-89 image file starts with “GIF89a” in ASCII to specify their format.

MIME type
----
When files are sent using email (SMTP), the server provides a Multipurpose Internet Mail Extensions (MIME) type for the file which identifies it with a string such as “text/html” in a header. This same MIME information is used by HTTP and other Internet protocols. Some operating systems employ MIME information in file metadata to help identify files.