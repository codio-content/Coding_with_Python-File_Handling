In order to read a text file, the **encoding type** or, *how the file was encoded* must be known. Once we know the *encoding type*, it is easy to convert the bytes of data in a file into text.

ASCII (1963)
----
The American Standard Code for Information Interchange (ASCII) maps each byte in a file to a single character. The value 65 (*01000001 in binary*) represents the character ‘A’; 32 is a blank space. Some of the ASCII characters are non-printable characters that were used historically as instructions to a printer. Originally, only 128 characters (7 bits) were used, so all the normal printable characters are in the first 128 places.

ISO-8859-X (1985)
----
In order to add additional characters for other languages, the International Organization for Standardization (ISO) issued several character sets which were the same as ASCII with some of the “extra” typically unused characters changed to the missing characters for other languages. The series 8859 are encodings of Latin, 8-bit character sets. 

UTF-8 (1993)
----
The name ‘UTF-8’ is derived from: * **U**niversal Coded Character Set + **T**ransformation **F**ormat—**8**-bit*. UTF-8 has become the standard character set for the World Wide Web, probably due to its support for a wide number of languages and its status as the default character encoding for HTML. UTF-8 is backward compatible with ASCII by having the first 128 characters of UTF-8 the same as ASCII. 

Comparison Table
----
This tables shows how these different encoding types convert binary information into characters for humans to read. Notice that there is no ASCII character for the copyright symbol. UTF-8 uses two bytes to display it.

<table>
<thead><th>Binary</th><th>Decimal</th><th>ASCII</th><th>UTF-8</th></thead>
<tbody>
  <tr>
    <td>01000001</td>
    <td>65</td>
    <td>A</td>
    <td>A</td>
    <td></td>
  </tr>
  <tr>
    <td>01011010</td>
    <td>90</td>
    <td>Z</td>
    <td>Z</td>
  </tr>
  <tr>
    <td>11000010 10101001</td>
    <td>194 169</td>
    <td>─ ┎</td>
    <td>© (Copyright Symbol)</td>
  </tr>
</tbody>
</table>

What?
----
If you don't understand all of this, don't worry. You don't need to know all of it. Just understand that text files are simply binary files with a set of instructions for making them into a set of characters.

